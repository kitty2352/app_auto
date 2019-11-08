from Common.config import init_driver
from Pages.Page import Page_Obj
import pytest
from Common.Read_Data import Read_Data
import allure

# 通过数据驱动方式实现测试用例
def test_data():
    data_list = []
    data = Read_Data("data.yml").return_data().get("loginData")
    for i in data.keys():
        data_list.append((i, data.get(i).get("username"), data.get(i).get("password")))
    return data_list

@allure.severity(allure.severity_level.NORMAL)
class Test_login():

    def setup(self):
        self.driver = init_driver('com.krhd.qls.zhxj', 'com.krhd.qls.zhxj.ui.login.LoginActivity')
        self.loginObj = Page_Obj(self.driver).Login_Page()


    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize("test_num,user,pwd", test_data())
    def test01(self, test_num, user, pwd):
        self.loginObj.permission_choose()
        self.loginObj.login(user, pwd)
        self.driver.get_screenshot_as_file("../screen/%s.png" % test_num)

if __name__ == "__main__":
    pytest.main(['--html=../Report/report.html', 'test_login1.py'])
