import os.path

import pytest
import allure

from unitest.util import rootpath
from unitest.util.api_method import request_Util

from unitest.util.operate_yaml import read_case_yaml


@pytest.mark.seal
class TestOrganization:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/oss/get_root_organization.yaml")
        ),
    )
    @pytest.mark.regression
    @allure.story("获取顶级组织信息")
    def test_root_organization(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
