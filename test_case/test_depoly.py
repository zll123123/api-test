import os

import allure
import pytest
from util import log
from rootpath import rootpath
from util.auto_depoly import MyService
from util.operate_yaml import read_case_yaml
from util import log

@pytest.mark.active
class Test_depoly:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(os.path.join(rootpath, "test_data/depoly/depoly_info.yaml")),
    )
    @allure.title("windows下部署qiyuesuo服务")
    def test_depoly(self, new_case_info):
        log.logger.info(f"{new_case_info}")
        MyService(**new_case_info).auto_depoly()



