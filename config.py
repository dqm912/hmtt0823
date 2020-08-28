# 1.导包
import logging.handlers
from utils import BASE_DIR


# 日志基础配置方法
def basic_log_config():
    # 2.创建日志器对象
    logger = logging.getLogger()
    # 设置日志的打印级别
    logger.setLevel(level=logging.INFO)
    # 3.创建处理器
    # 3.1 输出到控制台
    ls = logging.StreamHandler()
    # 3.2每日生成一个日志文件 最多备份两天（最近两个备份文件 自动删除早期日志）
    lht = logging.handlers.TimedRotatingFileHandler(BASE_DIR + '/log/potest.log', when='midnight', interval=1,
                                                    backupCount=2,
                                                    encoding='utf-8')
    # 4.创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 5.给树立起设置格式化器
    ls.setFormatter(formatter)
    lht.setFormatter(formatter)
    # 6.给日志添加处理器
    logger.addHandler(ls)
    logger.addHandler(lht)


# 发布文章标题
PUB_ARTICLE_TITLE = None
