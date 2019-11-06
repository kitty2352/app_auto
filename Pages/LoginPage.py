from appium import webdriver
from Common.base import Base
from Pages.SettingPage import Setting
from Common.config import init_driver

# 登录类
class Login(Base):

    # 定位登录页面上的元素
    loc_user = ("id", "com.krhd.qls.zhxj:id/et_login_username")
    loc_password = ("id", "com.krhd.qls.zhxj:id/et_login_password")
    loc_lgbtn = ('id', "com.krhd.qls.zhxj:id/tv_login")
    loc_error = ('id', "com.krhd.qls.zhxj:id/tv_login_error")
    loc_success = ('id', "android:id/button1")
    loc_after = ('id', "android:id/button2")


    def __init__(self, driver):
        self.driver = driver
        # Base.__init__(self, driver)
        self.exitObj = Setting(self.driver)

    # 用户名输入框
    def input_user(self, text=''):
        self.input_element(self.loc_user, text)

    # 密码输入框
    def input_psw(self, text=''):
        self.input_element(self.loc_password, text)

    # 登录按钮
    def login_btn(self):
        self.click_element(self.loc_lgbtn)


    # 权限处理
    def permission_choose(self):
        # 权限弹框处理
        while True:
            if '允许' in self.driver.page_source:
                self.driver.switch_to.alert.accept()
            else:
                break

    # 登录功能
    def login(self, username, password):

        # 输入用户名
        self.input_element(self.loc_user, username)
        # 输入密码
        self.input_element(self.loc_password, password)
        # 点击确认按钮
        self.click_element(self.loc_lgbtn)

    # 登录后
    def login_after(self):
        self.click_element(self.loc_after)

    # 登录注销
    def logout(self):
        self.login_after()
        self.exitObj.exit()

    # 清空输入框
    def clear_input(self):
        self.click_element(self.loc_user)
        self.click_element(self.loc_password)

    # 获取错误结果
    def get_error_message_verify(self):
        msg = self.find_element(self.loc_error).text
        return msg

    # 获取成功消息
    def get_success_message_verify(self):
        msg = self.find_element(self.loc_success).text
        return msg


if __name__ == '__main__':
    driver = init_driver()
    logObj = Login(driver)
    logObj.permission_choose()
    logObj.login("admin", "123")
    logObj.logout()
    driver.quit()