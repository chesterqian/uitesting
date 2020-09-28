from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from .locator import GENERIC_LOADING_ICON

IDENTIFIER = "//android.widget.ImageView[@index='0']"
RECHARGE_AMOUNT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_recharge_amount']"
RECHARGE_CONFIRM_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_recharge_next']"
SUCCESS_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/useroperation_succeed_bt']"
CHECK_ELEMENT_EXISTS = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/trade_pop_info']"


class RechargePage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(RechargePage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def recharge(self, recharge_amount, keycodes):
        self.perform_actions(RECHARGE_AMOUNT, recharge_amount, RECHARGE_CONFIRM_BUTTON)
        self.element_exists(CHECK_ELEMENT_EXISTS)
        for i in keycodes:
            self.web_driver.press_keycode(i)
        self.perform_actions(SUCCESS_BUTTON)
        return self
