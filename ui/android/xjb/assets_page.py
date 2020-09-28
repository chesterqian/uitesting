# coding: utf-8

from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from database import cif_database_operator
from ui.android.xjb.xjb_detail_page import XjbDetailPage
from .locator import GENERIC_LOADING_ICON
from .bank_card_management_page import BankCardManagementPage

IDENTIFIER = "//android.widget.TextView[@text='我的资产']"
CARD_MANAGEMENT_BUTTON = "//android.widget.TextView[@text='银行卡管理']"
XJB_BUTTON = "//android.widget.TextView[@text='现金宝']"


class AssetsPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(AssetsPage, self).__init__(driver)

        self.check_destination_page(self)
        self._bank_cards_amount = 0

    @property
    def bank_cards_amount(self):
        if not self._bank_cards_amount:
            self._cif_db_oprator = cif_database_operator

        self._bank_cards_amount = len(self._cif_db_oprator.get_all_cif_bank_card())

        return self._bank_cards_amount

    @wait_for_page_to_load
    def go_to_bank_card_management_page(self):
        self.handle_swipe_operation(IDENTIFIER, CARD_MANAGEMENT_BUTTON, 1)
        self.perform_actions(CARD_MANAGEMENT_BUTTON)
        page = BankCardManagementPage(self.web_driver)

        return page

    def go_to_xjb_detail_page(self):
        self.perform_actions(XJB_BUTTON)
        page = XjbDetailPage(self.web_driver)

        return page
