import time
import pytest

import config
from page.mp.homepage import HomeProxy, HomeHandle
from page.mp.publish_artical_page import PubAriProxy
from utils import DriverUtils, is_element_exist, build_data, BASE_DIR


# 定义测试类
@pytest.mark.run(order=3)
class TestPubArticle:

    def setup_class(self):
        # 打开浏览器
        self.driver = DriverUtils.get_mp_driver()
        # 创建首页业务层对象
        self.home_proxy = HomeProxy()
        # 创建发布文章业务层对象
        self.pub_ari_proxy = PubAriProxy()

    # def setup_method(self):
    #     self.driver.get("")

    def teardown_class(self):
        # 关闭浏览器
        DriverUtils.quit_mp_driver()

    # 定义测试方法
    @pytest.mark.parametrize(('article_title', 'article_context', 'article_channel', 'expect'),
                             build_data(BASE_DIR + '/data/mp/test_pub_ari_data.json'))
    def test_pub_article(self, article_title, article_context, article_channel, expect):
        # 组织测试数据
        config.PUB_ARTICLE_TITLE = article_title.format(time.strftime("%H%M%S"))
        # 执行测试步骤
        self.home_proxy.to_pub_ari_page()
        self.pub_ari_proxy.test_pub_article(config.PUB_ARTICLE_TITLE, article_context, article_channel)
        # 断言
        assert is_element_exist(self.driver, expect)
        HomeHandle().click_context_tab()
        time.sleep(1)

