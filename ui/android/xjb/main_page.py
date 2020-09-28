# coding: utf-8
from .home_page import HomePage
from .assets_page import AssetsPage
from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject
from .locator import GENERIC_LOADING_ICON

SWIPE_STOP_CONDITION = "//android.widget.ImageButton[@resource-id='com.shhxzq.xjb:id/guide_bt']"
SWIPE_SART_CONDITION = "//android.support.v4.view.ViewPager/android.widget.ImageView"
IDENTIFIER = "//android.widget.ImageView[@index='0']"
LOGIN_REGISTER_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_home_not_login_entrance']"
HOME_PAGE_NAVIGATOR = "//android.widget.RelativeLayout[1]/android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/tab_image']"
FINACIAL_PAGE_NEVIGATOR = "//android.widget.RelativeLayout[2]/android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/tab_image']"
ASSETS_PAGE_NEVIGATOR = "//android.widget.RelativeLayout[3]/android.widget.ImageView[@resource-id='com.shhxzq.xjb:id/tab_image']"


class MainPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = GENERIC_LOADING_ICON
        self._current_xjb_page = None
        self._ui_flow = {}
        super(MainPage, self).__init__(driver)

        self.check_destination_page(self)

    def __getattr__(self, attribute):

        if hasattr(self._current_xjb_page, attribute):
            attribute_value = getattr(self._current_xjb_page, attribute)

            if callable(attribute_value):
                def wrapper(*args, **kwargs):
                    return_page = attribute_value(*args, **kwargs)

                    if not isinstance(return_page, PageObject):
                        pass
                    else:
                        self._ui_flow.update({return_page.__class__.__name__: return_page})
                        self.current_xjb_page = return_page

                    return return_page

                return wrapper

            return attribute_value
        else:
            return super(MainPage, self).__getattr__(attribute)

    @property
    def current_xjb_page(self):
        return self._current_xjb_page

    @current_xjb_page.setter
    def current_xjb_page(self, value):
        setattr(value, 'ui_flow', self.ui_flow)
        self._current_xjb_page = value

    @property
    def ui_flow(self):
        return self._ui_flow

    @wait_for_page_to_load
    def perform_actions(self, *args, **kwargs):
        super(MainPage, self).perform_actions(*args, **kwargs)

    @wait_for_page_to_load
    def go_to_home_page(self):
        self.handle_swipe_operation(SWIPE_SART_CONDITION,
                                    SWIPE_STOP_CONDITION)
        self.perform_actions(SWIPE_STOP_CONDITION)

        return_page = HomePage(self.web_driver)
        self._ui_flow.update({return_page.__class__.__name__: return_page})
        self.current_xjb_page = return_page

        return self.current_xjb_page

    @wait_for_page_to_load
    def go_to_assets_page(self):
        self.perform_actions(ASSETS_PAGE_NEVIGATOR)
        self.current_xjb_page = AssetsPage(self.web_driver)

        return self._current_xjb_page