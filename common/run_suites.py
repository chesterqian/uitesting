# -*- coding:utf-8 -*-

__author__ = 'Shirley'

import os
import sys
import re
import unittest
from lib import HTMLTestRunner
from lib.csv_handler import resource_root_path

# Add top source code path into sys path
sys.path.append(resource_root_path)

REPORT_RELATIVE_PATH = os.sep + 'report'

DEFAULT_TESTS_RELATIVE_PATH = \
    os.sep + 'unit_test' + os.sep + 'service_entities_unit_test' + os.sep + 'borrower_service_entities_unit_test'

BORROWER_TESTS_MATCH_PATTERN = r'borrower_service_entities_unit_test$'
VIP_TESTS_MATCH_PATTERN = r'lender_service_entities_unit_test$'
TECHOPS_TESTS_MATCH_PATTERN = r'techops_service_entities_unit_test$'
TEST_MODULE_MATCH_PATTERN = r'_test.py$'
TEST_MATCH_PATTERN = '*_test.py'

def create_report_dir(report_name):
    """
    Create a report dir and put the generated html report which is named report_name under the directory.
    :param report_name: it's the name of report.
    """
    report_dir = resource_root_path + REPORT_RELATIVE_PATH
    # print report_dir
    if not os.path.exists(report_dir):
        os.mkdir(report_dir)

    report_path = os.path.join(report_dir, report_name)
    return report_path

def load_tests():
    """
    Loads all tests into suites from tests path.
    """
    default_tests_path = resource_root_path + DEFAULT_TESTS_RELATIVE_PATH

    borrower_tests_match_path = [path for path in sys.argv if re.search(BORROWER_TESTS_MATCH_PATTERN, path)]
    vip_tests_match_path = [path for path in sys.argv if re.search(VIP_TESTS_MATCH_PATTERN, path)]
    techops_tests_match_path = [path for path in sys.argv if re.search(TECHOPS_TESTS_MATCH_PATTERN, path)]
    tests_match_module = [module for module in sys.argv if re.search(TEST_MODULE_MATCH_PATTERN, module)]

    loader = unittest.TestLoader()
    report_name = create_report_dir('report.html')

    if not tests_match_module:
        if borrower_tests_match_path:
            report_name = create_report_dir('borrower_report.html')
            suite = loader.discover(os.path.normpath(borrower_tests_match_path[0]), pattern=TEST_MATCH_PATTERN)
        elif vip_tests_match_path:
            report_name = create_report_dir('vip_report.html')
            suite = loader.discover(os.path.normpath(vip_tests_match_path[0]), pattern=TEST_MATCH_PATTERN)
        elif techops_tests_match_path:
            report_name = create_report_dir('techops_report.html')
            suite = loader.discover(os.path.normpath(techops_tests_match_path[0]), pattern=TEST_MATCH_PATTERN)
        else:
            suite = loader.discover(os.path.normpath(default_tests_path), pattern=TEST_MATCH_PATTERN)
    else:
        suite = unittest.TestSuite()
        for test_module in tests_match_module:
            module = test_module.split(os.sep)[-1]
            test_dir = test_module.split(os.sep + module)[0]
            suite.addTests(loader.discover(os.path.normpath(test_dir), pattern=module))

    return report_name, suite

def generate_html_report(report_name, suites):
    """
    Run all tests which is collected by load_tests function.
    :param report_name: It's used to record test runner result.
    :param suites: all collected suite by unittest loader.
    """
    with open(report_name, "w") as outfile:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title=u'API自动化测试报告',
            description=u'点融网api自动化执行情况展示'
        )
        runner.run(suites)

report, all_suite = load_tests()
generate_html_report(report, all_suite)
