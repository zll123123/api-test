import json
import time

import pytest

from rootpath import rootpath
from util.APiMethod import request_Util

from util.operate_csv import analysis_csv, read_csv
from util.operate_yaml import write_yaml, read_case_yaml


class Test_seal:
    @pytest.mark.parametrize('case_info',
                             read_case_yaml(rootpath +
                                            '/test_data/seal_create.yaml'))
    def test_create_seal(self, case_info):
        new_case_info = analysis_csv(case_info)
        for i in range(len(new_case_info)):
            print(i, new_case_info[i])
        import pdb
        pdb.set_trace()
        for case in new_case_info:
            res = request_Util().analyse_yaml(case)

    # # 测试获取印章列表
    # @pytest.mark.parametrize('case_info', read_case_yaml(rootpath + '/test_data/seal_list.yaml'))
    # def test_getseal_list(self, case_info):
    #
