"""后台登录管理系统的登录页面"""

from selenium.webdriver.common.by import By
from utils import DriverUtils
from base.mis_base.mis_base import BasePage, BaseHandle


# 对象库层
class MisLoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = (By.NAME, "username")
        # 密码输入框
        self.password = (By.NAME, "password")
        # 登录按钮
        self.login_btn = (By.ID, "inp1")

    # 找用户名输入框
    def find_username(self):
        return self.find_elt(self.username)

    # 找密码输入框
    def find_password(self):
        return self.find_elt(self.password)

    # 找登录按钮
    def find_login_btn(self):
        return self.find_elt(self.login_btn)


# 操作层
class MisLoginHandle(BaseHandle):
    def __init__(self):
        self.mis_login_page = MisLoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.mis_login_page.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.mis_login_page.find_password(), password)

    # 点击登录
    def click_login_btn(self):
        # 删除登录按钮对象disable属性
        js_str = 'document.getElementById("inp1").removeAttribute("disabled")'
        # 执行js语句
        DriverUtils.get_mis_driver().execute_script(js_str)
        # 点击登录按钮
        self.mis_login_page.find_login_btn().click()


# 业务层
class MisLoginProxy:
    def __init__(self):
        self.mis_login_handle = MisLoginHandle()

    # 登录方法
    def test_mis_login(self, username, password):
        # 输入用户名
        self.mis_login_handle.input_username(username)
        # 输入密码
        self.mis_login_handle.input_password(password)
        # 点击登录按钮
        self.mis_login_handle.click_login_btn()
