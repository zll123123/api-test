import os.path

import pytest
import allure





@pytest.mark.seal
class TestAppLogin:
    @pytest.mark.parametrize(
        "new_case_info",
        parse_csv(
            read_case_yaml(
                os.path.join(rootpath, "/test_data/app/app_login_info.yaml")
            )
        ),
    )

    @allure.story("sign登录")
    def test_create_company_seal(self, new_case_info):
        request_Util().analyse_yaml(new_case_info)
if __name__ == '__main__':
    pytest.main(["./test_case/app/test_app_login.py.py", "-s"])