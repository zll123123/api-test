import os.path

import pytest
import allure

from unitest.util import rootpath
from unitest.util.api_method import request_Util

from unitest.util.operate_csv import parse_csv
from unitest.util.operate_yaml import read_case_yaml


@pytest.mark.seal
class TestOssLogin:
    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(os.path.join(rootpath, "test_data/oss/oss_login_info.yaml"))
        ),
    )
    @pytest.mark.regression
    @allure.story("oss登录")
    def test_oss_login(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
