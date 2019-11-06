from appium import webdriver


def init_driver(appPacke='com.krhd.qls.zhxj', appActive='com.krhd.qls.zhxj.ui.login.LoginActivity'):
    # server 启动参数
    desired_caps = {}
    # 设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = '4db643a8'
    # app信息
    desired_caps['appPackage'] = appPacke
    desired_caps['appActivity'] = appActive
    # 允许输入中文
    desired_caps['unicodeKeyboard'] = True
    desired_caps['resetKeyboard'] = True
    # 声明手机驱动对象（服务端地址，服务端请求参数）
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)

    return driver
