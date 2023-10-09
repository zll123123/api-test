import glob

import pytest
import os
import subprocess
from util.send_mail import SendEmail

# if __name__ == "__main__":
#     pytest.main(["./test_case/test_deploy.py", "-s","-q"])
#     # pytest.main(["./test_case/test_seal.py::Test_seal::test_auto_create_seal", "-s"])
#     # SendEmail().send_main()


def run_tests():

    test_files = ["./test_case/test_deploy.py", "./test_case/test_activate.py"]
    story_name = "active"

    # test_files = ["./test_case/test_deploy.py","./test_case/test_activate.py"]
    test_files=glob.glob('./test_case/app/*.py')
    # story_name = "active"
    story_name=""
    command = f"pytest -m \"{story_name}\" {' '.join(test_files)} -s"

    subprocess.run(command, shell=True)


if __name__ == "__main__":
    run_tests()