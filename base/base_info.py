import hashlib
import rootpath
import time

from util.operate_yaml import getData


class login_info:
    def __init__(self):
        # 获取字典信息
        api_path = rootpath.rootpath + "/config/apiConfig.yaml"
        appSecret = getData(api_path, "apitest", "app_secret")
        app_token = getData(api_path, "apitest", "app_token")
        address = getData(api_path, "apitest", "address")
        times = str(int(time.time() * 1000))
        signature_hash = hashlib.md5((app_token + appSecret + times).encode("utf-8"))
        signature = signature_hash.hexdigest()
        self.url = address
        self.app_token = app_token
        self.signature = signature
        self.time = times
        self.default_header = {
            "x-qys-accesstoken": self.app_token,
            "x-qys-signature": self.signature,
            "x-qys-timestamp": self.time,
        }

if __name__ == '__main__':
    getData()