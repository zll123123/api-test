import os.path

import pytest
import allure

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util

from apitest.util.operate_yaml import read_case_yaml


@pytest.mark.seal
class TestOrganization:
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/oss/get_root_organization.yaml")
        ),
    )
    @pytest.mark.run(order=2)
    @pytest.mark.regression
    @allure.story("获取顶级组织信息")
    def test_root_organization(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
