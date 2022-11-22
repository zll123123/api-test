# python_unittest_interface

（1）run.py主运行文件，运行之后可以生成相应的测试报告，并以邮件形式发送；

（2）report文件夹存放测试结果报告；

（3）unit_test文件夹是存放测试用例（demo.py和test_unittest.py用例用法介绍，实际项目中可以按照不同模块新建python package，来存放不同模块的接口用例）；

（4）util对测试接口相关方法的封装：HTMLTestRunner.py生成测试报告的封装；send_mail.py发送邮件的封装；test_get_post.py接口请求类型的封装。
测试用例文件编写规则：
1.必须有的一级关键字： name request expected
2.request下必须有的耳机关键字 method url
3.get 请求 使用parmas传参
  post 请求 数据是json时 使用json传参
            数据是form表单格式时 使用data传参
            如果需要上传文件时 使用关键字files传参  midea:"文件路径"
4.请求中如果需要提取参数时 ：
    支持正则提取
    支持json提取