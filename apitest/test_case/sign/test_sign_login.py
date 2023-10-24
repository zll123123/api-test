import os.path

import pytest
import allure

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util
from apitest.util.operate_yaml import read_case_yaml


class TestSignLogin:
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/sign/sign_login_info.yaml")),
    )
    @pytest.mark.testapi
    @allure.story("sign登录")
    @pytest.mark.run(order=1)
    def test_sign_login(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
