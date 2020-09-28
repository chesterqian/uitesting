# coding: utf-8
from common.page_object import PageObject
from .locator import GENERIC_LOADING_ICON
from .binding_card_page import BindingCardPage

IDENTIFIER = "//android.widget.TextView[@text='银行卡管理']"
CARD_MANAGEMENT_BUTTON = "//android.widget.TextView[@text='绑定银行卡']"
SWIPE_STOP_CONDITION = "//android.widget.TextView[@text='绑定银行卡']"
SWIPE_SART_CONDITION = "//android.widget.TextView[@text='银行卡管理']"

BINDING_CARD = "//android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/bankLogo']"
UNBUNDLING_LIST = "//android.widget.ImageButton[@resource-id='com.shhxzq.xjb:id/ibtn_actionbar_right']"
DELETE = "//android.widget.TextView[@text='删除']"
CHECK_ELEMENT_EXISTS = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/trade_pop_info']"
SUCCESS_BUTTON = "//android.widget.Button[@text='确认']"


class BankCardManagementPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(BankCardManagementPage, self).__init__(driver)

        self.check_destination_page(self)

    def go_to_binding_card_page(self):
        self.handle_swipe_operation(SWIPE_SART_CONDITION, SWIPE_STOP_CONDITION, 1)

        self.perform_actions(CARD_MANAGEMENT_BUTTON)

        phone_number = self.web_driver.login_cookie['phone_number']
        page = BindingCardPage(self.web_driver, phone_number, self.__class__.__name__)

        return page

    def unbundling_card(self, keycodes):
        args = [
            BINDING_CARD, UNBUNDLING_LIST, DELETE,
        ]
        self.perform_actions(*args)
        self.element_exists(CHECK_ELEMENT_EXISTS)
        for i in keycodes:
            self.web_driver.press_keycode(i)
        self.perform_actions(SUCCESS_BUTTON)
