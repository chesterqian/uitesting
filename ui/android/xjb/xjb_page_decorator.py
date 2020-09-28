# coding: utf-8
from functools import wraps
from selenium.common.exceptions import TimeoutException

CANCEL_GESTURE_BOTTUN = "//android.widget.TextView[@resource-id='com.shhxzq.xjb:id/setpassword_cancel']"
CANCEL_PROMPT = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_xjb_freshguide']"

PHONE_NUMBER = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_forget_pwd_mobile']"
GET_VERIFICATION_CODE_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_forget_get_verify_code']"
TEMPLATE_ID = 'cif_resetLoginPwd'
VERIFICATION_CODE_INPUT = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_forget_verify_code']"
CONFIRM_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_forget_mobile_next']"
LOGIN_PASSWORD = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_pwd_confirm']"
CONFIRM_2_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_confirm']"
LOGIN_PASSWORD_VERIFICATION = "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_pwd_confirm']"
CONFIRM_3_BUTTON = "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_confirm']"


def cancel_gasture_afterwards(func):
    @wraps(func)
    def wrapper(page_obj, *args, **kwargs):
        next_page_obj = func(page_obj, *args, **kwargs)
        try:
            page_obj.perform_actions(CANCEL_GESTURE_BOTTUN)
        except TimeoutException:
            pass

        return next_page_obj

    return wrapper


def cancel_prompt_afterwards(func):
    @wraps(func)
    def wrapper(page_obj, *args, **kwargs):
        next_page_obj = func(page_obj, *args, **kwargs)
        try:
            page_obj.perform_actions(CANCEL_PROMPT)
        except TimeoutException:
            pass

        return next_page_obj

    return wrapper


def return_page_afterwards(func):
    @wraps(func)
    def wrapper(from_page, *args, **kwargs):
        func(from_page, *args, **kwargs)

        ui_flow = from_page.ui_flow
        activity_map_return_page = from_page.activity_map_return_page
        return_page_name = activity_map_return_page[func.__name__]

        return_page = ui_flow[return_page_name]

        check = return_page.check_destination_page
        check(return_page)

        return return_page

    return wrapper
