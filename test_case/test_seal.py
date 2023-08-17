import os.path

import pytest
import allure

from rootpath import rootpath
from util import log
from util.api_method import request_Util

from util.operate_csv import parse_csv
from util.operate_yaml import read_case_yaml


@pytest.mark.seal
class Test_seal:
    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(
                os.path.join(rootpath, "test_data/seal/company_seal_create.yaml")
            )
        ),
    )
    @pytest.mark.run(order=2)
    @allure.story("创建企业公章")
    def test_create_company_seal(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    """
        自动生成创建印章
        """

    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(
                os.path.join(rootpath, "test_data/seal/seal_create_auto.yaml")
            )
        ),
    )
    @pytest.mark.run(order=3)
    @allure.story("v2接口创建印章")
    def test_auto_create_seal(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    """
    获取印章列表接口
    """

    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(os.path.join(rootpath, "test_data/seal/seal_list.yaml"))
        ),
    )
    @pytest.mark.run(order=4)
    @allure.story("获取印章列表接口")
    def test_getseal_list(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    """
    变更印章状态
    """

    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(os.path.join(rootpath, "test_data/seal/seal_status.yaml"))
        ),
    )
    @pytest.mark.run(order=5)
    @allure.story("变更印章状态")
    def test_change_sealstatus(self, new_case_info):
        log.logger.info(f"new_case_info is {new_case_info}")
        request_Util().analyse_yaml(new_case_info)
