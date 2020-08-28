# 导包
# 定义测试类
from page.app.index_page import IndexProxy
from utils import DriverUtils, is_element_exist_by_attribute


class TestQueryArticle:
    # 定义初始化方法
    def setup_class(self):
        self.driver = DriverUtils.get_app_driver()
        self.index_proxy = IndexProxy()

    # 定义测试方法
    def test_query_article(self):
        channel_name = '人工智能'
        self.index_proxy.test_qari_by_channel(channel_name)
        assert is_element_exist_by_attribute(self.driver, "text", '点赞')

    # 定义销毁方法
    def teardowm_class(self):
        DriverUtils.quit_app_driver()
