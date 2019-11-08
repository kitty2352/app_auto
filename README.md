# Python + appiums + yaml数据驱动 + Pytest+ Allure定制报告

## 项目目录结构
      - Common # 存储基础设施类
          - __init__.py # 空文件
          - config.py # 手机驱动对象初始化
          - base.py # 方法的二次封装
          - Read_Data.py #数据解析读取方法
      - Page # 存储封装页面文件
          - __init__.py # 存储页面元素
          - Page.py  # 封装各个页面对象，方便调用
          - LoginPage.py # 封装登录页面元素的操作方法
          - SettingPage.py # 封装设置页面元素的操作方法
      - Data # 存储数据文件
          - data.yaml(也可以是其他文件比如txt，excel，json，数据库等)
      - Cases # 存储测试脚本目录
          - test.py # 测试
          - test_login.py # 测试登录功能
          - tes_login1.py # 测试登录功能（使用yaml数据文件中的数据方式驱动）
      - pytest.ini # pytest运行配置文件
      - report # 存放测试报告
          - html index.html (测试报告，推荐使用chrome打开)
       


##使用方法：

在cmd下运行命令：
* pytest （运行测试用例代码）
* allure generate --clean  report/ -o report/html（）

