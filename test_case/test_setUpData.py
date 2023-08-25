# 前置处理 添加员工 添加企业
import os
import allure
import pytest
from rootpath import rootpath
from util.api_method import request_Util
from util.operate_csv import parse_csv
from util.operate_yaml import read_case_yaml


@allure.feature("初始化数据")
@pytest.mark.setup
class Test_setUp:

    """
    创建内部法人单位
    """

    @allure.title("使用初始的测试数据信息" "创建内部法人单位")
    @pytest.mark.run(order=1)
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/company/create_company.yaml")),
    )
    def test_create_company(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    """
    个人实名认证
    """

    @allure.title("完成测试数据中的个人信息认证")
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/user/auth_user.yaml")),
    )
    def test_authUser(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
