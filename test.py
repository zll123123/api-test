import json
import os

import jsonpath

if __name__ == "__main__":
    # 去除转义字符
    str1 = '{"code":0,"message":"SUCCESS","result":{"pageNo":1,"pageSize":10,"result":[{"id":"3125464328683655374","name":"萌点科技-layla.zhang1691248764","createTime":"2023-08-05 23:19:24","pm":"zll_03","am":"zll_01","cs":"zll_02","contact":"PASSPORT","contactPhone":"1234567890","agentId":"10000","agentName":"上海亘岩网络科技有限公司","source":"MANUAL","auth":false,"status":"BUILDING","online":false,"platformType":"PRIVATE","balanceState":"normal","balance":"0","feeState":"normal","totalRecharge":"0","apps":["PRIVATE"],"sorter":"3125464328683655374","systemId":"测试12344555","searchName":"萌点科技-layla.zhang1691248764-测试12344555","platFeeRuleStatus":"未设置"}],"totalCount":1,"hasNext":false,"totalPages":1,"nextPage":1,"hasPre":false,"prePage":1,"first":1}}'

    data = json.loads(str1)
    print(data)

    agrs = "result.result[0].id"

    # 使用 jsonpath 来提取属性值
    result = jsonpath.jsonpath(data, "$." + agrs)
    print(result[0])
