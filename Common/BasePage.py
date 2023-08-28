import os
import time
import datetime
import logging
from selenium.common import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from common.constant import IMG_DIR

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='D:\\POselenium\\my_log.log',level=logging.DEBUG, format='%(levelname)s: %(message)s')
IMG_DIR=""
class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, img_desc, timeout=20, frequency=0.5):
        """等待元素可见"""
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.visibility_of_element_located(loc))
            logger.info("等待:{} - 元素{}可见成功。".format(img_desc, loc))
            #print("等待:{} - 元素{}可见成功。".format(img_desc, loc))
            return True
        except TimeoutException:
            logger.exception("等待:{} - 元素{}可见失败！".format(img_desc, loc))
            self.save_img(img_desc)
            #raise
            return False

    def get_element(self, loc, img_desc):
        """查找元素"""
        try:
            ele = self.driver.find_element(*loc)
        except:
            logger.exception("查找:{} - 元素{}失败！".format(img_desc, loc))
            self.save_img(img_desc)
            raise
        else:
            logger.info("查找:{} - 元素{}成功".format(img_desc, loc))
            return ele

    def click_element(self, loc, img_desc, timeout=20, frequency=0.5):
        """点击元素"""
        #self.wait_ele_visible(loc, img_desc, timeout, frequency)
        if not self.wait_ele_visible(loc, img_desc, timeout, frequency):
            logger.warning("点击:{} - 元素{}超时，点击操作未执行。".format(img_desc, loc))
            return False
        ele = self.get_element(loc, img_desc)
        try:
            ele.click()
            logger.info("点击:{} - 元素{}成功".format(img_desc, loc))
        except:
            logger.exception("点击:{} - 元素{}失败！".format(img_desc, loc))
            self.save_img(img_desc)
            raise

    def input_text(self, loc, value, img_desc, timeout=20, frequency=0.5):
        """在元素中输入文本"""
        #self.wait_ele_visible(loc, img_desc, timeout, frequency)
        if not self.wait_ele_visible(loc, img_desc, timeout, frequency):
            logger.warning("点击:{} - 元素{}超时，点击操作未执行。".format(img_desc, loc))
            return False
        ele = self.get_element(loc, img_desc)
        try:
            ele.send_keys(value)
            logger.info("输入：在{} - 元素{}输入文本值({})成功".format(img_desc, loc, value))
        except:
            logger.exception("输入：在{} - 元素{}输入文本值({})失败！".format(img_desc, loc, value))
            self.save_img(img_desc)
            raise

    def save_img(self, img_description):
        """保存异常截图"""
        now = time.strftime("%Y-%m-%d %H-%M-%S ", time.localtime())
        img_path = os.path.join(IMG_DIR, now + img_description + '.png')
        try:
            self.driver.save_screenshot(img_path)
        except:
            logger.exception("异常截图失败！")
        else:
            logger.info("异常截图成功，截图存放在{}".format(img_path))