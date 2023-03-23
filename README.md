# python_unittest_interface

（1）run.py主运行文件，运行之后可以生成相应的测试报告，并以邮件形式发送；

（2）report文件夹存放测试结果报告；

（3）test_case文件夹是存放测试用例（实际项目中可以按照不同模块新建python package，来存放不同模块的接口用例）；

（4）util对测试接口相关方法的封装：HTMLTestRunner.py生成测试报告的封装；send_mail.py发送邮件的封装；api_method.py接口请求类型的封装。
测试用例文件编写规则：
1.必须有的一级关键字： name request expected
2.request下必须有的二级关键字 method url
3.get 请求 使用parmas传参
  post 请求 数据是json时 使用json传参
            数据是form表单格式时 使用data传参
            如果需要上传文件时 使用关键字files传参  yaml文件中：传参示例：
            files:
              license: /images/营业执照.png
              legalAuthorization: /images/法人授权书.png   key后面写文件路径即可，目前文件都放在images文件夹内
4.请求中如果需要提取参数时 ：
 支持json提取 ，yaml文件中extract关键字下写法如下（示例标识提取result中的name字段到extract.yaml文件中，且字段的key为companyName）
extract:
    companyId : result.id
    companyName: result.name
   