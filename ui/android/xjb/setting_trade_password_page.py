from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from database import SgwDataBaseOperator
from ui.android.xjb.context import PasswordHandle
from .locator import GENERIC_LOADING_ICON


IDENTIFIER = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_account_modify_pwd']"
GET_VERIFICATION_CODE_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_forget_get_verify_code']"
FIND_TRADE_PASSWORD = "//android.widget.RelativeLayout[@resource-id='com.shhxzq.xjb:id/rl_account_find_login_pwd']"
CHANGE_TRADE_PASSWORD = "//android.widget.RelativeLayout[@resource-id='com.shhxzq.xjb:id/rl_account_modify_login_pwd']"


class SettingTradePasswordPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON

        super(SettingTradePasswordPage, self).__init__(driver)

        self.check_destination_page(self)
        self._db_operator = SgwDataBaseOperator('supergw_uat')

    @wait_for_page_to_load
    def change_trade_password(self, trade_password, new_trade_password):
        self.perform_actions(CHANGE_TRADE_PASSWORD)
        ph = PasswordHandle()
        ph.all_handle(self, trade_password=trade_password, new_trade_password=new_trade_password)
