import os
import pytest


from unitest.util.operate_yaml import clean_yaml
from unitest.util import rootpath


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    yamlpath = os.path.join(rootpath, "config/extract.yaml")
    clean_yaml(yamlpath)
