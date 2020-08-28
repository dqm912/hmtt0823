import logging
import os
import json

import allure
import appium.webdriver
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# 绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 浏览器驱动对象工具
class DriverUtils:
    # 自媒体驱动对象
    __mp_driver = None
    # 后台管理系统
    __mis_driver = None
    # app
    __app_driver = None
    #
    __mp_key = True
    __mis_key = True

    # 修改mp自媒体关闭浏览器驱动的开关方法
    @classmethod
    def change_mp_key(cls, key):
        cls.__mp_key = key

    # 修改mis自媒体关闭浏览器驱动的开关方法
    @classmethod
    def change_mis_key(cls, key):
        cls.__mis_key = key

    # 自媒体 浏览器驱动方法
    @classmethod
    def get_mp_driver(cls):
        if cls.__mp_driver is None:
            cls.__mp_driver = webdriver.Chrome()
            cls.__mp_driver.get('http://ttmp.research.itcast.cn/')
            cls.__mp_driver.maximize_window()
            cls.__mp_driver.implicitly_wait(10)
        return cls.__mp_driver

    @classmethod
    def quit_mp_driver(cls):
        if cls.__mp_driver is not None and cls.__mp_key:
            sleep(2)
            cls.__mp_driver.quit()
            cls.__mp_driver = None

    # 后台管理系统浏览器驱动方法
    @classmethod
    def get_mis_driver(cls):
        if cls.__mis_driver is None:
            cls.__mis_driver = webdriver.Chrome()
            cls.__mis_driver.get('http://ttmis.research.itcast.cn/')
            cls.__mis_driver.maximize_window()
            cls.__mis_driver.implicitly_wait(10)
        return cls.__mis_driver

    @classmethod
    def quit_mis_driver(cls):
        if cls.__mis_driver is not None and cls.__mis_key:
            sleep(2)
            cls.__mis_driver.quit()
            cls.__mis_driver = None

    # app系统获取驱动对象方法
    @classmethod
    def get_app_driver(cls):
        if cls.__app_driver is None:
            desired_caps = dict()
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '5.1'
            desired_caps['deviceName'] = 'emulator-5554'
            desired_caps['appPackage'] = 'com.itcast.toutiaoApp'
            desired_caps['appActivity'] = '.MainActivity'
            desired_caps['noReset'] = True  #
            cls.__app_driver = appium.webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            cls.__app_driver.implicitly_wait(5)
        return cls.__app_driver

    @classmethod
    def quit_app_driver(cls):
        if cls.__app_driver:
            sleep(2)
            cls.__app_driver.quit()
            cls.__app_driver = None


# 列表选择-文本
def select_choose(element, text):
    select = Select(element)
    return select.select_by_visible_text(text)


# 获取弹出框信息
def get_tck_tip(driver, element, find=By.XPATH):
    msg = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element(find, element)).text
    return msg


# 获取弹出框信息
def get_all_tck_tip(element, find=By.XPATH):
    msg = WebDriverWait(DriverUtils.get_driver(), 10, 0.5).until(lambda x: x.find_element(find, element)).text
    return msg


# 构建测试数据
def build_data(file):
    data = list()
    with open(file, encoding='utf-8') as f:
        json_data = json.load(f)
        for i in json_data.values():
            data.append(list(i.values()))
        return data


# 根据文本判断元素是否存在
def is_element_exist(driver, text):
    # 定位元素的Xpath表达式
    str_xpath = f'//*[contains(text(),"{text}")]'
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        logging.error(NoSuchElementException(f'找不到文本为{text}的元素对象'))
        NoSuchElementException(f'找不到文本为{text}的元素对象')
        return False


# 根据元素属性判断元素是否存在
def is_element_exist_by_attribute(driver, attr_name, attr_value):
    # 定位元素的Xpath表达式
    str_xpath = f'//*[contains(@{attr_name},"{attr_value}")]'
    try:
        is_element = WebDriverWait(driver, 10, 0.5).until(lambda x: x.find_element_by_xpath(str_xpath))
        return is_element
    except Exception as e:
        logging.error(NoSuchElementException(f'找不到属性为{attr_name}且其值为{attr_value}的元素对象'))
        NoSuchElementException(f'找不到属性为{attr_name}且其值为{attr_value}的元素对象')
        return False


# 非select 选项框 元素选择
def not_select_check(driver, find_select_ele, find_option_eles, option_name):
    """
    driver 浏览器驱动对象
    find_select_ele 选择框元素对象
    find_option_eles 选择框选项元素s对象
    option_name 选项名称
    """
    # 点击频道框
    find_select_ele.click()
    # 获取所有选项的列表
    channel_option = find_option_eles
    is_suc = False
    # 遍历所获取的频道名称
    for option in channel_option:
        # 判断当前遍历的元素文本信息是否等于所想要的频道名称
        if option.text == option_name:
            # 如果相等则点击 跳出 吧默认标识改成True
            option.click()
            is_suc = True
            break
        # 不相等则 鼠标悬浮到当前遍历的元素对象上并按下向下的按钮
        else:
            # 创建鼠标对象
            action = ActionChains(driver)
            action.move_to_element(option).send_keys(Keys.DOWN).perform()
    # 判断标识是否为False，则掏出没找到对应频道的选项
    if is_suc is False:
        NoSuchElementException(f"找不到名称为{option_name}的频道")


# allure截图方法
def get_allure_picture(driver, filename="截图"):
    allure.attach(driver.get_screenshot_as_png(), filename, allure.attachment_type.PNG)
