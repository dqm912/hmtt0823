"""
后台管理系统--首页
"""
from selenium.webdriver.common.by import By

from base.mis_base.mis_base import BasePage, BaseHandle


# 定义页面对象类
class MisHomePage(BasePage, BaseHandle):
    # 定义实例属性
    def __init__(self):
        super().__init__()
        # 信息管理菜单栏
        self.info_manage_tab = (By.CSS_SELECTOR, '.fa-shopping-basket')
        # 内容审核菜单栏
        self.context_manage_tab = (By.XPATH, '//*[text()="内容审核"]')

    # 跳转内容审核管理菜单
    def to_audit_page(self):
        # 点击信息管理
        self.find_elt(self.info_manage_tab).click()
        # 点击内容审核
        self.find_elt(self.context_manage_tab).click()
