import os

import allure
import pytest

from apitest.util.auto_deploy import MyService
from apitest.util.rootpath import rootpath

from apitest.util.operate_yaml import read_case_yaml
from apitest.util import log


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
