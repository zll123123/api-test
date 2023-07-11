import time

import requests
import win32serviceutil
import win32service
import win32event
import servicemanager
import socket
import os
import logging
import tarfile

# 定义服务名称和路径
SERVICE_NAME = 'layla_qiyuesuo'
SERVICE_DISPLAY_NAME = 'qiyuesuo'
SERVICE_PATH = r'C:\path\to\your\service.exe'
URL="http://127.0.0.1:9181/"


class MyService(win32serviceutil.ServiceFramework):
    # 服务的属性配置
    _svc_name_ = SERVICE_NAME
    _svc_display_name_ = SERVICE_DISPLAY_NAME
    _exe_name_ = SERVICE_PATH

    global  extract_flag

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(60)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()
    def extract_pack(self,file_path,target_dir):
        extract_flag=0
        try:
            with tarfile.open(file_path, 'r:gz') as tar:
                tar.extractall(target_dir)
            logging.info(f"成功解压tar.gz文件: {file_path}")
            extract_flag=1
        except Exception as e:
            logging.error(f"解压tar.gz文件时出现错误: {str(e)}")

    def execute_start_bat(self,target_dir):
        start_bat_path = os.path.join(target_dir, 'bin', 'start.bat')
        if os.path.exists(start_bat_path):
            try:
                win32api.ShellExecute(0, 'open', start_bat_path, '', target_dir, 1)
                logging.info(f"成功执行start.bat文件: {start_bat_path}")
            except Exception as e:
                logging.error(f"执行start.bat文件时出现错误: {str(e)}")
        else:
            logging.error(f"未找到start.bat文件: {start_bat_path}")

    def check_service(self):
        # try:
        #     service_status = win32serviceutil.QueryServiceStatus(SERVICE_NAME)[1]
        #     if service_status == win32serviceutil.SERVICE_RUNNING:
        #         logging.info(f"服务 '{SERVICE_NAME}' 已启动")
        #     else:
        #         logging.error(f"服务未启动")
        # except Exception as e:
        #     logging.error(f"服务状态异常:{str(e)}")
        #2.检查9181后台是否能打开，能打开则服务运行正常
        try:
            response = requests.get(URL)
            if response.status_code == 200:
                logging.info(f"页面 '{URL}' 正常打开")
            else:
                logging.error(f"页面 '{URL}' 返回了错误状态码：{response.status_code}")
        except requests.RequestException as e:
            logging.error(f"无法访问页面 '{URL}': {str(e)}")



    def main(self):
        #进入部署目录
        os.chdir(SERVICE_PATH)
        #获取目录中以tar.gz结尾的文件
        tar_gz_files=[]
        for file_pack in os.listdir():
            if file_pack.lower().endswith(".gz"):
                tar_gz_files.append(file_pack)
        pack_nums=len(tar_gz_files)
        if pack_nums==1:
            #获取被解压文件的完整路径
            file_path=os.path.join(SERVICE_PATH,tar_gz_files[0])
            self.extract_pack(file_path,SERVICE_PATH)
            time.sleep(5)
            if extract_flag:
                self.execute_start_bat(SERVICE_PATH)
            time.sleep(1)
            #检查服务状态
            self.check_service()

        else:
            logging.error(f'安装包数量异常')







if __name__ == '__main__':
    if len(os.sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(MyService)
