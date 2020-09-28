from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from ui.android.xjb.assets_page import AssetsPage
from ui.android.xjb.personal_center_page import PersonalCenterPage
from .locator import GENERIC_LOADING_ICON
from .login_page import LoginPage
from .withdraw_page import WithdrawPage
from .recharge_page import RechargePage

LOGIN_REGISTER_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_home_not_login_entrance']"
TV_MARKETING_INFO = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_hmarketing_intro_no']"
TV_MARKETING_INFO_CHARACTER = "//android.widget.TextView[@resource-id=com.shhxzq.xjb:id/tv_hmarketing_intro_character']"
IDENTIFIER = "//android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/img_home_actionbar_left']"
WITHDRAW_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_home_enchashment']"
RECHARGE_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_home_recharge']"
PERSONAL_CENTER_BUTTON = "//android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/img_home_actionbar_left']"
ASSETS_BUTTON = "//android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/tab_image']"


class HomePage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        super(HomePage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def go_to_register_page(self):
        pass

    @wait_for_page_to_load
    def go_to_login_page(self):
        self.perform_actions(LOGIN_REGISTER_BUTTON)
        page = LoginPage(self.web_driver)

        return page

    @wait_for_page_to_load
    def go_to_finadcial_page(self, sub_page='DqbPage'):
        # sub_page:DqbPage\FoundPage
        page_map_navigation_element = {
            'DqbPage': TV_MARKETING_INFO,
            'FoundPage': TV_MARKETING_INFO_CHARACTER
        }
        element = page_map_navigation_element[sub_page]

        self.perform_actions(element)

        page = getattr(sub_page, '__init__')(self.web_driver)
        self.check_destination_page(page)
        return page

    @wait_for_page_to_load
    def go_to_withdraw_page(self):
        self.perform_actions(WITHDRAW_BUTTON)
        page = WithdrawPage(self.web_driver)
        return page

    @wait_for_page_to_load
    def go_to_recharge_page(self):
        self.perform_actions(RECHARGE_BUTTON)
        page = RechargePage(self.web_driver)
        return page

    @wait_for_page_to_load
    def go_to_assets_page(self):
        self.perform_actions(ASSETS_BUTTON)
        page = AssetsPage(self.web_driver)
        return page

    @wait_for_page_to_load
    def go_to_personal_center_page(self):
        self.perform_actions(PERSONAL_CENTER_BUTTON)
        page = PersonalCenterPage(self.web_driver)
        return page
