import os

import allure
import pytest

import rootpath
import logging
from util.auto_depoly import MyService
from util.operate_yaml import read_case_yaml


class Test_depoly:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/depoly_info.yaml")),
    )
    @allure.title("windows下部署qiyuesuo服务")
    def test_depoly(self, new_case_info):
        logging.info(f"{new_case_info}")
        MyService(**new_case_info).auto_depoly()
        MyService.check_service()

    # 获取产品识别码
    def get_active_code(self):
        pass
