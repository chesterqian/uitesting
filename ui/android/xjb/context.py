# coding: utf-8

find_login_pwd = {
    'IDENTIFIER': "//android.widget.TextView[@text='验证手机号码']",
    'PHONE_NUMBER': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_forget_pwd_mobile']",
    'GET_VERIFICATION_CODE': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_forget_get_verify_code']",
    'TEMPLATE_ID': 'cif_resetLoginPwd',
    'VERIFICATION_CODE_INPUT': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_forget_verify_code']",
    'NEXT_STEP_1': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_forget_mobile_next']",
    'LOGIN_PASSWORD': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_pwd_confirm']",
    'NEXT_STEP_2': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_confirm']",
    'LOGIN_PASSWORD_CONFIRM': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_pwd_confirm']",
    'NEXT_STEP_3': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_confirm']",
    'USER_NAME': "//android.widget.EditText[@text='请输入您的姓名']",
    'CERT_NO': "//android.widget.EditText[@text='请输入您的证件号码']",
    'NEXT_STEP_4': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_forget_ID_next']",
}

change_login_pwd = {
    'IDENTIFIER': "//android.widget.TextView[@text='验证当前密码']",
    'ORIGINAL_LOGIN_PASSWORD': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_current_pwd']",
    'NEXT_STEP_1': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_next']",
    'NEW_LOGIN_PASSWORD': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_pwd_confirm']",
    'NEXT_STEP_2': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_confirm']",
    'NEW_LOGIN_PASSWORD_CONFIRM': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/cedt_modify_pwd_confirm']",
    'NEXT_STEP_3': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/btn_modify_confirm']",

}

change_trade_pwd = {
    'IDENTIFIER': "//android.widget.TextView[@text='当前交易密码']",
    'ORIGINAL_TRADE_PASSWORD': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/tradepwd_et']",
    'NEXT_STEP_1': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/tradepwd_btn']",
    'NEW_TRADE_PASSWORD': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/tradepwd_et']",
    'NEW_TRADE_PASSWORD_CONFIRM': "//android.widget.EditText[@resource-id='com.shhxzq.xjb:id/tradepwd_et']",
    'NEXT_STEP_2': "//android.widget.Button[@resource-id='com.shhxzq.xjb:id/tradepwd_btn']",

}

change_phone_by_sms = {
    'IDENTIFIER': "//android.widget.TextView[@text='更换绑定手机']",
    'TEMPLATE_ID': 'cif_changeMobile',
    'VERIFICATION_CODE_INPUT_1': "//android.widget.EditText[@text='请输入验证码']",
    'NEXT_STEP_1': "//android.widget.Button[@text='下一步']",
    'PHONE_NUMBER': "//android.widget.EditText[@text='请输入11位手机号码']",
    'GET_VERIFICATION_CODE': "//android.widget.Button[@text='获取验证码']",
    'VERIFICATION_CODE_INPUT_2': "//android.widget.EditText[@text='请输入验证码']",
    'NEXT_STEP_2': "//android.widget.Button[@text='下一步']",
    'NEXT_STEP_3': "//android.widget.Button[@text='确认']",

}


