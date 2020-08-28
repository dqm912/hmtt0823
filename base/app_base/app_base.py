# 对象库层 基类 把定位元素的方法定义在基类中
from utils import DriverUtils


# 1定义对象库层基类
class BasePage:
    def __init__(self):
        self.driver = DriverUtils.get_app_driver()

    # 2公用的元素定位方法
    def find_elt(self, location):
        return self.driver.find_element(*location)


# 1定义操作层的基类
class BaseHandle:
    # 2 定义公用的元素输入方法
    def input_text(self, element, text):
        element.clear()
        element.send_keys(text)
