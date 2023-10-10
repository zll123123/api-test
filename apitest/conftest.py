import os
import pytest


from apitest.util.operate_yaml import clean_yaml
from apitest.util.rootpath import rootpath


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    yamlpath = os.path.join(rootpath, "config/extract.yaml")
    clean_yaml(yamlpath)
