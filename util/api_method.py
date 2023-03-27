import hashlib
import json
import os
import random
import uuid
from datetime import time
import time
import jsonpath as jsonpath
from util import log
import pytest
import requests

from debug_talk import Debug_talk
from rootpath import rootpath
from util.operate_yaml import getData, write_yaml, read_commData
from util.upload_file import upload_file


class request_Util:
    def __init__(self):
        yamlpath = os.path.join(rootpath, "config/apiConfig.yaml")
        self.base_url = getData(yamlpath, "apitest", "address")

        appSecret = getData(yamlpath, "apitest", "app_secret")
        app_token = getData(yamlpath, "apitest", "app_token")

        times = str(int(time.time() * 1000))
        signature_hash = hashlib.md5((app_token + appSecret + times).encode("utf-8"))
        signacture = signature_hash.hexdigest()
        self.signacture = signacture
        self.app_token = app_token
        self.time = times
        self.default_header = {
            "x-qys-accesstoken": self.app_token,
            "x-qys-signature": self.signacture,
            "x-qys-timestamp": self.time,
        }

    # 替换数据，包含变量的数据可以是url（str），参数（字典或者字典列表），header（字典）
    # def replace_data(self, data):
    #     if data and isinstance(data, dict):
    #         convert_data = json.dumps(data)
    #     else:
    #         convert_data = data
    #         # 循环次数为变量中{{的个数
    #     for i in range(1, convert_data.count('{{') + 1):
    #         if '{{' in data and '}}' in data:
    #             start_index = convert_data.index('{{')  # 获取字符串对应的下标
    #             end_index = convert_data.index('}}')
    #             conver_key_org = convert_data[start_index:end_index + 2]
    #             convert_key = conver_key_org[2:-2]
    #             yamlpath = rootpath + '/config/extract.yaml'
    #             convert_value = get_extract(yamlpath, convert_key)
    #             # 字符串是不可变对象，不能用下标赋值的方式去替换
    #
    #             data = convert_data.replace(conver_key_org, str(convert_value))
    #
    #     if isinstance(data, dict):
    #         data = json.loads(convert_data)
    #     else:
    #         data = data
    #     return data
    # ${get_random_int}(1,500)
    def replace_expression(self, data):
        comm_path = os.path.join(rootpath, "config/common_data.yaml")
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
                    value = read_commData(comm_path, *args_list)
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
            for key, value in caseinfo["extract"].items():
                log.logger.info(f"要提取的参数的为{key},{value}")
                depend_key = value.split(".")
                args_list = ""
                for item in depend_key:
                    args_list += f"['{item}']"
                extract_data[key] = eval(str(res.json()) + args_list)
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
            # 一级关键字request下必须有的二级关键字 method url
            if (
                "method" in dict(caseinfo)["request"].keys()
                and "url" in dict(caseinfo)["request"].keys()
            ):
                url = caseinfo["request"]["url"]
                method = caseinfo["request"]["method"]
                # request下可能有json params files 等,而请求可能会有params json data等，可以约束的是files  headers
                headers = self.default_header
                files = None
                if jsonpath.jsonpath(caseinfo, "$..files"):
                    files = caseinfo["request"].pop("files")
                if jsonpath.jsonpath(caseinfo, "$..headers"):
                    headers = caseinfo["request"]["headers"]
                    headers = self.default_header.update(headers)
                    caseinfo["request"].pop("headers")

                caseinfo["request"].pop("url")
                caseinfo["request"].pop("method")

                res = self.send_request(
                    case_name,
                    url=url,
                    method=method,
                    headers=self.default_header if not headers else headers,
                    files=None if not files else files,
                    **caseinfo["request"],
                )
                self.assert_result(caseinfo["expected"], res)
                self.get_depend_data(caseinfo, res)
            else:
                log.logger.error("request下必须有的二级关键字url method")
        else:
            log.logger.error("必须有的四个一级关键字name base_url request expected")

        return res

    def send_request(self, case_name, url, method, headers, files, **kwargs):
        headers = self.default_header
        # 处理url
        self.url = self.base_url + self.replace_expression(url)

        self.lastmethod = method.lower()

        # 处理header
        if headers and isinstance(headers, dict):
            headers = self.replace_expression(headers)
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
                                            log.logger.error("是结果不等于预期结果")
                                    else:
                                        log.logger.error(f"接口返回中未找到{assert_key}")
                            else:
                                log.logger.error("相等断言的表达式不存在")

                        elif "contains" == key:
                            if value:
                                pytest.assume(
                                    value[0] in str(res.json()), f"实际结果中不包含字段{value}"
                                )

                            else:
                                log.logger.error(f"包含条件未识别到表达式")
                        else:
                            log.logger.error("不支持的断言表达式{key}")
