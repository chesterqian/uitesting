import time
from robot.api.deco import keyword
from robot.api import logger
from selenium.common.exceptions import NoSuchElementException
from basic_controller import BasicController
from common.utility import Utility
from tools.mobile.controller.adb import install_apk
from ui.android.xjb.account_info import AccountInfo
from ui.android.xjb.main_page import MainPage

APP_ACCESS_ALLOW_BUTTON = "//android.widget.Button[@resource-id='com.huawei.systemmanager:id/btn_allow']"

ACCOUNT = {
    'p1': AccountInfo('p1'),
    'u1': AccountInfo('u1'),
    'u2': AccountInfo('u2'),
    'u3': AccountInfo('u3'),
}


def take_sreen_shot(driver):
    file_name = str(str(time.time()).replace('.', ''))
    driver.get_screenshot_as_file(
        '/Users/linkinpark/jenkins_workspace/workspace/xjb_android_test/' + file_name + '.jpg')
    logger.info('<a href="%s.jpg"><img src="%s.jpg" width="%s"></a>'
                % (file_name, file_name, '250'), html=True)


class MainPageWatcher:
    def __init__(self, page):
        self.page = page

    def __getattr__(self, attribute):
        if hasattr(self.page, attribute):
            value = getattr(self.page, attribute)
            if callable(value):
                driver = self.page.web_driver

                def wrapper(*args, **kwargs):
                    value(*args, **kwargs)

                    logger.info(attribute)
                    take_sreen_shot(driver)

                return wrapper


