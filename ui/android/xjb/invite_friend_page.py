# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from .locator import GENERIC_LOADING_ICON

IDENTIFIER = "//android.widget.TextView[@text='邀请人']"
PHONE_NUMBER = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/et_inviter_mobile']"
CONFIRM_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_inviter_next']"
PREVIOUS_PAGE_BUTTON = "//android.widget.RelativeLayout[@class='android.widget.RelativeLayout']"


class InviteFriendPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON

        super(InviteFriendPage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def invite_friend(self, phone_number):
        self.perform_actions(PHONE_NUMBER, phone_number, CONFIRM_BUTTON)
