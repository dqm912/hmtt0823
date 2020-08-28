# 登录页面
# 对象库层
from selenium.webdriver.common.by import By

from base.mp_base import BasePage, BaseHandle


class LoginPage(BasePage):

    def __init__(self):
        # 重写父类
        super().__init__()
        # self.driver = DriverUtils.get_driver() 子类不需要 继承父类
        self.username = (By.NAME, 'username')
        self.password = (By.NAME, 'password')
        self.verify = (By.NAME, 'vertify')
        self.login_btn = (By.NAME, 'submit')

    # 用户名输入框
    def find_username(self):
        # return self.driver.find_element(*self.username)  # *拆分符
        return self.find_elt(self.username)

    # 密码输入框
    def find_password(self):
        return self.find_elt(self.password)

    # 验证码输入框
    def find_verify(self):
        return self.find_elt(self.verify)

    # 登录按钮
    def login_button(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.__login_page = LoginPage()

    # 用户名输入框
    def input_user(self, username):
        # self.__login_page.find_username().clear()
        # self.__login_page.find_username().send_keys(username)
        self.input_text(self.__login_page.find_username(), username)

    # 密码输入框
    def input_password(self, password):
        self.input_text(self.__login_page.find_password(), password)

    # 验证码输入框
    def input_verify(self, verify):
        self.input_text(self.__login_page.find_verify(), verify)

    # 确认按钮
    def click_login_button(self):
        self.__login_page.login_button().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.__login_handle = LoginHandle()

    # 登陆业务的方法
    def test_login(self, username, password, verify_code):
        # 输入用户名
        self.__login_handle.input_user(username)
        # 输入密码
        self.__login_handle.input_password(password)
        # 输入验证码
        self.__login_handle.input_verify(verify_code)
        # 点击登陆
        self.__login_handle.click_login_button()
