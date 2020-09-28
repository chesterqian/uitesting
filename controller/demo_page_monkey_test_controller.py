from robot.api.deco import keyword
from robot.utils.asserts import fail_unless

from basic_controller import BasicController
from test_oracle.monkey_test.monkey_test_oracle import MonkeyTestOracle
from tools.mobile.controller.adb import execute_monkey_test
from ui.android.xjb.demo_page import DemoPage as XjbDemoPage

class XjbDemoPageController(BasicController):
    
    @keyword('Set Environemt Args')
    def set_environemt_args(self, app_path, platform_name, version):
        self.open_app(app_path, platform_name, version)

    @keyword('Execute Monkey Test After Login')
    def execute_monkey_test_after_login(self, monkey_test_log_output):
        self.main_page = XjbDemoPage(self.web_driver)
        self.main_page.go_to_main_page_with_new_session()
        self.main_page.go_to_login_page()
        self.main_page.login('17100000004', '12qwaszx')

        file_path = execute_monkey_test(business_type=0, log_output=monkey_test_log_output)
        test_oracle = MonkeyTestOracle(file_path)
        fail_unless(test_oracle.is_passed)