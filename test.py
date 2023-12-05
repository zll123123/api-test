import json
import os
import re

import jsonpath

from apitest.util import log
from apitest.util.validate import recognize_re


def get_data():
    res = '{"result":"https://person-auth.qiyuesuo.me?ticket=dIaAEUyCc8Rgzk1p107GcdYCjhy3TtDIqid3Qwx9eSFUC59plwPH0hfZ9Qq6%2FX6u&channel=PRIVATE","code":0,"message":"\u8BF7\u6C42\u6210\u529F"}'
    res1 = json.loads(res)
    caseinfo = {"auth_url": r"(https?://[^\s?]+)"}
    extract_data = {}
    for key, value in caseinfo.items():
        log.logger.info(f"要提取的参数的为{key},{value}")
        # 正则提取
        if recognize_re(value):
            log.logger.error(1)
            match = re.search(value, res).group(0)
            log.logger.error("值为" + match)
            extract_data[key] = match


if __name__ == "__main__":
    get_data()
