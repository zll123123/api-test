import json
import time

import pytest

from rootpath import rootpath
from util.APiMethod import request_Util
from util import log
from util.operate_csv import parse_csv
from util.operate_yaml import read_case_yaml


class Test_seal:
    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(read_case_yaml(rootpath + "/test_data/seal_create.yaml")),
    )
    def test_create_seal(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    # 测试获取印章列表
    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(read_case_yaml(rootpath + "/test_data/seal_list.yaml")),
    )
    def test_getseal_list(self, new_case_info):
        log.logger.info(f"测试用例信息{new_case_info}")
        request_Util().analyse_yaml(new_case_info)
