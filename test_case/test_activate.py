import os

import allure
import pytest

from rootpath import rootpath
from util.api_method import request_Util
from util.operate_yaml import read_case_yaml


class Test_activate:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/active/customer.yaml")),
    )
    @allure.title("公有云添加客户")
    def test_add_customer(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/active/get_customer_info.yaml")
        ),
    )
    @allure.title("获取添加的客户的customerId")
    def test_get_coustomerId(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/active/auth_info.yaml")),
    )
    @allure.title("公有云进行企业认证")
    def test_company_auth(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/active/cooperation_info.yaml")
        ),
    )

    @pytest.mark.skip("1")
    @allure.title("公有云填写企业开通的功能")
    def test_set_cooperation(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/active/license.yaml")),
    )
    @pytest.mark.skip("1")
    @allure.title("传入id，获取license信息")
    def test_get_licnese(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    #
    #
    # def test_set_license(self,new_case_info):
    #     pass
    #
    # def test_conn_db(self,new_case_info):
    #     pass
    #
    # def test_init_db(self,new_case_info):
    #     pass
