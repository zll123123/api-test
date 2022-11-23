import pytest
import rootpath

from util.operate_yaml import clean_yaml


@pytest.fixture(scope="session", autouse=True)
def clear_extract():
    yamlpath = yamlpath = rootpath.rootpath + "/config/extract.yaml"
    clean_yaml(yamlpath)
