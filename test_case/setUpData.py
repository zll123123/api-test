#前置处理 添加员工 添加企业
import os

import pytest

import rootpath
from util.api_method import request_Util
from util.operate_csv import parse_csv
from util.operate_yaml import read_case_yaml


@pytest.mark.parametrize(
        "new_case_info",
        parse_csv(read_case_yaml(os.path.join(rootpath, "test_data/seal_list.yaml"))),
    )
def test_addUser(self,new_case_info):
    request_Util().analyse_yaml(new_case_info)
