import unittest
import pytest
import ddt
import logging
from selenium import webdriver
from Pages.LoginPage import LoginPage
from BusinessLayer.testdatas import common_datas as com_d
from BusinessLayer.testdatas import login_data as lo_d



@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger()
        self.logger.info("-------用例前置工作：打开浏览器--------")
        #print("-------用例前置工作：打开浏览器--------")
        self.driver = webdriver.Chrome()
        #self.driver.get(com_d.baidu_url)
        self.driver.get(com_d["baidu_url"])
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()
        self.logger.info("-------用例后置工作：关闭浏览器--------")
        #print("-------用例后置工作：关闭浏览器--------")

    @pytest.mark.smoke
    def test_login_invalid(self):
        # 用例:登录页的登录功能
        # 步骤
        LoginPage(self.driver).login(lo_d["invalid_data"]['user'], lo_d["invalid_data"]['pwd'])
        # 断言.....