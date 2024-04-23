import os.path

import pytest
import allure

from apitest.util.api_method import request_Util
from apitest.util.operate_yaml import read_case_yaml
from apitest.util.rootpath import rootpath


@pytest.mark.active
class Test_activate:
    @pytest.mark.parametrize("case_info",read_case_yaml(
            os.path.join(rootpath, "test_case/activate/data/active_info.yaml")
        ),)

    def test_activate(self,case_info):
        allure.dynamic.title(case_info["name"])
        request_Util().analyse_yaml(case_info)




    # @pytest.mark.run(order=2)
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(
    #         os.path.join(rootpath, "test_data/cloud/active/identifier.yaml")
    #     ),
    # )
    # @allure.title("从启动的私有云服务中获取产品识别码")
    # def test_get_identifier(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @pytest.mark.run(order=3)
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(os.path.join(rootpath, "test_data/cloud/active/customer.yaml")),
    # )
    # @allure.title("公有云添加客户")
    # def test_add_customer(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(
    #         os.path.join(rootpath, "test_data/cloud/active/get_customer_info.yaml")
    #     ),
    # )
    # @allure.title("获取添加的客户的customerId")
    # def test_get_coustomerId(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(os.path.join(rootpath, "test_data/cloud/active/auth_info.yaml")),
    # )
    # @allure.title("公有云进行企业认证")
    # def test_company_auth(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(
    #         os.path.join(rootpath, "test_data/cloud/active/cooperation_info.yaml")
    #     ),
    # )
    # @allure.title("公有云填写企业开通的功能")
    # def test_set_cooperation(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @allure.title("获取企业的license列表信息")
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(
    #         os.path.join(rootpath, "test_data/cloud/active/license_list_info.yaml")
    #     ),
    # )
    # def test_get_license_list(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @allure.title("依据licenseid,得到license信息")
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(os.path.join(rootpath, "test_data/cloud/active/license.yaml")),
    # )
    # def test_get_licnese(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @allure.title("回写license信息到私有云")
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(
    #         os.path.join(rootpath, "test_data/cloud/active/active_license.yaml")
    #     ),
    # )
    # def test_set_license(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @allure.title("初始化数据库信息")
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(os.path.join(rootpath, "test_data/cloud/active/init_db.yaml")),
    # )
    # def test_init_db(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @allure.title("设置私有云管理员信息")
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(
    #         os.path.join(rootpath, "test_data/cloud/active/admin_info.yaml")
    #     ),
    # )
    # def test_init_db(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
    #
    # @allure.title("重启私有云服务")
    # @pytest.mark.parametrize(
    #     "new_case_info",
    #     read_case_yaml(os.path.join(rootpath, "test_data/deploy/deploy_info.yaml")),
    # )
    # def test_restart_service(self, new_case_info):
    #     request_Util().analyse_yaml(new_case_info)
