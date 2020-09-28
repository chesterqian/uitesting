# coding: utf-8
from common.page_object import PageObject
# from database import SgwDataBaseOperator
from ui.android.xjb.recharge_page import RechargePage
from ui.android.xjb.withdraw_page import WithdrawPage
from .locator import GENERIC_LOADING_ICON


IDENTIFIER = "//android.widget.TextView[@text='现金宝']"
RECHARGE_BUTTON = "//android.widget.Button[@text='存入']"
WITHDRAW_BUTTON = "//android.widget.Button[@text='取出']"


class XjbDetailPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON
        super(XjbDetailPage, self).__init__(driver)

        self.check_destination_page(self)
        self.login_cookie = {'login_cookie': ''}
        self._db_operator = SgwDataBaseOperator('supergw_uat')

    def go_to_recharge_page(self):
        self.perform_actions(RECHARGE_BUTTON)
        page = RechargePage(self.web_driver)

        return page

    def go_to_withdraw_page(self):
        self.perform_actions(WITHDRAW_BUTTON)
        page = WithdrawPage(self.web_driver)

        return page
