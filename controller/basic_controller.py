'''
Created on Feb 21, 2013

@author: Chester.Qian
'''

import sys
import time


from selenium.webdriver.chrome.webdriver import WebDriver as C_WebDriver
from selenium.webdriver.ie.webdriver import WebDriver as I_WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver as F_WebDriver
from selenium.webdriver.phantomjs.webdriver import WebDriver as P_WebDriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
# from appium import webdriver as app_driver

from common.global_config import Global
# from common.utility import Utility


class MyChromeWebDriver(C_WebDriver):
    set_time_out_for_element = 0

    def get(self, *args):
        super(C_WebDriver, self).get(*args)

    def find_element_by_xpath(self, *args):
        return super(C_WebDriver, self).find_element_by_xpath(*args)

    def find_elements_by_tag_name(self, *args):
        return super(C_WebDriver, self).find_elements_by_tag_name(*args)


class MyFireFoxWebDriver(F_WebDriver):
    set_time_out_for_element = 0

    def get(self, *args):
        super(F_WebDriver, self).get(*args)
        # print "sleeping after get (firefox)"
        time.sleep(5)

    def find_element_by_xpath(self, *args):
        if not self.set_time_out_for_element:
            self.set_time_out_for_element += 1
            self.implicitly_wait(10)
        return super(F_WebDriver, self).find_element_by_xpath(*args)

    def find_elements_by_tag_name(self, *args):
        self.implicitly_wait(1)
        return super(F_WebDriver, self).find_elements_by_tag_name(*args)


class MyIEWebDriver(I_WebDriver):
    set_time_out_for_element = 0

    def get(self, *args):
        super(I_WebDriver, self).get(*args)

    def find_element_by_xpath(self, *args):
        return super(I_WebDriver, self).find_element_by_xpath(*args)

    def find_elements_by_tag_name(self, *args):
        return super(I_WebDriver, self).find_elements_by_tag_name(*args)


class MyPhantomjsDriver(P_WebDriver):
    set_time_out_for_element = 0

    def get(self, *args):
        super(P_WebDriver, self).get(*args)

    def find_element_by_xpath(self, *args):
        return super(P_WebDriver, self).find_element_by_xpath(*args)

    def find_elements_by_tag_name(self, *args):
        return super(P_WebDriver, self).find_elements_by_tag_name(*args)


class BasicController:
    page_assertion_obj = None
    _main_window_handle = None
    _current_window_handle = None

    def __init__(self):
        self.web_driver = None
        self.current_page_obj = None

    def open_web_driver(self, browser):
        browser_dict = {'chrome': MyChromeWebDriver,
                        'firefox': MyFireFoxWebDriver,
                        'ie': MyIEWebDriver,
                        'phantomjs': MyPhantomjsDriver}
        self.web_driver = browser_dict[browser](executable_path='C:/Users/jqian079/Downloads/chromedriver.exe')
        # self.web_driver = browser_dict[browser](executable_path='/opt/WebDriver/bin/chromedriver')
        # self.web_driver = browser_dict[browser](executable_path='/opt/WebDriver/bin/geckodriver')
        # assert 0
        self.web_driver.maximize_window()
        self._main_window_handle = self.web_driver.current_window_handle
        self._current_window_handle = self.web_driver.current_window_handle
        return self.web_driver

    def open_android_app(self, app_path, platform_version, full_reset='false'):
        util = Utility()
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = platform_version
        self.desired_caps['deviceName'] = 'Android'
        self.desired_caps['app'] = util.intersection_of_path(app_path)
        self.desired_caps['fullReset'] = full_reset

        self.web_driver = app_driver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        return self.web_driver

    def open_ios_app(self):
        pass

    def open_app(self, app_path, platform_name, *args):
        name_map_func = {'android': self.open_android_app,
                         'ios': self.open_ios_app
                         }
        func = name_map_func[platform_name]
        func(app_path, *args)

    def switch_window_by_title(self, title):
        '''
        This method is on purpose of handle one driver with multiple windows/tabs.
        The switching identifier is @title text. If fail to switch by title, web 
        driver would stay on the focus page.
        '''
        for handle in self.web_driver.window_handles:
            self.web_driver.switch_to_window(handle)
            if str(self.web_driver.title) == title:
                self._current_window_handle = self.web_driver.current_window_handle
                break
            else:
                self._current_window_handle = None

        if self._current_window_handle == None:
            self.web_driver.switch_to_default_content()
            self._current_window_handle = self.web_driver.current_window_handle

    def switch_to_main_window(self):
        self.web_driver.switch_to_window(self._main_window_handle)
        self._current_window_handle = self._main_window_handle

    def go_back(self):
        self.web_driver.back()

    def close_web_driver(self):
        '''
        Release the opened web driver, in the meanwhile, the browser would be closed.
        '''
        self.web_driver.quit()

    def close_window(self):
        '''
        Close the current window of browser which is controlled by current web driver.
        '''
        self.web_driver.close()

    def status_should_be(self, expected_msg):
        status_msg = self.current_page_obj.status_msg
        actual_msg = status_msg.msg
        details = status_msg.details
        if not actual_msg == expected_msg:
            raise AssertionError("expected_msg to be '%s' but was '%s(details is%s)'"
                                 % (expected_msg, actual_msg, details))

    def wait_for_element_to_be_displayed(self, xpath, timeout=Global.PageTimeout.CHECK_STATUS):
        return self.current_page_obj.wait_for_element_attribute_as_specific_value(xpath, \
                                                                                  timeout=timeout)

    def wait_for_element_as_specific_attribute_value(self, xpath, \
                                                     attr_name, attr_value, timeout=Global.PageTimeout.CHECK_STATUS):
        return self.current_page_obj.wait_for_element_attribute_as_specific_value(xpath, \
                                                                                  attribute_name=attr_name,
                                                                                  attribute_value=attr_value,
                                                                                  timeout=timeout)