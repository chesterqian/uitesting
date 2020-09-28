# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from database import sgw_database_operator
from ui.android.xjb.context import PasswordHandle
from ui.android.xjb.xjb_page_decorator import return_page_afterwards, cancel_prompt_afterwards, \
    cancel_gasture_afterwards
from .locator import GENERIC_LOADING_ICON
from .register_page import RegisterPage


IDENTIFIER = "//android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/img_login_header_bg']"
USER_NAME = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/etAccount']"
PASSWORD = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/etPwd']"
LOGIN_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/login_bt']"
REGISTER_ACCOUNT = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/login_register_bt']"
FORGET_LOGIN_PASSWORD = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/login_forgot_tv']"


class LoginPage(PageObject):
    activity_map_return_page = {'login': 'HomePage'}

    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(LoginPage, self).__init__(driver)

        self.check_destination_page(self)
        self._db_operator = sgw_database_operator
        self.login_cookie = {'login_cookie': ''}

    @return_page_afterwards
    @cancel_prompt_afterwards
    @cancel_gasture_afterwards
    def login(self, user_name, password):
        self.perform_actions(USER_NAME, user_name, PASSWORD, password, LOGIN_BUTTON)
        self.login_cookie.update({'phone_number': user_name})
        setattr(self.web_driver, 'login_cookie', self.login_cookie)

    @wait_for_page_to_load
    def go_to_register_page(self):
        self.perform_actions(REGISTER_ACCOUNT)
        page = RegisterPage(self.web_driver)
        return page

    @wait_for_page_to_load
    def find_login_password(self, is_bind_card, phone_number, login_password, user_name, cert_no):
        self.perform_actions(FORGET_LOGIN_PASSWORD)
        ph = PasswordHandle()
        ph.all_handle(self, is_bind_card=is_bind_card, phone_number=phone_number, login_password=login_password,
                      user_name=user_name, cert_no=cert_no)