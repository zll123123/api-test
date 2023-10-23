import os

import pytest

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util
from apitest.util.operate_yaml import read_case_yaml


class TestAuth:

    # 获取个人实名认证链接
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "")
        ),
    )
    def test_person_authurl(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

   #上传证件照图片
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/cloud/auth/person_card_image.yaml")
        ),
    )
    def test_upload_person_image(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)


