from Pages.LoginPage import Login
from Pages.SettingPage import Setting

# 返回各个页面对象，方便用例调用
# 所有页面都继承了base类
# 所有元素都放在__init__内，统一管理
class Page_Obj():
    def __init__(self, driver):
        self.driver = driver

    def Login_Page(self):
        return Login(self.driver)

    def Setting_Page(self):
        return Setting(self.driver)