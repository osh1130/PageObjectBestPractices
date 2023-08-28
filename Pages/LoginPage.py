from selenium.webdriver.common.by import By
from Common.BasePage import BasePage
import logging
logger = logging.getLogger()
class LoginPage(BasePage):

    login_btn = (By.XPATH, '//div[@id="u1"]//a[@name="tj_login"]')  # 登录按钮
    username_login_btn = (By.ID, 'TANGRAM__PSP_11__footerULoginBtn')    # 用户名登录按钮
    user_input = (By.ID, 'TANGRAM__PSP_11__userName')  # 用户信息输入框
    pwd_input = (By.ID, 'TANGRAM__PSP_11__password')  # 密码输入框
    login_submit = (By.ID, 'TANGRAM__PSP_11__submit')   # 登录提交按钮

    def login(self, user, pwd):
        """
        百度用户名登录
        :param user: 手机/邮箱/用户名
        :param pwd: 密码
        :return:
        """
        self.click_element(self.login_btn, '百度-登录')
        self.click_element(self.username_login_btn, '百度登录-用户名登录')
        self.input_text(self.user_input, user, '用户名登录-手机/邮箱/用户名')
        self.input_text(self.pwd_input, pwd, '用户名登录-密码')
        self.click_element(self.login_submit, '用户名登录-登录')