# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
# from database import sgw_database_operator
from ui.android.xjb.context import PhoneHandle
from .locator import GENERIC_LOADING_ICON

IDENTIFIER = "//android.widget.TextView[@text='修改绑定手机']"
CAN_RECEIVE_SMS = "//android.widget.TextView[@text='能接收短信']"
CAN_NOT_RECEIVE_SMS = "//android.widget.TextView[@text='不能接收短信']"


class SettingChangePhonePage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON

        super(SettingChangePhonePage, self).__init__(driver)

        self.check_destination_page(self)
        self._db_operator = sgw_database_operator

    @wait_for_page_to_load
    def change_phone_by_sms(self, phone_number, new_phone_number):
        self.perform_actions(CAN_RECEIVE_SMS)
        ph = PhoneHandle()
        ph.all_handle(self, phone_number=phone_number, new_phone_number=new_phone_number)