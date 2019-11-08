from Common.config import init_driver
from Pages.Page import Page_Obj
import pytest
import allure


@allure.severity(allure.severity_level.NORMAL)
class Test_login():

    def setup_class(self):
        self.driver = init_driver('com.krhd.qls.zhxj', 'com.krhd.qls.zhxj.ui.login.LoginActivity')
        self.loginObj = Page_Obj(self.driver).Login_Page()

    def teardown(self):
        self.loginObj.clear_input()

    def teardown_class(self):
        self.driver.quit()

    @allure.step(title="输入正确的用户名和密码")
    def test01(self):
        allure.attach("登录用例1", "输入正确的用户名和密码")
        self.loginObj.permission_choose()
        self.loginObj.login("admin", "123")
        assert '立即设置' in self.loginObj.get_success_message_verify(), '成功'
        self.loginObj.logout()

    @allure.step(title="输入正确的用户名和错误的密码")
    def test02(self):
        allure.attach("登录用例2", "输入正确的用户名和错误的密码")
        self.loginObj.login("admin", "1234")
        assert '密码错误' == self.loginObj.get_error_message_verify(), '成功'

    @allure.step(title="输入错误的用户名和错误的密码")
    def test03(self):
        self.loginObj.login("hahaha", "1234")
        assert '用户名不存在' == self.loginObj.get_error_message_verify(), '成功'

    @allure.step(title="输入用户名为空")
    def test04(self):
        self.loginObj.login("", "1234")
        assert '不可为空' in self.loginObj.get_error_message_verify(), '成功'

    @allure.step(title="输入密码为空")
    def test05(self):
        self.loginObj.login("admin", "")
        assert '不可为空' in self.loginObj.get_error_message_verify(), '成功'


if __name__ == "__main__":
    pytest.main(['--html=../Report/report.html', 'test_login.py'])
