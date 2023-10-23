import glob

import subprocess


# if __name__ == "__main__":
#     pytest.main(["./test_case/test_deploy.py", "-s","-q"])
#     # pytest.main(["./test_case/test_seal.py::Test_seal::test_auto_create_seal", "-s"])
#     # SendEmail().send_main()


def run_tests():
    test_files = glob.glob("./test_case/*/*.py")
    # story_name = "active"
    story_name = "testapi"
    command = f"pytest -m \"{story_name}\" {' '.join(test_files)} -s"
    subprocess.run(command, shell=True)


if __name__ == "__main__":
    run_tests()
