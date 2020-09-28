# coding: utf-8
import unittest

from selenium.common.exceptions import NoSuchElementException

# from common.utility import Utility
from controller.basic_controller import BasicController
from ui.android.xjb.account_info import AccountInfo
from ui.android.xjb.main_page import MainPage

APP_ACCESS_ALLOW_BUTTON = "//android.widget.Button[@resource-id='com.huawei.systemmanager:id/btn_allow']"
# ACCOUNT = AccountInfo('p1')
ACCOUNT = AccountInfo('u3')


class MainPageTest(unittest.TestCase):
    def setUp(self):
        # self.util = Utility()
        self.app_path = 'huaxin/ui/apps/hxxjb-uat-latest.apk'
        # self.app_path = 'huaxin/ui/apps/hxxjb-test-develop-release-1.4.1-b10.apk'
        self.platform_version = '6.0'
        # self.driver = BasicController().open_android_app(self.app_path, self.platform_version)
        self.driver = BasicController().open_web_driver('chrome')
        self.driver.get("https://cn.bing.com/")
        assert 0
        # assert 0
        try:
            button = self.driver.find_element_by_xpath(APP_ACCESS_ALLOW_BUTTON)
            button.click()
        except NoSuchElementException:
            pass

    def tearDown(self):
        self.driver.quit()

    # def test_home_page_recharge(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_recharge_page()
    #     page.recharge(ACCOUNT.recharge_amount, ACCOUNT.trade_password)
    #
    # def test_home_page_fast_withdraw(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_withdraw_page()
    #     page.fast_withdraw(ACCOUNT.withdraw_amount, ACCOUNT.trade_password)
    #
    # def test_home_page_regular_withdraw(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_withdraw_page()
    #     page.regular_withdraw(ACCOUNT.withdraw_amount, ACCOUNT.trade_password)
    #
    # def test_xjb_detail_page_recharge(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_assets_page()
    #     page.go_to_xjb_detail_page()
    #     page.go_to_recharge_page()
    #     page.recharge(ACCOUNT.recharge_amount, ACCOUNT.trade_password)
    #
    # def test_xjb_detail_page_fast_withdraw(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_assets_page()
    #     page.go_to_xjb_detail_page()
    #     page.go_to_withdraw_page()
    #     page.fast_withdraw(ACCOUNT.withdraw_amount, ACCOUNT.trade_password)
    #
    # def test_xjb_detail_page_regular_withdraw(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_assets_page()
    #     page.go_to_xjb_detail_page()
    #     page.go_to_withdraw_page()
    #     page.regular_withdraw(ACCOUNT.withdraw_amount, ACCOUNT.trade_password)
    #
    # def test_register_not_binding_card(self):
    #     phone_number = self.util.fake_cn.phone_number()
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.go_to_register_page()
    #     page.register(phone_number, '12qwaszx')
    #     page.shopping()
    #
    # def test_register_binding_card(self):
    #     phone_number = self.util.fake_cn.phone_number()
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.go_to_register_page()
    #     page.register(phone_number, '12qwaszx')
    #     page.go_to_binding_card_page()
    #     page.binding_card('622202')
    #
    # def test_register_unbundling_card(self):
    #     phone_number = self.util.fake_cn.phone_number()
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.go_to_register_page()
    #     page.register(phone_number, '12qwaszx')
    #     page.go_to_binding_card_page()
    #     page.binding_card('622202')
    #     page.go_to_assets_page()
    #     page.go_to_bank_card_management_page()
    #     page.unbundling_card((8, 10, 12, 14, 16, 7))
    #
    # def test_login_binding_card(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_assets_page()
    #     page.go_to_bank_card_management_page()
    #     page.go_to_binding_card_page()
    #     page.binding_card('622202')
    #
    # def test_personal_center_invite_friend(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_personal_center_page()
    #     page.go_to_invite_friend_page()
    #     page.invite_friend('15888888888')
    #
    # def test_personal_center_share_weixin_friend(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_personal_center_page()
    #     page.go_to_share_friend_page()
    #     page.share_friend('weixin_friend')
    #
    # def test_personal_center_share_weixin_circle(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_personal_center_page()
    #     page.go_to_share_friend_page()
    #     page.share_friend('weixin_circle')
    #
    # def test_personal_center_share_weibo(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_personal_center_page()
    #     page.go_to_share_friend_page()
    #     page.share_friend('weibo')
    #
    # def test_login_page_find_login_password_user_not_binding_card(self):
    #     ACCOUNT = AccountInfo('u2')
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.find_login_password(ACCOUNT.is_bind_card, ACCOUNT.phone_number,
    #                              ACCOUNT.login_password, ACCOUNT.user_name,
    #                              ACCOUNT.cert_no)
    #
    # def test_login_page_find_login_password_user_binding_card(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.find_login_password(ACCOUNT.is_bind_card, ACCOUNT.phone_number,
    #                              ACCOUNT.login_password, ACCOUNT.user_name,
    #                              ACCOUNT.cert_no)
    #
    # def test_setting_find_login_password_user_not_binding_card(self):
    #     ACCOUNT = AccountInfo('u2')
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_personal_center_page()
    #     page.go_to_security_center_page()
    #     page.go_to_setting_login_password_page()
    #     page.find_login_password(ACCOUNT.is_bind_card, ACCOUNT.phone_number,
    #                              ACCOUNT.login_password, ACCOUNT.user_name,
    #                              ACCOUNT.cert_no)
    #
    # def test_setting_find_login_password_user_binding_card(self):
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(ACCOUNT.phone_number, ACCOUNT.login_password)
    #     page.go_to_personal_center_page()
    #     page.go_to_security_center_page()
    #     page.go_to_setting_login_password_page()
    #     page.find_login_password(ACCOUNT.is_bind_card, ACCOUNT.phone_number,
    #                              ACCOUNT.login_password, ACCOUNT.user_name,
    #                              ACCOUNT.cert_no)
    #
    # def test_setting_change_login_password(self):
    #     phone_number = self.util.fake_cn.phone_number()
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.go_to_register_page()
    #     page.register(phone_number, '12qwaszx')
    #     page.shopping()
    #
    #     page.go_to_personal_center_page()
    #     page.go_to_security_center_page()
    #     page.go_to_setting_login_password_page()
    #     page.change_login_password('12qwaszx', 'a1111111')
    #
    #     self.driver.quit()
    #     self.driver = BasicController().open_android_app(self.app_path, self.platform_version)
    #     allow_button = self.driver.find_element_by_xpath(APP_ACCESS_ALLOW_BUTTON)
    #     allow_button.click()
    #
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(phone_number, 'a1111111')
    #     page.go_to_personal_center_page()
    #     page.go_to_security_center_page()
    #     page.go_to_setting_login_password_page()
    #     page.change_login_password('a1111111', 'a0000000')
    #
    # def test_setting_change_trade_password(self):
    #     phone_number = '18994455607'
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(phone_number, '12qwaszx')
    #
    #     page.go_to_personal_center_page()
    #     page.go_to_security_center_page()
    #     page.go_to_setting_trade_password_page()
    #     page.change_trade_password('147258', '135790')
    #
    #     self.driver.quit()
    #     self.driver = BasicController().open_android_app(self.app_path, self.platform_version)
    #     allow_button = self.driver.find_element_by_xpath(APP_ACCESS_ALLOW_BUTTON)
    #     allow_button.click()
    #
    #     page = MainPage(self.driver)
    #     page.go_to_home_page()
    #     page.go_to_login_page()
    #     page.login(phone_number, '12qwaszx')
    #     page.go_to_personal_center_page()
    #     page.go_to_security_center_page()
    #     page.go_to_setting_trade_password_page()
    #     page.change_trade_password('135790', '147258')

    def test_setting_change_phone_by_sms(self):
        phone_number = self.util.fake_cn.phone_number()
        phone_number2 = self.util.fake_cn.phone_number()
        page = MainPage(self.driver)
        page.go_to_home_page()
        page.go_to_login_page()
        page.go_to_register_page()
        page.register(phone_number, '12qwaszx')
        page.shopping()

        page.go_to_personal_center_page()
        page.go_to_security_center_page()
        page.go_to_setting_change_phone_page()
        page.change_phone_by_sms(phone_number, phone_number2)
        self.driver.quit()
        self.driver = BasicController().open_android_app(self.app_path, self.platform_version)
        allow_button = self.driver.find_element_by_xpath(APP_ACCESS_ALLOW_BUTTON)
        allow_button.click()

        page = MainPage(self.driver)
        page.go_to_home_page()
        page.go_to_login_page()
        page.login(phone_number2, '12qwaszx')


def suite():
    suite = unittest.TestSuite()

    # suite.addTest(MainPageTest("test_home_page_recharge"))
    # suite.addTest(MainPageTest("test_home_page_fast_withdraw"))
    # suite.addTest(MainPageTest("test_home_page_regular_withdraw"))
    # suite.addTest(MainPageTest("test_xjb_detail_page_recharge"))
    # suite.addTest(MainPageTest("test_xjb_detail_page_fast_withdraw"))
    # suite.addTest(MainPageTest("test_xjb_detail_page_regular_withdraw"))

    # suite.addTest(MainPageTest("test_register_not_binding_card"))
    # suite.addTest(MainPageTest("test_register_binding_card"))
    # suite.addTest(MainPageTest("test_register_unbundling_card"))
    # suite.addTest(MainPageTest("test_login_binding_card"))

    # suite.addTest(MainPageTest("test_personal_center_invite_friend"))
    # suite.addTest(MainPageTest("test_personal_center_share_weixin_friend"))
    # suite.addTest(MainPageTest("test_personal_center_share_weixin_circle"))
    # suite.addTest(MainPageTest("test_personal_center_share_weibo"))

    # suite.addTest(MainPageTest("test_login_page_find_login_password_user_not_binding_card"))
    # pass----
    # suite.addTest(MainPageTest("test_login_page_find_login_password_user_binding_card"))
    # pass----
    # suite.addTest(MainPageTest("test_setting_find_login_password_user_binding_card"))
    # pass----
    # suite.addTest(MainPageTest("test_setting_find_login_password_user_not_binding_card"))
    # pass----
    # suite.addTest(MainPageTest("test_setting_change_login_password"))
    # suite.addTest(MainPageTest("test_setting_change_trade_password"))
    # suite.addTest(MainPageTest("test_setting_find_trade_password"))
    # pass----
    suite.addTest(MainPageTest("test_setting_change_phone_by_sms"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    suite()
