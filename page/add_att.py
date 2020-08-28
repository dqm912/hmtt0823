from time import sleep

from selenium.webdriver.common.by import By

from base.mp_base import BasePage, BaseHandle

# 商品属性添加与管理
from page.main_page import MainHandle
from utils import select_choose, DriverUtils


class AddAttPage(BasePage):
    def __init__(self):
        super().__init__()
        # 返回
        self.back = (By.CSS_SELECTOR, '.fa-arrow-circle-o-left')
        # 属性名称
        self.name = (By.XPATH, '//*[@name="attr_name"]')
        # 所属商品模型列表
        self.goods_model = (By.ID, 'type_id')
        # 不需要检索
        # 关键字检索
        # 手工录入
        # 从下面的列表中选择（一行代表一个可选值）
        # 多行文本框
        # 确认提交
        self.button = (By.ID, 'submitBtn')
        # iframe
        self.frame = (By.ID, 'workspace')

    def find_back(self):
        return self.find_elt(self.back)

    def find_name(self):
        return self.find_elt(self.name)

    def find_goods_model(self):
        return self.find_elt(self.goods_model)

    def find_button(self):
        return self.find_elt(self.button)

    def find_frame(self):
        return self.find_elt(self.frame)


class AddAttHandle(BaseHandle):
    def __init__(self):
        self.main_page = AddAttPage()

    def input_name(self, name):
        self.input_text(self.main_page.find_name(), name)

    def chooss_goods_model(self, text):
        select_choose(self.main_page.find_goods_model(), text)

    def click_button(self):
        self.main_page.find_button().click()

    # def switch_frame(self):
    #     return DriverUtils.get_driver().switch_to.frame(self.main_page.find_frame())
    #
    # def switch_default(self):
    #     return DriverUtils.get_driver().switch_to.default_content()


class AddAttProxy():
    def __init__(self):
        self.add_att_handle = AddAttHandle()
        self.main_handle = MainHandle()
        self.main_page = AddAttPage()

    def add_att(self, name, text):
        DriverUtils.get_driver().switch_to.default_content()
        self.main_handle.click_shop()
        self.main_handle.click_goods_attribute()
        DriverUtils.get_driver().switch_to.frame(self.main_page.find_frame())
        self.main_handle.click_add_attribute()
        self.add_att_handle.input_name(name)
        self.add_att_handle.chooss_goods_model(text)
        self.add_att_handle.click_button()
        sleep(1)
