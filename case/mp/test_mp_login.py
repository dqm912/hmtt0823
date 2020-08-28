# 定义测试类
import pytest

from page.mp.login_page import LoginProxy
from utils import DriverUtils, is_element_exist


@pytest.mark.run(order=2)
class TestMpLogin:
    # 定义初始化方法
    def setup_class(self):
        # 获取驱动对象
        self.driver = DriverUtils.get_mp_driver()
        # 创建好所需要调用业务方法所在类的对象
        self.login_proxy = LoginProxy()

    # 定义测试方法
    def test_mp_login(self):
        # 定义测试数据
        username = '13387679730'
        verity = '246810'
        # 调用业务方法形成完整业务操作
        self.login_proxy.test_mp_login(username, verity)
        # 断言
        assert is_element_exist(self.driver, '江苏传智播客')

    # 定义销毁的方法
    def teardown_class(self):
        DriverUtils.quit_mp_driver()
