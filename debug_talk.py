import base64
import random

from rootpath import rootpath
from util.operate_yaml import get_extract


class Debug_talk:
    def get_random_int(self, min, max):
        return random.randint(int(min), int(max))

    # 统一都使用热加载的方式来进行数据处理
    def get_extract(self, key):
        return get_extract(key)

    # 将请求中的文件转换成base64编码的字符串
    def image_to_base64(self, path):
        path = rootpath + path
        with open(path, "rb") as img:
            # 使用base64进行编码
            b64encode = base64.b64encode(img.read())
            s = b64encode.decode()
            b64_encode = "data:image/jpeg;base64,%s" % s
            # 返回base64编码字符串
            return b64_encode


if __name__ == "__main__":
    path = "./images/印章01.png"
    (Debug_talk.image_to_base64(path))
