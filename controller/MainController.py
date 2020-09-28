def add_to_sys_path():
    '''
    Relatively importing modules depends on
    the given command line arguments.

    Note: The source code should be put
    under path like "\root_source_code_folder".
    And also the path of test case file should
    be something like "\root_source_code_folder\robot_scripts"
    '''
    import sys, os, re

    CONCATENATION_STRING = ['']
    REG_TEST_CASE_SOURCE_PATTERN = '\Drobot_scripts(\D*\d*\D*\d?).(txt|html|robot)$'
    data_sources = [i for i in sys.argv \
                    if re.search(REG_TEST_CASE_SOURCE_PATTERN, os.path.normpath(i))]
    if data_sources:
        data_source = data_sources.pop(0)
        source_code_path = re.sub(REG_TEST_CASE_SOURCE_PATTERN, '', data_source)

        for s in CONCATENATION_STRING:
            complete_path = source_code_path + s
            sys.path.append(complete_path)


add_to_sys_path()

"All customized methods can be invoked, must and only need to refer this class,"
"and you can let this class inherit your customized controller classes so that"
"Robot Framework(R) scripts can invoke them."

from demo_page_monkey_test_controller import XjbDemoPageController
from main_page_test_controller import MainPageController

class MainController(
    XjbDemoPageController,
    MainPageController
):
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
