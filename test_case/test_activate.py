import os

import allure
import pytest

from rootpath import rootpath
from util.api_method import request_Util
from util.operate_yaml import read_case_yaml


class Test_activate:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/active/activate_info.yaml")),
    )
    @allure.title("公有云申请license")
    def test_activate(self, new_case_info):
        request_Util().analyse_yaml(self, new_case_info)

    @allure.title("公有云进行企业认证")
    def test_company_auth(self):
        pass

    @allure.title("获取license")
    def test_get_license(self):
        pass

    def test_set_licnese(self):
        pass

    def test_conn_db(self):
        pass

    def test_init_db(self):
        pass
