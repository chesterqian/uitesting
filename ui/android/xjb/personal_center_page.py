# coding: utf-8
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from ui.android.xjb.invite_friend_page import InviteFriendPage
from ui.android.xjb.security_center_page import SecurityCenterPage
from ui.android.xjb.share_friend_page import ShareFriendPage
from .locator import GENERIC_LOADING_ICON


IDENTIFIER = "//android.widget.TextView[@text='个人中心']"
INVITE_FRIEND = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/setting_item_inviter']"
SHARE_FRIEND = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/setting_item_share']"
SECURITY_CENTER = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/setting_item_secure']"


class PersonalCenterPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON
        super(PersonalCenterPage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def go_to_invite_friend_page(self):
        self.perform_actions(INVITE_FRIEND)
        page = InviteFriendPage(self.web_driver)

        return page

    @wait_for_page_to_load
    def go_to_share_friend_page(self):
        self.perform_actions(SHARE_FRIEND)
        page = ShareFriendPage(self.web_driver)

        return page

    @wait_for_page_to_load
    def go_to_security_center_page(self):
        self.perform_actions(SECURITY_CENTER)
        page = SecurityCenterPage(self.web_driver)

        return page
