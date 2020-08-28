import allure
from selenium.webdriver.common.by import By

from base.mp_base.mp_base import BasePage, BaseHandle


# 对象库层（自媒体）
from utils import get_allure_picture, DriverUtils


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        self.verify = (By.CSS_SELECTOR, '[placeholder="验证码"]')
        self.login_btn = (By.CSS_SELECTOR, '.el-button--primary')

    def find_username(self):
        return self.find_elt(self.username)

    def find_verify(self):
        return self.find_elt(self.verify)

    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class LoginHandle(BaseHandle):

    def __init__(self):
        self.login_page = LoginPage()

    @allure.step(title='用户名输入')
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    @allure.step(title='验证码输入')
    def input_verity(self, verity):
        self.input_text(self.login_page.find_verify(), verity)

    @allure.step(title='登录按钮点击')
    def click_login_but(self):
        self.login_page.find_login_btn().click()


# 业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务方法
    def test_mp_login(self, username, verity):
        # 输入用户名
        self.login_handle.input_username(username)
        # 输入验证码
        self.login_handle.input_verity(verity)
        #截图
        get_allure_picture(DriverUtils.get_mp_driver())
        # 点击登录按钮
        self.login_handle.click_login_but()
