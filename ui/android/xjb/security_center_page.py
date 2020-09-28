# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from ui.android.xjb.setting_change_phone_page import SettingChangePhonePage
from ui.android.xjb.setting_login_password_page import SettingLoginPasswordPage
from ui.android.xjb.setting_trade_password_page import SettingTradePasswordPage
from .locator import GENERIC_LOADING_ICON

IDENTIFIER = "//android.widget.TextView[@text='安全中心']"
LOGIN_PASSWORD_BUTTON = "//android.widget.TextView[@text='登录密码']"
TRADE_PASSWORD_BUTTON = "//android.widget.TextView[@text='交易密码']"
CHANGE_PHONE_BUTTON = "//android.widget.TextView[@text='修改绑定手机']"


class SecurityCenterPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON

        super(SecurityCenterPage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def go_to_setting_login_password_page(self):
        self.perform_actions(LOGIN_PASSWORD_BUTTON)
        page = SettingLoginPasswordPage(self.web_driver)

        return page

    @wait_for_page_to_load
    def go_to_setting_trade_password_page(self):
        self.perform_actions(TRADE_PASSWORD_BUTTON)
        page = SettingTradePasswordPage(self.web_driver)

        return page

    @wait_for_page_to_load
    def go_to_setting_change_phone_page(self):
        self.perform_actions(CHANGE_PHONE_BUTTON)
        page = SettingChangePhonePage(self.web_driver)

        return page
