import pytest
import os

from util.send_mail import SendEmail

if __name__ == "__main__":
    # pytest.main(["./test_case/test_setUpData.py", "-s"])
    pytest.main(
        [
            "-s",
            "--html=./report/report.html",
            "--alluredir=./allure_result",
            "--clean-alluredir",
        ]
    )
    # pytest.main(["./test_case/test_seal.py::Test_seal::test_auto_create_seal", "-s"])
    # SendEmail().send_main()
