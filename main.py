import pytest
import os
import subprocess
from util.send_mail import SendEmail

# if __name__ == "__main__":
#     # pytest.main(["./test_case/test_setUpData.py", "-s"])
#     pytest.main(["./test_case/test_activate.py::Test_activate::test_restart_service", "-s"])
#     SendEmail().send_main()


def run_tests():
    # test_files = ["./test_case/test_deploy.py","./test_case/test_activate.py"]
    test_files = ["./test_case/test_activate.py"]
    story_name = "active"
    command = f"pytest -m \"{story_name}\" {' '.join(test_files)} -s"

    subprocess.run(command, shell=True)


if __name__ == "__main__":
    run_tests()
