import pytest

from util.send_mail import SendEmail

if __name__ == "__main__":
    # pytest.main(["./test_case/test_setUpData.py", "-s"])
    # pytest.main(["-s", ""])
     pytest.main(["./test_case/test_seal.py::Test_seal::test_auto_create_seal", "-s"])
     SendEmail().send_main()