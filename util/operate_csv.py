import csv
import json

import rootpath

sys_path = rootpath.rootpath


# 读取csv文件
def read_csv(csv_path):
    list_csv = []
    with open(sys_path + csv_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            list_csv.append(row)

        return list_csv


# 解析csv文件
def analysis_csv(case_info):
    case_info_keys = dict(case_info).keys()
    if "parameters" in case_info_keys:
        case_info_str = json.dumps(case_info)
        for key, value in case_info["parameters"].items():
            # 校验csv文件的格式
            param_keys = key.split("-")
            # 获取csv文件数据
            list_data = read_csv(value)
            length_flag = True
            for csv_data in list_data:
                if len(csv_data) != len(list_data[0]):  # 下面的字段值与填写的字段key的个数不一致
                    length_flag = False
                    break
            new_case_info = []
            if length_flag:
                for x in range(1, len(list_data)):  # x表示行数,数据从第一行开始
                    # 每替换一行csv用例数据，yaml的用例字符串需要被还原
                    temp_case_info = case_info_str
                    for y in range(0, len(list_data[x])):  # Y表示列数
                        if list_data[0][y] in param_keys:
                            # 将caseinfo中的变量都替换掉
                            temp_case_info = temp_case_info.replace(
                                "$csv{" + list_data[0][y] + "}", list_data[x][y]
                            )
                            new_case_info.append(json.loads(temp_case_info))
            return new_case_info
    else:
        return case_info


#
# if __name__ == '__main__':
#     data=read_csv('/data/create_seal.csv')
#
