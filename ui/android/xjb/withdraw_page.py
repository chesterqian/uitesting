from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from .locator import GENERIC_LOADING_ICON

IDENTIFIER = "//android.widget.ImageView[@index='0']"
WITHDRAW_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_home_enchashment']"
REGULAR_WITHDRAW_RADIO = "//android.widget.RadioButton[@resource-id='com.shhxzq.xjb:id/rbtn_enchashment_normal_select']"
AMOUNT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_enchashment_amount']"
CONFIRM_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_enchashment_confirm']"
SUCCESS_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/useroperation_succeed_bt']"
CHECK_ELEMENT_EXISTS = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/trade_pop_info']"


class WithdrawPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(WithdrawPage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def perform_actions(self, *args, **kwargs):
        super(WithdrawPage, self).perform_actions(*args, **kwargs)

    @wait_for_page_to_load
    def go_to_withdraw_page(self):
        self.perform_actions(WITHDRAW_BUTTON)

    @wait_for_page_to_load
    def fast_withdraw(self, amount, keycodes):
        self.perform_actions(AMOUNT, amount, CONFIRM_BUTTON, interval=1.5)
        flag = self.element_exists(CHECK_ELEMENT_EXISTS)
        if flag:
            for i in keycodes:
                self.web_driver.press_keycode(i)
            self.perform_actions(SUCCESS_BUTTON)
        else:
            raise Exception('%s not found!' % CHECK_ELEMENT_EXISTS)
        return self

    @wait_for_page_to_load
    def regular_withdraw(self, amount, keycodes):
        self.perform_actions(REGULAR_WITHDRAW_RADIO, AMOUNT, amount, CONFIRM_BUTTON, interval=1.5)
        flag = self.element_exists(CHECK_ELEMENT_EXISTS)
        if flag:
            for i in keycodes:
                self.web_driver.press_keycode(i)
            self.perform_actions(SUCCESS_BUTTON)
        else:
            raise Exception('%s not found!' % CHECK_ELEMENT_EXISTS)

        return self
