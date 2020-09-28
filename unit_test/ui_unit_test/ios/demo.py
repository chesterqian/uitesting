import unittest

from appium import webdriver

from common.utility import Utility
from tools.mobile.controller.adb import execute_monkey_test
from ui.android.xjb.main_page import MainPage


class MainLoanAppServiceEntityTest(unittest.TestCase):
    def setUp(self):
        self.util = Utility()
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['deviceName'] = 'iPhone 6s Plus'
        desired_caps['app'] = '/Users/linkinpark/Downloads/HXXjb_1.4.1_M525.ipa'
        desired_caps['automationName'] = 'XCUITest'
        desired_caps['platformVersion'] = '9.3'
        # desired_caps['udid'] = '56a36d750ab8d2c6e5b73365099bdbf7bc05d9d2'
        desired_caps['fullReset'] = 'true'
        # desired_caps['xcodeConfigFile'] = '/Users/linkinpark/Documents/xcodeConfigFile.xcconfig'
        # desired_caps['app'] = self.util.intersection_of_path(app_path)
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def test_open_app(self):
        page = MainPage(self.driver)
        page.go_to_main_page_with_new_session()
        page.go_to_login_page()
        page.login('17100000004', '12qwaszx')




