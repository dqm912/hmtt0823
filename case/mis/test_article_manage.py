import logging
from time import sleep

import pytest
import config
from page.mis.mis_audit_page import MisAuditProxy
from page.mis.mis_home_page import MisHomePage
from page.mis.mis_login_page import MisLoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=103)
class TestArticleManage:
    def setup_class(self):
        self.driver = DriverUtils.get_mis_driver()
        # 创建审核页面对象
        self.audit_proxy = MisAuditProxy()
        # 创建登录页面对象
        self.login_proxy = MisLoginProxy()
        # 创建首页 对象
        self.home_page = MisHomePage()

    # def setup_method(self):
    #     sleep(2)
    #     DriverUtils.get_mis_driver().get('http://ttmis.research.itcast.cn/#/home')

    # 登录
    # @pytest.mark.run(order=1)
    # def test_login_proxy(self):
    #     self.login_proxy.test_mis_login('testid', 'testpwd123')

    # @pytest.mark.run(order=2)
    # 测试审核通过的测试用例
    def test_audit_article_pass(self):
        article_title = config.PUB_ARTICLE_TITLE
        logging.info(article_title)
        self.home_page.to_audit_page()
        self.audit_proxy.test_audit_pass(article_title)
        assert is_element_exist(DriverUtils.get_mis_driver(), '驳回')

    # 测试驳回文章的测试用例
    # @pytest.mark.run(order=3)
    # def test_audit_article_reject(self):
    #     self.home_page.to_audit_page()
    #     self.audit_proxy.test_audit_reject()
    #     # 断言
    #     assert is_element_exist(DriverUtils.get_mis_driver(), '查看')

    def teardown_class(self):
        DriverUtils.quit_mis_driver()
