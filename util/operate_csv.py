import csv
import json
import os
from util import log
from rootpath import rootpath


# 读取csv文件
def read_csv(csv_path):
    list_csv = []
    with open(os.path.join(rootpath, csv_path), mode="r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")  # 指定csv文件分割符
        for row in reader:
            list_csv.append(row)

        return list_csv


# 解析csv文件
def parse_csv(case_info):
    new_case_info = []
    case_info_keys = dict(case_info).keys()
    if "parameters" in case_info_keys:
        case_info_str = json.dumps(case_info)
        log.logger.info(f"case info str is: {case_info_str}")
        for key, value in case_info["parameters"].items():
            log.logger.info(f"key: {key}\nvalue: {value}")
            # 校验csv文件的格式是否一致
            param_keys = key.split("-")
            # 获取csv文件数据
            csv_data = read_csv(value)
            log.logger.info(f"csv_data{csv_data}")
            for x in range(1, len(csv_data)):  # x表示行数,数据从第一行开始
                if len(csv_data[x]) != len(csv_data[0]):  # 下面的字段值与填写的字段key的个数不一致
                    break
                # 每替换一行csv用例数据，yaml的用例字符串需要被还原
                temp_case_info = case_info_str
                for y in range(0, len(csv_data[x])):  # Y表示列数
                    if csv_data[0][y] in param_keys:
                        # 将caseinfo中的变量都替换掉
                        temp_case_info = temp_case_info.replace(
                            "$csv{" + csv_data[0][y] + "}", csv_data[x][y]
                        )
                new_case_info.append(json.loads(temp_case_info))
                log.logger.info(f"sub new_case_info length is {len(new_case_info)}")
        log.logger.info(f"new_case_info length is {len(new_case_info)}")
        return new_case_info

    else:
        log.logger.info(f"parameters not in keys {case_info_keys}")
        return case_info


if __name__ == "__main__":
    data = read_csv(os.path.join(rootpath, "data/create_seal.csv"))
    print(data[0][1])
