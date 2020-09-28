# coding: utf-8
from functools import wraps

from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from common.utility import Utility
# from database import cif_database_operator, sgw_database_operator
from .locator import GENERIC_LOADING_ICON
from .xjb_page_decorator import cancel_gasture_afterwards
from .xjb_page_decorator import cancel_prompt_afterwards

IDENTIFIER_1 = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/tradepwd_et']"
IDENTIFIER_2 = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/title_actionbar' and @text='绑定银行卡']"
TRADE_CODE_INPUT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/tradepwd_et']"
CONFIRM_TRADE_CODE_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/tradepwd_btn']"
BANK_CARD_INPUT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/bind_card_account']"
BANK_CARD_CERT_ID = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/bind_card_certID']"
BANK_CARD_PHONE_NUMBER_INPUT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/bind_card_phonenumber']"
GET_VERIFICATION_CODE_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/bind_card_checkcode_bt']"
VERIFICATION_CODE_INPUT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/bind_card_checkcode']"
BINDING_OPERATION_SUCCESS = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/bind_card_checkcode_bt']"
BINDING_OPERATION_NEXT_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/bind_card_sure_bt']"
BINDING_OPERATION_SUCCESS_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/useroperation_succeed_bt']"
BIND_CARD_USERNAME = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/bind_card_username']"
TEMPLATE_ID = 'cif_bindBankCard'


def handle_trade_code(func):
    @wraps(func)
    def wrapper(page_obj, *args, **kwargs):
        if not page_obj.has_bank_card:
            trade_code = '135790'
            operation_args = ([TRADE_CODE_INPUT, trade_code]) * 2 + \
                             [CONFIRM_TRADE_CODE_BUTTON]
            page_obj.perform_actions(*operation_args)

        return func(page_obj, *args, **kwargs)

    return wrapper


class BindingCardPage(PageObject):
    def __init__(self, driver, phone_number, from_page):
        # from_page: RegisterPage/BankCardManagementPage
        super(BindingCardPage, self).__init__(driver)

        self.loading_icon = GENERIC_LOADING_ICON
        self._has_bank_card = None
        self._phone_number = phone_number

        if self.has_bank_card:
            self._page_identifier = IDENTIFIER_2
        else:
            self._page_identifier = IDENTIFIER_1
        self.check_destination_page(self)

        self._faker_cn = Utility().fake_cn
        self._faker_en = Utility().fake_en
        self._sgw_db_operator = sgw_database_operator

        self._from_page = from_page

    @wait_for_page_to_load
    def perform_actions(self, *args, **kwargs):
        super(BindingCardPage, self).perform_actions(*args, **kwargs)

    @property
    def has_bank_card(self):
        if not hasattr(self, '_cif_db_operator'):
            self._cif_db_operator = cif_database_operator

        base_account_db_record = \
            self._cif_db_operator.get_cif_base_account(mobile=self._phone_number)
        bank_card_info_db_record = \
            self._cif_db_operator.get_cif_bank_card_info(cust_no=base_account_db_record.cust_no)

        self._has_bank_card = bank_card_info_db_record and True or False

        return self._has_bank_card

    @cancel_prompt_afterwards
    @cancel_gasture_afterwards
    @handle_trade_code
    def binding_card(self, bank_card_prefix):
        args = None
        if self._from_page == 'BankCardManagementPage':
            args = [
                BANK_CARD_INPUT, bank_card_prefix + self._faker_cn.credit_card_number(),
                BANK_CARD_PHONE_NUMBER_INPUT, self._phone_number,
                GET_VERIFICATION_CODE_BUTTON,
            ]
        elif self._from_page == 'RegisterPage':
            args = [
                BANK_CARD_INPUT, bank_card_prefix + self._faker_cn.credit_card_number(),
                BANK_CARD_CERT_ID, self._faker_cn.create_id_card(),
                BIND_CARD_USERNAME, self._faker_en.name_male(),
                BANK_CARD_PHONE_NUMBER_INPUT, self._phone_number,
                GET_VERIFICATION_CODE_BUTTON,
            ]
        self.perform_actions(*args)

        verification_code = self._sgw_db_operator.get_verification_code(
            sgw_sms_mobile=self._phone_number, template_id=TEMPLATE_ID)

        args = [
            VERIFICATION_CODE_INPUT, str(verification_code),
            BINDING_OPERATION_NEXT_BUTTON
        ]
        self.perform_actions(*args)

        # submit request
        self.perform_actions(BINDING_OPERATION_SUCCESS_BUTTON)
