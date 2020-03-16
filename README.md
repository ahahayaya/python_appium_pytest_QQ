# python_appium_pytest_QQ

python + appium + pytest编写

#comm
    #comm模块:comm类封装了元素的定位、点击、输入操作
    #init_data模块:从yaml文件种读取测试准备数据
    #init_driver模块：封装启动参数函数
#page
    #page模块：page类继承自comm模块中的comm类
    #__init__.py：按属性存储页面元素
#test_scripts
    #实例化page类，组成业务操作，实现参数化
#data
    #存储测试数据
