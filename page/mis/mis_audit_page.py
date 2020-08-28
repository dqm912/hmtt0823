"""
后台管理系统 审核文章
"""
from time import sleep

from selenium.webdriver.common.by import By
from base.mis_base.mis_base import BasePage, BaseHandle
from utils import not_select_check, DriverUtils


# 对象库层
class MisAuditPage(BasePage):
    def __init__(self):
        super().__init__()
        # 文章标题搜索输入框
        self.ari_title = (By.CSS_SELECTOR, "[placeholder*='文章']")
        # 选择状态
        self.ari_channel = (By.CSS_SELECTOR, '[placeholder="请选择状态"]')
        # 选择结束时间
        self.time = (By.CSS_SELECTOR, '.el-input__inner')
        # 查询按钮
        self.query_btn = (By.CSS_SELECTOR, '.find')
        # 通过按钮
        self.pass_btn = (By.XPATH, "//*[text()='通过']")
        # 驳回按钮
        self.reject_btn = (By.XPATH, "//*[text()='驳回']")
        # 通过驳回确认按钮
        self.pass_reject_confirm_btn = (By.CSS_SELECTOR, ".el-button--primary")

    # find文章标题搜索输入框
    def find_ari_title_box(self):
        return self.find_elt(self.ari_title)

    # find选择状态
    def find_ari_channel(self):
        return self.find_elt(self.ari_channel)

    # find选择结束时间
    def find_time(self):
        return self.find_elt(self.time)

    # find查询按钮
    def find_query_btn(self):
        return self.find_elt(self.query_btn)

    # find通过按钮
    def find_pass_btn(self):
        return self.find_elt(self.pass_btn)

    # find驳回按钮
    def find_reject_btn(self):
        return self.find_elt(self.reject_btn)

    # find通过驳回确认按钮
    def find_pass_confirm_btn(self):
        return self.find_elt(self.pass_reject_confirm_btn)


# 操作层
class MisAuditHandle(BaseHandle):
    def __init__(self):
        self.mis_audit_page = MisAuditPage()

    # 输入查询标题
    def input_ari_title(self, title):
        self.input_text(self.mis_audit_page.find_ari_title_box(), title)

    # 选择频道
    def click_ari_channel(self, status):
        elements = DriverUtils.get_mis_driver().find_elements_by_css_selector('.el-select-dropdown__item')
        not_select_check(DriverUtils.get_mis_driver(), self.mis_audit_page.find_ari_channel(), elements, status)

    # 清除选择结束时间
    def clear_time(self):
        self.mis_audit_page.find_time().clear()

    # 点击查询按钮
    def click_query_btn(self):
        self.mis_audit_page.find_query_btn().click()

    # 点击通过按钮
    def click_pass_btn(self):
        self.mis_audit_page.find_pass_btn().click()

    # 点击驳回按钮
    def click_reject_btn(self):
        self.mis_audit_page.find_reject_btn().click()

    # 点击通过确认按钮
    def click_pass_reject_confirm_btn(self):
        self.mis_audit_page.find_pass_confirm_btn().click()


# 业务层
class MisAuditProxy:
    def __init__(self):
        self.__mis_audit_handle = MisAuditHandle()

    # 审核通过测试用例
    def test_audit_pass(self, title):
        # 输入搜索的文章名称
        self.__mis_audit_handle.input_ari_title(title)
        # 选择文章状态
        self.__mis_audit_handle.click_ari_channel('待审核')
        # 清除选择结束时间
        self.__mis_audit_handle.clear_time()
        # 点击查询按钮
        self.__mis_audit_handle.click_query_btn()
        sleep(2)
        # 点击通过按钮
        self.__mis_audit_handle.click_pass_btn()
        sleep(1)
        # 点击提示框确认按钮
        self.__mis_audit_handle.click_pass_reject_confirm_btn()
        sleep(1.5)
        # 选择文章状态
        self.__mis_audit_handle.click_ari_channel('审核通过')
        sleep(2)
        # 点击查询按钮
        self.__mis_audit_handle.click_query_btn()

    # 驳回测试用例
    def test_audit_reject(self):
        # 选择文章状态
        self.__mis_audit_handle.click_ari_channel('待审核')
        # 点击查询按钮
        self.__mis_audit_handle.click_query_btn()
        sleep(2)
        # 点击驳回按钮
        self.__mis_audit_handle.click_reject_btn()
        # 点击提示框确认按钮
        self.__mis_audit_handle.click_pass_reject_confirm_btn()
        sleep(2)
        # 切换审核失败界面
        self.__mis_audit_handle.click_ari_channel('审核失败')
        # 点击查询按钮
        self.__mis_audit_handle.click_query_btn()
        sleep(2)
