from selenium.webdriver.common.by import By

from base.mp_base.mp_base import BasePage, BaseHandle


# mp自媒体登录页面类
class LoginPage(BasePage, BaseHandle):
    def __init__(self):
        super().__init__()
        # 账号输入框
        self.username = (By.CSS_SELECTOR, '[placeholder="请输入手机号"]')
        # 验证码
        self.verify = (By.CSS_SELECTOR, '[placeholder="验证码"]')
        # 登录按钮
        self.login_btn = (By.CSS_SELECTOR, '.el-button--primary')

    # 登录的方法
    def test_login(self, username, verity):
        self.input_text(self.find_elt(self.username), username)
        self.input_text(self.find_elt(self.verify), verity)
        self.find_elt(self.login_btn).click()
    