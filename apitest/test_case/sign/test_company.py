import os.path

import pytest
import allure

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util

from apitest.util.operate_yaml import read_case_yaml


class TestCompany:
    @pytest.mark.regression
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/sign/company_create_info.yaml")
        ),
    )
    @allure.story("创建法人单位")
    @pytest.mark.run(order=4)
    def test_create_company(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)


    @pytest.mark.regression
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/sign/company_create_info.yaml")
        ),
    )
    @allure.story("提交法人单位认证")
    @pytest.mark.run(order=4)
    def test_create_company(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)