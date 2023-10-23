import os

import pytest

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util
from apitest.util.operate_yaml import read_case_yaml


class TestAuth:
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/cloud/auth/person_card_image.yaml")
        ),
    )
    def test_create_company(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)


