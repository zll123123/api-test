# 前置处理 添加员工 添加企业
import os

import pytest
from rootpath import rootpath
from util.api_method import request_Util
from util.operate_csv import parse_csv
from util.operate_yaml import read_case_yaml


class Test_setUp:

    """
    创建内部法人单位
    """

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

    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #
    #         read_case_yaml(os.path.join(rootpath, "test_data/user/auth_user.yaml")
    #     ),
    # )
    # def test_authUser(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
