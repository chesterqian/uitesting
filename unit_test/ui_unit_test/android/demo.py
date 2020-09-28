import unittest

from appium import webdriver

from common.utility import Utility
from tools.mobile.controller.adb import execute_monkey_test
from ui.android.xjb.demo_page import DemoPage


class MainLoanAppServiceEntityTest(unittest.TestCase):
    def setUp(self):
        self.util = Utility()
        apk_path = 'huaxin/ui/apps/hxxjb-uat-develop-debug-1.2.0-b59.apk'
        apk_path = 'huaxin/ui/apps/ztb-product-yyb-release-1.0.0.apk'
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android'
        desired_caps['app'] = self.util.intersection_of_path(apk_path)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        # self.driver.close_app()
        pass

    def test_open_app(self):
        # page = DemoPage(self.driver)
        # page.go_to_main_page_with_new_session()
        # page.go_to_login_page()
        # page.login('17100000004', '12qwaszx')
        # execute_monkey_test(business_type=0, log_output='xjb_android_monkey_test')
        pass

    def test_open_app2(self):
        page = DemoPage(self.driver)
        page.go_to_main_page_with_new_session()
        page.go_to_login_page()
        page.login('17100000004', '12qwaszx')




