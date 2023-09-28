import os.path

import pytest
import allure

from rootpath import rootpath
from util import log
from util.api_method import request_Util

from util.operate_csv import parse_csv
from util.operate_yaml import read_case_yaml


@pytest.mark.seal
class TestAppLogin:
    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(
                os.path.join(rootpath, "/test_data/app/create_electronic_seal.yaml")
            )
        ),
    )

    @allure.story("sign平台创建印章")
    def test_create_company_seal(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
