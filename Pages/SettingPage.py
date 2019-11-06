import time
from Common.base import Base
from Common.config import init_driver
# from Pages.LoginPage import Login
import Pages
# 设置页面
class Setting(Base):

    # 退出登录
    loc_logout = ('id', 'com.krhd.qls.zhxj:id/btn_logout')

    def __init__(self, driver):
        self.driver = driver

    # 进入设置
    def into_settting(self):
        # 点击个人中心
        self.driver.tap([(56, 147), (120, 211)], 100)
        self.click_element(Pages.loc_setting)

    # 退出登录操作
    def logout(self):
        self.click_element(self.loc_logout)

    # 退出登录
    def exit(self):
        self.into_settting()
        self.logout()


if __name__ == '__main__':
    driver = init_driver()
    logObj = Login(driver)
    logObj.permission_choose()
    logObj.login("admin", "123")
    logObj.login_after()
    exitObj = exit_login(driver)
    exitObj.exit()
    driver.quit()