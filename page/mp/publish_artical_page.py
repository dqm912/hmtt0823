from selenium.webdriver.common.by import By
from base.mp_base.mp_base import BasePage, BaseHandle
from utils import DriverUtils, not_select_check, get_allure_picture


# 对象库层
class PubAriPage(BasePage):
    def __init__(self):
        super().__init__()
        # 标题
        self.ari_title = (By.CSS_SELECTOR, '[placeholder="文章名称"]')
        # iframe
        self.ari_iframe = (By.CSS_SELECTOR, '#publishTinymce_ifr')
        # 内容
        self.ari_context = (By.CSS_SELECTOR, 'body')
        # 封面
        self.ari_cover = (By.XPATH, '//*[text()="自动"]')
        # 频道
        self.channel = (By.CSS_SELECTOR, '[placeholder="请选择"]')
        # 发表
        self.pub_btn = (By.XPATH, '//*[text()="发表"]')

    # 找标题
    def find_ari_title(self):
        return self.find_elt(self.ari_title)

    # 找iframe
    def find_ari_iframe(self):
        return self.find_elt(self.ari_iframe)

    # 找内容
    def find_ari_context(self):
        return self.find_elt(self.ari_context)

    # 找封面
    def find_ari_cover(self):
        return self.find_elt(self.ari_cover)

    # 找频道选择框
    def find_channel(self):
        return self.find_elt(self.channel)

    # 找发表按钮
    def find_pub_btn(self):
        return self.find_elt(self.pub_btn)


# 操作层
class PubAriHandle(BaseHandle):
    def __init__(self):
        self.pub_ari_page = PubAriPage()

    # 文章标题的输入
    def input_ari_title(self, title):
        self.pub_ari_page.find_ari_title().send_keys(title)

    # 文章内容的输入
    def input_ari_content(self, context):
        # iframe切换
        DriverUtils.get_mp_driver().switch_to.frame(self.pub_ari_page.find_ari_iframe())
        # 输入文章内容
        self.pub_ari_page.find_ari_context().send_keys(context)
        # 切换回默认页面
        DriverUtils.get_mp_driver().switch_to.default_content()

    # 选择封面
    def check_ari_cover(self):
        self.pub_ari_page.find_ari_cover().click()

    # 选择频道
    def check_ari_channel(self, channel_name):
        # # 点击频道框
        # self.pub_ari_page.find_channel().click()
        # # # 发表点击
        # # self.pub_ari_page.find_channel_option().click()
        # # 获取所有选项的列表
        # channel_option = DriverUtils.get_mp_driver().find_elements_by_css_selector(
        #     ".el-select-dropdown__item span")
        # is_suc = False
        # # 遍历所获取的频道名称
        # for option in channel_option:
        #     # 判断当前遍历的元素文本信息是否等于所想要的频道名称
        #     if option.text == channel_name:
        #         # 如果相等则点击 跳出 吧默认标识改成True
        #         option.click()
        #         is_suc = True
        #         break
        #     # 不相等则 鼠标悬浮到当前遍历的元素对象上并按下向下的按钮
        #     else:
        #         # 创建鼠标对象
        #         action = ActionChains(DriverUtils.get_mp_driver()
        #         action.move_to_element(option).send_keys(Keys.DOWN).perform()
        # # 判断标识是否为False，则掏出没找到对应频道的选项
        # if is_suc is False:
        #     NoSuchElementException(f"找不到名称为{channel_name}的频道")
        channel_option = DriverUtils.get_mp_driver().find_elements_by_css_selector(
            ".el-select-dropdown__item span")
        not_select_check(DriverUtils.get_mp_driver(), self.pub_ari_page.find_channel(), channel_option, channel_name)

    # 点击发表按钮
    def click_pub_btn(self):
        self.pub_ari_page.find_pub_btn().click()


# 业务层
class PubAriProxy:
    def __init__(self):
        self.pub_ari_page = PubAriPage()
        self.pub_ari_handle = PubAriHandle()

    # 发布文章业务的方法
    def test_pub_article(self, title, context, channel_name):
        # 输入标题内容
        self.pub_ari_handle.input_ari_title(title)
        # 输入内容
        self.pub_ari_handle.input_ari_content(context)
        # 选择封面
        self.pub_ari_handle.check_ari_cover()
        # 选择频道
        self.pub_ari_handle.check_ari_channel(channel_name)
        # 截图
        get_allure_picture(DriverUtils.get_mp_driver())
        # 点击发表按钮
        self.pub_ari_handle.click_pub_btn()
