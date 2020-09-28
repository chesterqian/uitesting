# coding: utf-8
from common.page_object import PageObject
from .locator import GENERIC_LOADING_ICON

IDENTIFIER = "//android.widget.Button[@class='android.widget.Button']"
PHONE_NUMBER = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/et_inviter_mobile']"
SHARE_FRIEND = "//android.widget.Button[@innerText='分享给好友']"
WEIXIN_FRIEND = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tvWeixin']"


class ShareFriendPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self._loading_icon = GENERIC_LOADING_ICON

        super(ShareFriendPage, self).__init__(driver)

        self.check_destination_page(self)

