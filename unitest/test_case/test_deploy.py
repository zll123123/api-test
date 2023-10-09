import os

import allure
import pytest
from unitest.util import rootpath
from unitest.util import MyService
from unitest.util.operate_yaml import read_case_yaml
from unitest.util import log


@pytest.mark.active
class Test_depoly:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/deploy/deploy_info.yaml")),
    )
    @allure.title("windows下部署qiyuesuo服务")
    def test_deploy(self, new_case_info):
        log.logger.info(f"{new_case_info}")
        MyService(**new_case_info).auto_deploy()
