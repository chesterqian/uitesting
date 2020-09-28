# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from database import sgw_database_operator
from .locator import GENERIC_LOADING_ICON
from .binding_card_page import BindingCardPage
from .xjb_page_decorator import cancel_gasture_afterwards, return_page_afterwards
from .xjb_page_decorator import cancel_prompt_afterwards


IDENTIFIER = "//android.widget.TextView[@text='注册']"
PHONE_NUMBER = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/register_step1_phone']"
PASSWORD = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/register_pwd']"
CONFIRM_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/register_step1_sure_btn']"
GET_VERIFICATION_CODE_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/register_authcode_btn']"
VERIFICATION_CODE_INPUT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/register_authcode_et']"
BINDING_CARD_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/useroperation_succeed_bt']"
TEMPLATE_ID = 'cif_register'
SHOPPING_FIRST_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_register_succeed_stroll_first']"


class RegisterPage(PageObject):
    activity_map_return_page = {'shopping': 'HomePage'}

    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(RegisterPage, self).__init__(driver)

        self.check_destination_page(self)

        self._phone_number = None
        self._db_operator = sgw_database_operator

    @property
    def phone_number(self):
        return self._phone_number

    def go_to_binding_card_page(self):
        self.perform_actions(BINDING_CARD_BUTTON)
        page = BindingCardPage(self.web_driver, self.phone_number, self.__class__.__name__)

        return page

    def register(self, phone_number, password):
        self.perform_actions(PHONE_NUMBER, phone_number,
                             GET_VERIFICATION_CODE_BUTTON,
                             PASSWORD, password)

        verification_code = \
            self._db_operator.get_verification_code(phone_number, TEMPLATE_ID)
        self.perform_actions(VERIFICATION_CODE_INPUT,
                             verification_code, CONFIRM_BUTTON)

        self._phone_number = phone_number
        
    @return_page_afterwards
    @cancel_prompt_afterwards
    @cancel_gasture_afterwards
    @wait_for_page_to_load
    def shopping(self):
        self.perform_actions(SHOPPING_FIRST_BUTTON)