# python_unittest_interface

（1）main.py主运行文件，运行之后可以生成相应的测试报告，并以邮件形式发送；

（2）report文件夹存放测试结果报告；

（3）test_case文件中存放的是测试用例文件、test_data文件中存在的是用例配置文件 yaml 、data目录下存放的是数据文件，主要适用于一个测试用例需要执行多组测试数据时

（4）util对测试接口相关方法的封装；send_mail.py发送邮件的封装；api_method.py接口请求类型的封装。
测试用例文件编写规则：
1.必须有的一级关键字： name request expected
2.request下必须有的耳机关键字 method url
3.get 请求 使用parmas传参
  post 请求 数据是json时 使用json传参
            数据是form表单格式时 使用data传参
            如果需要上传文件时 使用关键字files传参  midea:"文件路径"
4.请求中如果需要提取参数时 ：
 使用extract:
        customerId : result.result[0].id   此写法 ，会提取当前接口返回结果中的result.result[0].id 存储到extract.yaml文件中以便后续使用
例如：
-
  name: 依据licenseId，获取license
  request:
    method: post
    url: /crm/oss/customer/license/generate
    modoule: cloud
    headers:
      Content-Type: application/json
    json:
      id: ${get_extract}(licenseId)
  extract:
    licenseCode: result
  expected:
    - eq: { 'code': 0 }
    - eq: { 'message': SUCCESS }

  ${get_extract}(licenseId)写法标识从extract.yaml提取licenseId 作为参数id的值
- 提取公共配置的值使用表达式${common_data}(key)
- 提取数据库配置文件dbconfig.yaml中值使用表达式${db_data}(key)
5.数据库配置文件中，数据库类型名称需大写，激活的数据库环境也需大写