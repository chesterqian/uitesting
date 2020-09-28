from common.page_decorator import wait_for_page_to_load
from common.page_object import PageObject

SWIPE_CONDITION = "//android.widget.ImageButton[@resource-id='com.shhxzq.xjb:id/guide_bt']"
IDENTIFIER = "//android.widget.ImageView[@index='0']"
USER_NAME = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/etAccount']"
PASSWORD = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/etPwd']"
LOGIN_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/login_bt']"
LOGIN_REGISTER_BUTTON = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/tv_home_not_login_entrance']"
LOADING_ICON = "//android.widget.LinearLayout[@index='0']"
CANCEL_GESTURE_BOTTUN = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/setpassword_cancel']"
CANCEL_PROMPT = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_xjb_freshguide']"
SWIPE_SART_CONDITION = "//android.support.v4.view.ViewPager/android.widget.ImageView"
SWIPE_STOP_CONDITION = "//android.widget.ImageButton[@resource-id='com.shhxzq.xjb:id/guide_bt']"


def cancel_gasture(func):
    def wrapper(page_obj, *args, **kwargs):
        next_page_obj = func(page_obj, *args, **kwargs)
        if page_obj.element_exists(CANCEL_GESTURE_BOTTUN):
            page_obj.perform_actions(CANCEL_GESTURE_BOTTUN)

        return next_page_obj

    return wrapper


def cancel_prompt(func):
    def wrapper(page_obj, *args, **kwargs):
        next_page_obj = func(page_obj, *args, **kwargs)
        if page_obj.element_exists(CANCEL_PROMPT):
            page_obj.perform_actions(CANCEL_PROMPT)

        return next_page_obj

    return wrapper


class DemoPage(PageObject):
    def __init__(self, driver):
        self._page_identifier = IDENTIFIER
        self.loading_icon = LOADING_ICON
        super(DemoPage, self).__init__(driver)

        self.check_destination_page(self)

    @wait_for_page_to_load
    def go_to_main_page_with_new_session(self):
        self.handle_swipe_operation(SWIPE_SART_CONDITION, SWIPE_STOP_CONDITION)
        self.perform_actions(SWIPE_CONDITION)

    @wait_for_page_to_load
    def go_to_login_page(self):
        self.perform_actions(LOGIN_REGISTER_BUTTON)

    @wait_for_page_to_load
    @cancel_prompt
    @cancel_gasture
    def login(self, user_name, password):
        self.perform_actions(
            USER_NAME, user_name, PASSWORD, password, LOGIN_BUTTON)

        self.check_destination_page(self)

        return self
