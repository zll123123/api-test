import subprocess
import time

import requests
import os
import tarfile
from apitest.util import log


class MyService:
    def __init__(self, name, svc_name, svc_display_name, service_path, oss_url):
        self.extract_flag = 0

        self.svc_name = svc_name
        self.svc_display_name = svc_display_name
        self.service_path = service_path
        self.oss_url = oss_url

    # 服务的属性配置

    def extract_pack(self, file_path, target_dir):
        try:
            with tarfile.open(file_path, "r:gz") as tar:
                tar.extractall(target_dir)
            log.logger.info(f"成功解压tar.gz文件: {file_path}")
            self.extract_flag = 1
        except Exception as e:
            log.logger.error(f"解压tar.gz文件时出现错误: {str(e)}")

    def execute_bat(self, target_dir, bat_name):
        bat_path = os.path.join(target_dir, "bin", bat_name)
        bat_dir = os.path.join(target_dir, "bin")
        if os.path.exists(bat_path):
            os.chdir(bat_dir)
            try:
                win32api.ShellExecute(0, "open", bat_path, "", bat_dir, 1)
                log.logger.info(f"成功执行{bat_name}文件: {bat_path}")
            except Exception as e:
                log.logger.error(f"执行{bat_name}文件时出现错误: {str(e)}")
        else:
            log.logger.error(f"未找到{bat_name}文件: {bat_name}")

    def check_service(self):
        try:
            response = requests.get(self.oss_url)
            if response.status_code == 200:
                log.logger.info(f"页面 '{self.oss_url}' 正常打开")
            else:
                log.logger.error(f"页面 '{self.oss_url}' 返回了错误状态码：{response.status_code}")
        except requests.RequestException as e:
            log.logger.error(f"无法访问页面 '{self.oss_url}': {str(e)}")

    def auto_deploy(self):
        # 进入部署目录
        os.chdir(self.service_path)
        # 获取目录中以tar.gz结尾的文件
        tar_gz_files = []
        for file_pack in os.listdir():
            if file_pack.lower().endswith(".gz"):
                tar_gz_files.append(file_pack)
        pack_nums = len(tar_gz_files)
        if pack_nums == 1:
            log.logger.info("开始解压安装包")
            # 获取被解压文件的完整路径
            file_path = os.path.join(self.service_path, tar_gz_files[0])
            self.extract_pack(file_path, self.service_path)
            time.sleep(5)
            if self.extract_flag:
                self.execute_bat(self.service_path, "start.bat")
            time.sleep(100)
            # 检查服务状态,成功后再进行后续操作
            self.check_service()
        else:
            log.logger.error(f"安装包数量异常")

    def stop_service(self, service_name):
        subprocess.run(["sc", "stop", service_name])

    def restart_service(self):
        # 进入部署目录
        os.chdir(self.service_path)
        self.stop_service(self.svc_name)
        self.execute_bat(self.service_path, "start.bat")
        time.sleep(100)
        self.check_service()
        log.logger.info("服务已成功重启")
