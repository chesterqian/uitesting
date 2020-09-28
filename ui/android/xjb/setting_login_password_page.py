# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from database import SgwDataBaseOperator
from ui.android.xjb.context import PasswordHandle
from .locator import GENERIC_LOADING_ICON


IDENTIFIER = "//android.widget.TextView[@text='登录密码']"
FIND_LOGIN_PASSWORD = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_account_find_pwd']"
CHANGE_LOGIN_PASSWORD = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_account_modify_pwd']"


class SettingLoginPasswordPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON

        super(SettingLoginPasswordPage, self).__init__(driver)

        self.check_destination_page(self)
        self._db_operator = SgwDataBaseOperator('supergw_uat')

    @wait_for_page_to_load
    def change_login_password(self, login_password, new_login_password):
        self.perform_actions(CHANGE_LOGIN_PASSWORD)
        ph = PasswordHandle()
        ph.all_handle(self, login_password=login_password, new_login_password=new_login_password)

    @wait_for_page_to_load
    def find_login_password(self, is_bind_card, phone_number, login_password, user_name, cert_no):
        self.perform_actions(FIND_LOGIN_PASSWORD)
        ph = PasswordHandle()
        ph.all_handle(self, is_bind_card=is_bind_card, phone_number=phone_number, login_password=login_password,
                      user_name=user_name, cert_no=cert_no)
