from selenium.webdriver.support.ui import WebDriverWait

class Base:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, loc, timeout=10, poll=0.5):
        """
        选择单个元素
        :param loc: 元组对象 定位类型+定位值 例如：("id", "com.krhd.qls.zhxj:id/et_login_username")
        :param timeout: 等待时间
        :param poll: 等待间隔
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_element(*loc))

    def find_elements(self, loc, timeout=10, poll=0.5):
        """
        选择多个元素
        :param loc: 元组对象 定位类型+定位值 例如：("id", "com.krhd.qls.zhxj:id/et_login_username")
        :param timeout: 等待时间
        :param poll: 等待间隔
        :return:
        """
        return WebDriverWait(self.driver, timeout, poll).until(lambda x: x.find_elements(*loc))

    def click_element(self, loc):
        # 点击元素函数
        self.find_element(loc).click()

    def input_element(self, loc, text):
        # 输入元素函数
        self.find_element(loc).send_keys(text)

    def clear_element(self, loc):
        # 输入元素函数
        self.find_element(loc).clear()