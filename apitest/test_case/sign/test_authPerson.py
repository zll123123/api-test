import os

import pytest

from apitest.util.rootpath import rootpath
from apitest.util.api_method import request_Util
from apitest.util.operate_yaml import read_case_yaml


class TestAuth:
    # 获取个人的userId
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/cloud/auth/get_userinfo.yaml")
        ),
    )
    @pytest.mark.run(order=2)
    def test_getUserInfo(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    # 获取个人实名认证链接
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/cloud/auth/person_authurl.yaml")
        ),
    )
    @pytest.mark.run(order=3)
    def test_person_authurl(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    # 获取auth服务的token和ticket
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/cloud/auth/person_authentication.yaml")
        ),
    )
    @pytest.mark.run(order=4)
    def test_person_authentication(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    # 上传证件照图片
    @pytest.mark.testapi
    @pytest.mark.parametrize(
        "new_case_info",
        read_case_yaml(
            os.path.join(rootpath, "test_data/cloud/auth/person_card_image.yaml")
        ),
    )
    @pytest.mark.run(order=5)
    def test_upload_person_image(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)

    #
    #     # 提交实名认证信息
    #     @pytest.mark.testapi
    #     @pytest.mark.parametrize(
    #         "new_case_info",
    #         read_case_yaml(
    #             os.path.join(rootpath, "test_data/cloud/auth/submit_person_auth.yaml")
    #         ),
    #     )
    #     @pytest.mark.run(order=6)
    #     def test_submit_authInfo(self, new_case_info):
    #         request_Util().analyse_yaml(new_case_info)