class PasswordHandle(object):
    def all_handle(self, page_object, **kwargs):

        msg = 'argument error!'

        def on_input(input_list):
            for key in kwargs.keys():
                if not key in input_list:
                    raise Exception(msg)

        if page_object.element_exists(find_login_pwd['IDENTIFIER'], timeout=3):
            input_list = ['phone_number', 'login_password', 'is_bind_card', 'user_name', 'cert_no']
            on_input(input_list)

            verification_code = \
                page_object._db_operator.get_verification_code(kwargs['phone_number'], find_login_pwd['TEMPLATE_ID'])

            if (kwargs['is_bind_card'] == 'N'):
                args = [
                    find_login_pwd['PHONE_NUMBER'], kwargs['phone_number'],
                    find_login_pwd['GET_VERIFICATION_CODE'],
                    find_login_pwd['VERIFICATION_CODE_INPUT'], verification_code,
                    find_login_pwd['NEXT_STEP_1'],
                    find_login_pwd['LOGIN_PASSWORD'], kwargs['login_password'],
                    find_login_pwd['NEXT_STEP_2'],
                    find_login_pwd['LOGIN_PASSWORD_CONFIRM'], kwargs['login_password'],
                    find_login_pwd['NEXT_STEP_3'],
                ]

                page_object.perform_actions(*args)
                pass

            if (kwargs['is_bind_card'] == 'Y'):
                args = [
                    find_login_pwd['PHONE_NUMBER'], kwargs['phone_number'],
                    find_login_pwd['GET_VERIFICATION_CODE'],
                    find_login_pwd['VERIFICATION_CODE_INPUT'], verification_code,
                    find_login_pwd['NEXT_STEP_1'],
                    find_login_pwd['USER_NAME'], kwargs['user_name'],
                    find_login_pwd['CERT_NO'], kwargs['cert_no'],
                    find_login_pwd['NEXT_STEP_4'],
                    find_login_pwd['LOGIN_PASSWORD'], kwargs['login_password'],
                    find_login_pwd['NEXT_STEP_2'],
                    find_login_pwd['LOGIN_PASSWORD_CONFIRM'], kwargs['login_password'],
                    find_login_pwd['NEXT_STEP_3'],
                ]

                page_object.perform_actions(*args)
                pass

        if page_object.element_exists(change_login_pwd['IDENTIFIER'], timeout=3):
            input_list = ['login_password', 'new_login_password']
            on_input(input_list)

            args = [
                change_login_pwd['ORIGINAL_LOGIN_PASSWORD'], kwargs['login_password'],
                change_login_pwd['NEXT_STEP_1'],
                change_login_pwd['NEW_LOGIN_PASSWORD'], kwargs['new_login_password'],
                change_login_pwd['NEXT_STEP_2'],
                change_login_pwd['NEW_LOGIN_PASSWORD_CONFIRM'], kwargs['new_login_password'],
                change_login_pwd['NEXT_STEP_3'],
            ]

            page_object.perform_actions(*args)
            pass

        if page_object.element_exists(change_trade_pwd['IDENTIFIER'], timeout=3):
            input_list = ['trade_password', 'new_trade_password']
            on_input(input_list)

            args = [
                change_trade_pwd['ORIGINAL_TRADE_PASSWORD'], kwargs['trade_password'],
                change_trade_pwd['NEXT_STEP_1'],
                change_trade_pwd['NEW_TRADE_PASSWORD'], kwargs['new_trade_password'],
                change_trade_pwd['NEW_TRADE_PASSWORD_CONFIRM'], kwargs['new_trade_password'],
                change_trade_pwd['NEXT_STEP_2'],
            ]

            page_object.perform_actions(*args)
            pass


class PhoneHandle():
    def all_handle(self, page_object, **kwargs):

        msg = 'argument error!'

        def on_input(input_list):
            for key in kwargs.keys():
                if not key in input_list:
                    raise Exception(msg)

        if page_object.element_exists(change_phone_by_sms['IDENTIFIER'], timeout=3):
            input_list = ['phone_number', 'new_phone_number']
            on_input(input_list)

            verification_code_1 = \
                page_object._db_operator.get_verification_code(kwargs['phone_number'],
                                                               change_phone_by_sms['TEMPLATE_ID'])

            args_1 = [
                change_phone_by_sms['VERIFICATION_CODE_INPUT_1'], verification_code_1,
                change_phone_by_sms['NEXT_STEP_1'],
                change_phone_by_sms['PHONE_NUMBER'], kwargs['new_phone_number'],
                change_phone_by_sms['GET_VERIFICATION_CODE'],
            ]

            page_object.perform_actions(*args_1)

            verification_code_2 = \
                page_object._db_operator.get_verification_code(kwargs['new_phone_number'],
                                                               change_phone_by_sms['TEMPLATE_ID'])

            args_2 = [
                change_phone_by_sms['VERIFICATION_CODE_INPUT_2'], verification_code_2,
                change_phone_by_sms['NEXT_STEP_2'],
                change_phone_by_sms['NEXT_STEP_3'],
            ]

            page_object.perform_actions(*args_2)
            pass
