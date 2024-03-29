import os.path

import pytest
import allure

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util

from apitest.util.operate_csv import parse_csv
from apitest.util.operate_yaml import read_case_yaml


@pytest.mark.seal
class TestOssLogin:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/oss/oss_login_info.yaml")),
    )
    @pytest.mark.run(order=1)
    @pytest.mark.regression
    @allure.story("oss登录")
    def test_oss_login(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
