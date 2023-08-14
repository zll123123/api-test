import hashlib
import json

import os
import random
import uuid
from datetime import time
import time


import allure
import jsonpath

from util import log
import pytest
import requests

from debug_talk import Debug_talk
from rootpath import rootpath
from util.operate_yaml import getData, write_yaml,read_commonData,read_dbconfig
from util.upload_file import upload_file


class request_Util:
    def __init__(self):
        yamlpath = os.path.join(rootpath, "config/apiConfig.yaml")
        self.open_url = getData(yamlpath, "open", "openurl")
        self.cloud_url = getData(yamlpath, "cloud", "cloud_url")
        self.oss_url=getData(yamlpath,"oss","oss_url")
        X_Qys_Oss_Token = getData(yamlpath, "cloud", "X-Qys-Oss-Token")
        X_Auth_Qid = getData(yamlpath, "cloud", "X-Auth-Qid")

        appSecret = getData(yamlpath, "open", "app_secret")
        app_token = getData(yamlpath, "open", "app_token")

        times = str(int(time.time() * 1000))
        signature_hash = hashlib.md5((app_token + appSecret + times).encode("utf-8"))
        signacture = signature_hash.hexdigest()
        self.signacture = signacture
        self.app_token = app_token
        self.time = times
        self.X_Qys_Oss_Token = X_Qys_Oss_Token
        self.X_Auth_Qid = X_Auth_Qid
        self.open_default_header = {
            "x-qys-accesstoken": self.app_token,
            "x-qys-signature": self.signacture,
            "x-qys-timestamp": self.time,
        }
        self.cloud_default_header = {
            "X-Auth-Qid": self.X_Auth_Qid,
            "X-Qys-Oss-Token": self.X_Qys_Oss_Token,
        }


    def replace_expression(self, data):
        comm_path = os.path.join(rootpath, "config/common_data.yaml")
        db_path=os.path.join(rootpath, "config/dbconfig.yaml")
        log.logger.info(f"data is {data}")

        if isinstance(data, dict):
            data_new = json.dumps(data, ensure_ascii=False)
        else:
            data_new = data
        for i in range(data_new.count("${")):
            if "${" in data_new and "}" in data_new:
                fun_agrs = data_new[data_new.index("$") : data_new.index(")") + 1]
                func = fun_agrs[fun_agrs.index("{") + 1 : fun_agrs.index("}")]
                args = data_new[data_new.index("(") + 1 : data_new.index(")")]
                # *号的作用是解包，相当于去除['1', '500'] []
                args_list = args.split(":")
                if "common_data" in func:
                    value = read_commonData(comm_path, *args_list)
                elif "db_data" in func:
                    value = read_dbconfig(db_path, env_name,*args_list)
                # split方法分割符不存在时，返回原字符串
                elif not args:
                    # 此处使用的是反射原理
                    value = getattr(Debug_talk(), func)()
                else:
                    value = getattr(Debug_talk(), func)(*args_list)
                data_new = data_new.replace(fun_agrs, str(value))
                log.logger.info(f"替换后的字符串为{data_new}")
        if isinstance(data, dict):
            data = json.loads(data_new)
        else:
            data = data_new
        return data

    # 处理接口返回结果中的依赖数据
    def get_depend_data(self, caseinfo, res):
        if "extract" in dict(caseinfo).keys():
            # json提取
            extract_data = {}
            depend_data = res.json()
            for key, value in caseinfo["extract"].items():
                log.logger.info(f"要提取的参数的为{key},{value}")

                extract_data[key] = jsonpath.jsonpath(depend_data, "$." + value)[0]
            write_yaml(os.path.join(rootpath, "config/extract.yaml"), extract_data)

    # 规范测试用例文件的写法
    def analyse_yaml(self, caseinfo):
        log.logger.info(f"caseinfo is {caseinfo}")
        # 必须有的三个一级关键字name ,request,expected
        caseinfo_keys = dict(caseinfo).keys()

        if (
            "name" in caseinfo_keys
            and "request" in caseinfo_keys
            and "expected" in caseinfo_keys
        ):
            case_name = caseinfo["name"]
            # 一级关键字request下必须有的二级关键字 method url modoule
            if (
                "method" in dict(caseinfo)["request"].keys()
                and "url" in dict(caseinfo)["request"].keys()
                and "modoule" in dict(caseinfo)["request"].keys()
            ):
                url = caseinfo["request"]["url"]
                method = caseinfo["request"]["method"]
                # request下可能有json params files 等,而请求可能会有params json data等，可以约束的是files  headers

                files = None
                if jsonpath.jsonpath(caseinfo, "$..files"):
                    files = caseinfo["request"].pop("files")
                if jsonpath.jsonpath(caseinfo, "$..headers"):
                    headers = caseinfo["request"]["headers"]
                    caseinfo["request"].pop("headers")

                caseinfo["request"].pop("url")
                caseinfo["request"].pop("method")

                res = self.send_request(
                    case_name,
                    url=url,
                    method=method,
                    headers=headers,
                    files=None if not files else files,
                    **caseinfo["request"],
                )

                self.assert_result(caseinfo["expected"], res)
                try:
                    self.get_depend_data(caseinfo, res)
                except Exception:
                    log.logger.error("提取返回依赖结果失败")
            else:
                log.logger.error("request下必须有的二级关键字url method")
        else:
            log.logger.error("必须有的四个一级关键字name open_url request expected")

        return res

    def send_request(self, case_name, url, method, modoule, headers, files, **kwargs):
        # 处理url
        if modoule == "open":
            self.url = self.open_url + self.replace_expression(url)
            headers = self.open_default_header
            if headers and isinstance(headers, dict):
                headers = self.open_default_header.update(headers)
                headers = self.replace_expression(headers)
        elif modoule == "cloud":
            self.url = self.cloud_url + self.replace_expression(url)
            headers = self.cloud_default_header
        else:
            self.url=self.oss_url + self.replace_expression(url)
            headers=headers

        self.lastmethod = method.lower()
        file_map = {}
        if files and isinstance(files, dict):
            for filekey in files:
                filepath = files[filekey]
                filevalue = upload_file(filepath)
                file_map[filekey] = filevalue

        # 处理请求参数，需要处理的是params ,data,json等,此处的可变参数接受到的值不确定是那种，但只对这三种处理
        if isinstance(kwargs, dict):
            for key, value in kwargs.items():
                if key in ["params", "data", "json"] and value:
                    # 如果存在参数值为空，则去掉此字符串传惨
                    for k in list(value.keys()):
                        if value[k] == "":
                            value.pop(k)
                kwargs[key] = self.replace_expression(value)

        sesseion = requests.session()
        log.logger.info(
            f"请求用例->{case_name},请求地址->{self.url},请求方式->{self.lastmethod },请求头->{headers},files->{file_map}，参数{kwargs}"
        )
        allure.attach(
            f"请求用例->{case_name},请求地址->{self.url},请求方式->{self.lastmethod },请求头->{headers},files->{file_map}，参数{kwargs}"
        )
        res = sesseion.request(
            url=self.url,
            method=self.lastmethod,
            headers=headers,
            files=file_map,
            **kwargs,
        )
        return res

    def assert_result(self, expect, res):
        log.logger.info(f"预期{expect},实际结果为{res.json()}")
        with allure.step("进入断言"):
            allure.attach(f"预期{expect},实际接口响应为{res.json()}")
        if expect and isinstance(expect, list):
            for item in expect:
                if item and isinstance(item, dict):
                    for key, value in item.items():
                        # 相等断言
                        if "eq" == key:
                            if value and isinstance(value, dict):
                                for assert_key, assert_value in value.items():
                                    act_value = jsonpath.jsonpath(
                                        res.json(), "$..%s" % assert_key
                                    )
                                    if act_value:
                                        try:
                                            assert assert_value == act_value[0]
                                        except AssertionError:
                                            log.logger.error(
                                                f"实际结果结果{act_value[0]}不等于预期结果{assert_value}"
                                            )
                                            allure.attach(
                                                f"实际结果结果{act_value[0]}不等于预期结果{assert_value}"
                                            )
                                    else:
                                        log.logger.error(f"接口返回中未找到{assert_key}")
                                        allure.attach(f"接口返回中未找到{assert_key}")
                            else:
                                log.logger.error("相等断言的表达式不存在")
                                allure.attach("相等断言的表达式不存在")

                        elif "contains" == key:
                            if value:
                                try:
                                    assert value[0] in str(res.json())
                                except AssertionError:
                                    log.logger.error(f"实际结果中不包含字段{value}")
                                    allure.attach(f"实际结果中不包含字段{value}")
                            else:
                                log.logger.error(f"包含条件未识别到表达式{key}")
                                allure.attach(f"包含条件未识别到表达式{key}")
                        else:
                            log.logger.error(f"不支持的断言表达式{key}")
                            allure.attach(f"不支持的断言表达式{key}")
