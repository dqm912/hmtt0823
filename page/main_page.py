from selenium.webdriver.common.by import By

from base.mp_base import BasePage, BaseHandle


class MainPage(BasePage):
    def __init__(self):
        super().__init__()
        self.system = (By.LINK_TEXT, '系统')
        self.shop = (By.LINK_TEXT, '商城')
        self.plug_in = (By.LINK_TEXT, '插件')
        # 商品属性
        self.goods_attribute = (By.XPATH, '//*[@data-param="goodsAttributeList|Goods"]')
        # 添加属性
        self.add_attribute = (By.CSS_SELECTOR, '.fa-plus')
        # 批量删除
        self.del_attribute = (By.XPATH, '//*[@title="批量删除"]')

    def find_system(self):
        return self.find_elt(self.system)

    def find_shop(self):
        return self.find_elt(self.shop)

    def find_plug_in(self):
        return self.find_elt(self.plug_in)

    def find_goods_attribute(self):
        return self.find_elt(self.goods_attribute)

    def find_add_attribute(self):
        return self.find_elt(self.add_attribute)


class MainHandle(BaseHandle):
    def __init__(self):
        self.main_page = MainPage()

    def click_system(self):
        self.main_page.find_system().click()

    def click_shop(self):
        self.main_page.find_shop().click()

    def click_goods_attribute(self):
        self.main_page.find_goods_attribute().click()

    def click_plug_in(self):
        self.main_page.find_plug_in().click()
    #点击添加属性
    def click_add_attribute(self):
        self.main_page.find_add_attribute().click()



class MainProxy():
    pass