class MainPageController(BasicController):
    util = Utility()
    started = False

    def handle_security_prompt(self):
        try:
            button = self.web_driver.find_element_by_xpath(APP_ACCESS_ALLOW_BUTTON)
            button.click()
        except NoSuchElementException:
            pass

    @keyword('Set Environemt Args1')
    def set_environemt_args1(self, app_path, platform_name, version, account):
        assert 0
        self.app_path = app_path
        self.platform_name = platform_name
        self.version = version
        self.account = ACCOUNT[account]

        if not self.started:
            apk_path = self.util.intersection_of_path(app_path)
            install_apk(apk_path)

            self.started = True

        self.open_app(app_path, platform_name, version, 'false')

        self.handle_security_prompt()

        page = MainPage(self.web_driver)
        self.main_page = MainPageWatcher(page)

    @keyword('Case Tear Down')
    def tear_down(self):
        take_sreen_shot(self.web_driver)
        self.web_driver.quit()

    @keyword('test home page recharge')
    def test_home_page_recharge(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_recharge_page()
        self.main_page.recharge(self.account.recharge_amount, self.account.trade_password)

    @keyword('test home page fast withdraw')
    def test_home_page_fast_withdraw(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_withdraw_page()
        self.main_page.fast_withdraw(self.account.withdraw_amount, self.account.trade_password)

    @keyword('test home page regular withdraw')
    def test_home_page_regular_withdraw(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_withdraw_page()
        self.main_page.regular_withdraw(self.account.withdraw_amount, self.account.trade_password)

    @keyword('test xjb detail page recharge')
    def test_xjb_detail_page_recharge(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_assets_page()
        self.main_page.go_to_xjb_detail_page()
        self.main_page.go_to_recharge_page()
        self.main_page.recharge(self.account.recharge_amount, self.account.trade_password)

    @keyword('test xjb detail page fast withdraw')
    def test_xjb_detail_page_fast_withdraw(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_assets_page()
        self.main_page.go_to_xjb_detail_page()
        self.main_page.go_to_withdraw_page()
        self.main_page.fast_withdraw(self.account.withdraw_amount, self.account.trade_password)

    @keyword('test xjb detail page regular withdraw')
    def test_xjb_detail_page_regular_withdraw(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_assets_page()
        self.main_page.go_to_xjb_detail_page()
        self.main_page.go_to_withdraw_page()
        self.main_page.regular_withdraw(self.account.withdraw_amount, self.account.trade_password)

    @keyword('test register not binding card')
    def test_register_not_binding_card(self):
        phone_number = self.util.fake_cn.phone_number()
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.go_to_register_page()
        self.main_page.register(phone_number, '12qwaszx')
        self.main_page.shopping()

    @keyword('test register binding card')
    def test_register_binding_card(self):
        phone_number = self.util.fake_cn.phone_number()
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.go_to_register_page()
        self.main_page.register(phone_number, '12qwaszx')
        self.main_page.go_to_binding_card_page()
        self.main_page.binding_card('622202')

    @keyword('test register unbundling card')
    def test_register_unbundling_card(self):
        phone_number = self.util.fake_cn.phone_number()
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.go_to_register_page()
        self.main_page.register(phone_number, '12qwaszx')
        self.main_page.go_to_binding_card_page()
        self.main_page.binding_card('622202')
        self.main_page.go_to_assets_page()
        self.main_page.go_to_bank_card_management_page()
        self.main_page.unbundling_card((8, 10, 12, 14, 16, 7))

    @keyword('test login binding card')
    def test_login_binding_card(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_assets_page()
        self.main_page.go_to_bank_card_management_page()
        self.main_page.go_to_binding_card_page()
        self.main_page.binding_card('622202')

    @keyword('test personal center invite friend')
    def test_personal_center_invite_friend(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_invite_friend_page()
        self.main_page.invite_friend('15888888888')

    # @keyword('test personal center share weixin friend')
    # def test_personal_center_share_weixin_friend(self):
    #     self.main_page.go_to_home_page()
    #     self.main_page.go_to_login_page()
    #     self.main_page.login(self.account.phone_number, self.account.login_password)
    #     self.main_page.go_to_personal_center_page()
    #     self.main_page.go_to_share_friend_page()
    #     self.main_page.share_friend('weixin_friend')

    # @keyword('test personal center share weixin circle')
    # def test_personal_center_share_weixin_circle(self):
    #     self.main_page.go_to_home_page()
    #     self.main_page.go_to_login_page()
    #     self.main_page.login(self.account.phone_number, self.account.login_password)
    #     self.main_page.go_to_personal_center_page()
    #     self.main_page.go_to_share_friend_page()
    #     self.main_page.share_friend('weixin_circle')

    # @keyword('test personal center share weibo')
    # def test_personal_center_share_weibo(self):
    #     self.main_page.go_to_home_page()
    #     self.main_page.go_to_login_page()
    #     self.main_page.login(self.account.phone_number, self.account.login_password)
    #     self.main_page.go_to_personal_center_page()
    #     self.main_page.go_to_share_friend_page()
    #     self.main_page.share_friend('weibo')

    @keyword('test login page find login password user not binding card')
    def test_login_page_find_login_password_user_not_binding_card(self):
        self.account = AccountInfo('u2')
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.find_login_password(self.account.is_bind_card, self.account.phone_number,
                                           self.account.login_password, self.account.user_name,
                                           self.account.cert_no)

    @keyword('test login page find login password user binding card')
    def test_login_page_find_login_password_user_binding_card(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.find_login_password(self.account.is_bind_card, self.account.phone_number,
                                           self.account.login_password, self.account.user_name,
                                           self.account.cert_no)

    @keyword('test setting find login password user not binding card')
    def test_setting_find_login_password_user_not_binding_card(self):
        self.account = AccountInfo('u2')
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_security_center_page()
        self.main_page.go_to_setting_login_password_page()
        self.main_page.find_login_password(self.account.is_bind_card, self.account.phone_number,
                                           self.account.login_password, self.account.user_name,
                                           self.account.cert_no)

    @keyword('test setting find login password user binding card')
    def test_setting_find_login_password_user_binding_card(self):
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(self.account.phone_number, self.account.login_password)
        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_security_center_page()
        self.main_page.go_to_setting_login_password_page()
        self.main_page.find_login_password(self.account.is_bind_card, self.account.phone_number,
                                           self.account.login_password, self.account.user_name,
                                           self.account.cert_no)

    @keyword('test setting change login password')
    def test_setting_change_login_password(self):
        phone_number = self.util.fake_cn.phone_number()
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.go_to_register_page()
        self.main_page.register(phone_number, '12qwaszx')
        self.main_page.shopping()

        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_security_center_page()
        self.main_page.go_to_setting_login_password_page()
        self.main_page.change_login_password('12qwaszx', 'a1111111')

        self.web_driver.quit()
        self.open_app(self.app_path, self.platform_name, self.version, 'false')
        self.handle_security_prompt()

        page = MainPage(self.web_driver)
        self.main_page = MainPageWatcher(page)

        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(phone_number, 'a1111111')

    @keyword('test setting change trade password')
    def test_setting_change_trade_password(self):
        phone_number = '18994455607'
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(phone_number, '12qwaszx')

        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_security_center_page()
        self.main_page.go_to_setting_trade_password_page()
        self.main_page.change_trade_password('147258', '135790')

        self.web_driver.quit()
        self.open_app(self.app_path, self.platform_name, self.version, 'false')
        self.handle_security_prompt()

        page = MainPage(self.web_driver)
        self.main_page = MainPageWatcher(page)

        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(phone_number, '12qwaszx')
        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_security_center_page()
        self.main_page.go_to_setting_trade_password_page()
        self.main_page.change_trade_password('135790', '147258')

    @keyword('test setting change phone by sms')
    def test_setting_change_phone_by_sms(self):
        phone_number = self.util.fake_cn.phone_number()
        phone_number2 = self.util.fake_cn.phone_number()
        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.go_to_register_page()
        self.main_page.register(phone_number, '12qwaszx')
        self.main_page.shopping()

        self.main_page.go_to_personal_center_page()
        self.main_page.go_to_security_center_page()
        self.main_page.go_to_setting_change_phone_page()
        self.main_page.change_phone_by_sms(phone_number, phone_number2)

        self.web_driver.quit()
        self.open_app(self.app_path, self.platform_name, self.version, 'false')
        self.handle_security_prompt()

        page = MainPage(self.web_driver)
        self.main_page = MainPageWatcher(page)

        self.main_page.go_to_home_page()
        self.main_page.go_to_login_page()
        self.main_page.login(phone_number2, '12qwaszx')
