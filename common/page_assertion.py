'''
Created on Oct 31, 2013

@author: Jamous.Fu
'''

import re
import time

from selenium.common.exceptions import TimeoutException
from common.basic_assertion import BasicAssertion
from common.global_config import Global
from common.page_decorator import instance_counter_plus
from common.service_helper import ServiceHelper
from common.logger import print_debug_info

CURRENT_ACTIVITY_NAVIGATION_PATTERN = "//a[@data-act-id='activity!%s']"
EPAPER_CONTAINER_XPATH = "//div[@data-at-id='pnl-epaper-container']"
ERROR_MESSAGE_NOT_READY_TO_CHECK = "[Checkpoint #%s] Checkpoint isn't ready for checking."
ERROR_MESSAGE_EXCEPTION_HAPPENS = "[Checkpoint #%s] Exception happens during checking. Detail error info: [%s]"
ERROR_MESSAGE_NOT_ON_RIGHT_PAGE = "[Checkpoint #%s] You are not on %s."

def wait_for_page_ready_to_check(func):
    '''
    every assertion on the page 
    depends on the load status of the page object 
    meaning that assertion will not be adopted before
    the page object is fully loaded
    '''
    def wrapper(*args, **kwargs):
        page_assertion = args[0]
        page = page_assertion.default_page_object

        def is_page_ready():
            return page.is_assumed_fully_loaded

        if is_page_ready():
            page_assertion._is_ready_to_check = True
        else:
            page_assertion._is_ready_to_check = False

        return func(*args, **kwargs)

    return wrapper

class PageAssertion():
    _is_ready_to_check = False
    page_object_collection = {}

    def __init__(self, page):
        
        '''
        create a default page object in page_object_collection
        '''
        self.page_object_collection.update({Global.PageType.DEFAULT : page})

    @property
    def default_page_object(self):
        if self.page_object_collection.has_key(Global.PageType.DEFAULT):
            return self.page_object_collection[Global.PageType.DEFAULT]
        else:
            return None

    # Collect all errors in whole lifecycle of the page assertion instance
    def collect_checkpoint_results(self):
        print_debug_info("Calling [collect_checkpoint_results].")
        '''
        Reset assertion checkpoint index counter after statistics complate
        '''
        BasicAssertion.checkpoint_counter = 0

        if BasicAssertion.errors:
            errorMessage = ''
            for err in BasicAssertion.errors:
                errorMessage = errorMessage + err + '\n'

            '''
            Reset assertion errors after statistics complate
            '''
            BasicAssertion.errors = list()

            raise AssertionError(errorMessage)

    def update_page_object(self, object_instance):
        '''
        This method is for appending multiple page objects so that
        PageAssertion can support cross page assertion
        '''
        object_name = ''
        if str(object_instance.__class__.__name__).endswith(Global.PageType.ACTIVITY_PAGE):
            object_name = Global.PageType.ACTIVITY_PAGE
        else:
            object_name = object_instance.__class__.__name__

        '''
        Add or update page object for page_object_collection
        '''
        self.page_object_collection.update({object_name : object_instance})

        '''
        Update default page object for page_object_collection as selected page
        '''
        self.page_object_collection.update({Global.PageType.DEFAULT : object_instance})

    def remove_page_object(self, object_name):
        '''
        Remove idle page object
        '''
        if self.page_object_collection.has_key(object_name):
            self.page_object_collection.pop(object_name)

    def get_page_object(self, object_name=Global.PageType.DEFAULT):
        if self.page_object_collection.has_key(object_name):
            return self.page_object_collection[object_name]

        return None

    def _check_element_visibility(self, xpath, element=None):
        print_debug_info("Calling [_check_element_visibility].")
        if not element:
            element = self.get_page_object().get_element(xpath, Global.PageTimeout.QUICK_IGNORE)

        if not element.is_displayed():
            BasicAssertion._append_assertion_error_message(\
                "[Checkpoint #%s] Element ['%s'] not displayed when checking visibility." % \
            (BasicAssertion.checkpoint_counter, xpath))
            
            return False
        else:
            return True  
        
    # Verify whether an element is existing or not
    # @xpath is a XPATH formatted string
    # @result_should_be_true is a boolean value, existing mean True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def is_existing(self, xpath, result_should_be_true):
        print_debug_info("Calling [is_existing].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            actual_result = self.get_page_object().element_exists(xpath, \
                Global.PageTimeout.QUICK_IGNORE)

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] not found." % (BasicAssertion.checkpoint_counter, xpath))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] found." % (BasicAssertion.checkpoint_counter, xpath))
            
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Return actual URL while the checkpoint performs
    # @expected_partial_url is a string which is part of URL
    # @result_should_be_true is a boolean value, contain the expected url means True
    # @pattern is a string which can be contains or endswith
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def is_on_right_page(self, expected_partial_url, result_should_be_true, pattern='contains'):
        print_debug_info("Calling [is_on_right_page].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            current_url = self.get_page_object().current_url
            actual_result = False
            if pattern == 'endwith':
                actual_result = current_url.endswith(expected_partial_url)
            else:
                actual_result = current_url.find(expected_partial_url) >= 0

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Isn't on the right page. Expected URL should contains '%s', but current URL is %s." \
                        % (BasicAssertion.checkpoint_counter, expected_partial_url, current_url))
                else:
                    BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Isn't on the right page. Expected URL should not contain '%s', but current URL is %s." \
                        % (BasicAssertion.checkpoint_counter, expected_partial_url, current_url))
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether a text is existing on current page or not
    # @text is a string
    # @result_should_be_true is a boolean value, text existing mean True 
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def is_text_existing(self, text, result_should_be_true):
        print_debug_info("Calling [is_text_existing].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            # xpath here is just a search pattern for getting all text on the page combined as a string
            xpath = "//*[contains(., '')]"

            try:
                actual_result = self.get_page_object().get_element_text(xpath).replace('\n', ' ').find(text) >= 0
            except TimeoutException:
                actual_result = False

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Text ['%s'] not found." % (BasicAssertion.checkpoint_counter, text))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Text ['%s'] found." % (BasicAssertion.checkpoint_counter, text))
            
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether an element is displayed or not
    # @xpath is a XPATH formatted string
    # @result_should_be_true is a boolean value, existing means True
    @instance_counter_plus
    @wait_for_page_ready_to_check 
    def element_is_displayed(self, xpath, result_should_be_true):
        print_debug_info("Calling [element_is_displayed].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)
        try:
            try:
                if self.get_page_object().element_exists(xpath, Global.PageTimeout.QUICK_IGNORE):
                    actual_result = self.get_page_object().get_element(xpath, Global.PageTimeout.QUICK_IGNORE)\
                        .is_displayed()
                else:
                    actual_result = False
            except TimeoutException:
                actual_result = False

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] not displayed." % (BasicAssertion.checkpoint_counter, xpath))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] displayed." % (BasicAssertion.checkpoint_counter, xpath))
            
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether the certain scope number of same elements are existing on the target page or not.
    # @xpath is a XPATH formatted string
    # @result_should_be_true is a boolean value, existing means True
    @instance_counter_plus
    @wait_for_page_ready_to_check 
    def check_element_count(self, xpath, expected_number):
        print_debug_info("Calling [check_element_count].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            element_count = 0
            try:
                elements = self.get_page_object().get_elements(xpath)
                if elements:
                    element_count = len(elements)
                    actual_result = element_count == expected_number
                else:
                    actual_result = False
            except TimeoutException:
                actual_result = False

            if actual_result == False:
                BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] The actual number of elements ['%s'] is [%s]; the expected number is [%s]." \
                    % (BasicAssertion.checkpoint_counter, xpath, str(element_count), str(expected_number)))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether an element is enabled or not
    # @xpath is a XPATH formatted string
    # @result_should_be_true is a boolean value, enabled means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def element_is_enabled(self, xpath, result_should_be_true):
        print_debug_info("Calling [element_is_enabled].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            element = self.get_page_object().get_element(xpath, Global.PageTimeout.QUICK_IGNORE)

            is_visible = self._check_element_visibility(xpath, element)
            if not is_visible:
                return [False, str(BasicAssertion.checkpoint_counter)]

            value = self.get_page_object().get_element_attribute_value_by_name(xpath, 'class')
            pattern = Global.WebElementStatus.REG_DISABLED

            if re.search(pattern, value) or not element.is_enabled():
                actual_result = False
            else:
                actual_result = True

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] disabled." % (BasicAssertion.checkpoint_counter, xpath))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] enabled." % (BasicAssertion.checkpoint_counter, xpath))
            
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether an element is displayed with expected text
    # @xpath is a XPATH formatted string
    # @expected_text is a string
    # @exact_match is a boolean value, exact match means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def element_is_displayed_with_text(self, xpath, expected_text, exact_match):
        print_debug_info("Calling [element_is_displayed_with_text].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            element = self.get_page_object().get_element(xpath, Global.PageTimeout.QUICK_IGNORE)

            is_visible = self._check_element_visibility(xpath, element)
            if not is_visible:
                return [False, str(BasicAssertion.checkpoint_counter)]

            actual_text = element.text
            if exact_match:
                actual_result = (expected_text == actual_text)            
            else:
                try:
                    actual_result = actual_text.find(expected_text) >= 0
                except TimeoutException:
                    actual_result = False
                
            if not actual_result:
                BasicAssertion._append_assertion_error_message(\
                "[Checkpoint #%s] Element ['%s'] should display ['%s'], but actually displays ['%s']."\
                                   % (BasicAssertion.checkpoint_counter, xpath, expected_text, actual_text))
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether an element has an expected CSS class name
    # @xpath is a XPATH formatted string
    # @css_class_name is a string
    # @result_should_be_true is a boolean value, having the CSS name means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def element_has_css_class_name(self, xpath, css_class_name, result_should_be_true):
        print_debug_info("Calling [element_has_css_class_name].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            actual_result = self.get_page_object().get_element(xpath, Global.PageTimeout.QUICK_IGNORE) \
                .get_attribute('class').find(css_class_name) >= 0

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] doesn't have CSS class ['%s']." % \
                    (BasicAssertion.checkpoint_counter, xpath, css_class_name))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] has an unexpected CSS class ['%s']." % \
                    (BasicAssertion.checkpoint_counter, xpath, css_class_name))
            
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether an element has a specific blurb id
    # @xpath is a XPATH formatted string
    # @blurb_id is a string
    # @result_should_be_true is a boolean value, having the blurb id means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_element_blurb_id(self, xpath, blurb_id, result_should_be_true):
        print_debug_info("Calling [check_element_blurb_id].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            actual_blurb_id = self.get_page_object().get_element(xpath, Global.PageTimeout.QUICK_IGNORE)\
                .get_attribute('data-blurb-id')
            actual_result = actual_blurb_id == blurb_id

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] doesn't have blurb id ['%s'], actually it's ['%s']." % \
                    (BasicAssertion.checkpoint_counter, xpath, blurb_id, actual_blurb_id))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] has an unexpected blurb id ['%s']." % \
                    (BasicAssertion.checkpoint_counter, xpath, blurb_id))
            
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether an element is displayed with expected text of a specific blurb id
    # @xpath is a XPATH formatted string
    # @blurb_id is a string
    # @result_should_be_true is a boolean value, having the blurb id means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_element_text_by_blurb_id(self, xpath, blurb_id, result_should_be_true):
        print_debug_info("Calling [check_element_text_by_blurb_id].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            expected_text = ServiceHelper.get_blurb_translation(blurb_id)
            actual_text = self.get_page_object().get_element_text(xpath)
            actual_result = actual_text == expected_text

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Element ['%s'] should display ['%s'], but actually displays ['%s']."\
                    % (BasicAssertion.checkpoint_counter, xpath, expected_text, actual_text))
                else:
                    BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Element ['%s'] displays an unexpected text['%s']."\
                    % (BasicAssertion.checkpoint_counter, xpath, expected_text))
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify the status of current activity navigation balloon   
    # @result_should_be_true is a boolean value, expecting passed status means True
    @instance_counter_plus
    @wait_for_page_ready_to_check 
    def check_activity_navigator_status(self, result_should_be_true):
        print_debug_info("Calling [check_activity_navigator_status].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)
        
        def load_activity_navigator_status():
            #search for the presence of a passed pattern
            match = re.search(Global.WebElementStatus.REG_PASSED, \
                element_parent_of_current_navigation_balloon.get_attribute('class'))
            if (result_should_be_true and match) or (not result_should_be_true and not match):
                return True
            else:
                return False

        try:
            page_object = self.get_page_object(Global.PageType.ACTIVITY_PAGE)
            if page_object:
                activity_id = page_object.activity.activity_id

                element_current_navigation_balloon = page_object.get_element(\
                    CURRENT_ACTIVITY_NAVIGATION_PATTERN % activity_id, Global.PageTimeout.QUICK_IGNORE)

                element_parent_of_current_navigation_balloon = \
                    element_current_navigation_balloon.find_element_by_xpath("..")

                actual_result = result_should_be_true
                
                retry = 0
                while not load_activity_navigator_status():
                    time.sleep(Global.PageTimeout.RETRY_INTERVAL)
                    retry += 1
                    print "Retry times #%s for checking status of activity navigator after %s seconds..." \
                        % (retry, Global.PageTimeout.RETRY_INTERVAL)
                
                    if retry > Global.RetryTimes.MAX:
                        actual_result = not result_should_be_true
                        break

                if actual_result != result_should_be_true:
                    if result_should_be_true:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Activity Navigation State is [Normal]." % (BasicAssertion.checkpoint_counter))
                    else:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Activity Navigation State is [Passed]." % (BasicAssertion.checkpoint_counter))
            
                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, Global.PageType.ACTIVITY_PAGE))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify epaper whether is expanded or not
    # @result_should_be_true is a boolean value, expecting expanded status means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_epaper_is_expanded(self, result_should_be_true):
        print_debug_info("Calling [check_epaper_is_expanded].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            if re.search(Global.WebElementStatus.REG_EXPANDED,\
                self.get_page_object().get_element_attribute_value_by_name(EPAPER_CONTAINER_XPATH, 'class')):
                actual_result = True
            else:
                actual_result = False

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] ePaper is [Not expanded]." % (BasicAssertion.checkpoint_counter))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] ePaper is [Expanded]." % (BasicAssertion.checkpoint_counter))

                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify specific node is passed or not
    # @node_type is enum value of CourseTree
    # @node_id is string value, level id or unit id or other node type id
    # @result_should_be_true is a boolean value, node passed means True
    @instance_counter_plus
    def check_specific_node_is_passed(self, course_query_string, result_should_be_true):
        print_debug_info("Calling [check_specific_node_is_passed].")

        try:
            actual_result = ServiceHelper.get_course_structure_state(Global.COOKIES['cookies'], \
                course_query_string)

            if actual_result != result_should_be_true:
                if result_should_be_true:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] '%s' should be passed."\
                    % (BasicAssertion.checkpoint_counter, course_query_string))
                else:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] '%s' should be not passed."\
                    % (BasicAssertion.checkpoint_counter, course_query_string))
                return [False, str(BasicAssertion.checkpoint_counter)]
            else:
                return [True, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether provided activity indexes with expected status
    # @page_type is a string ONLY can be Global.PageType.ACTIVITY_CONTAINER_PAGE
    #   and Global.PageType.STEP_SUMMARY_PAGE
    # @status is a string include normal and passed values
    # @expected_indexer_string is a '1,2,3' formatted string
    # @result_should_be_true is a boolean value, @indexer_string activities match @status means True
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_activity_navigator_status_by_page_type(self, page_type, status, \
        expected_indexer_string, result_should_be_true):
        print_debug_info("Calling [check_activity_container_activity_navigator_status].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            page_object = self.get_page_object(page_type)
            if page_object:
                actual_indexer_string = page_object.get_activity_index_string_by_status(status)
                actual_result = actual_indexer_string == expected_indexer_string

                if actual_result != result_should_be_true:
                    if result_should_be_true:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Not all activity [%s] are [%s]."\
                        % (BasicAssertion.checkpoint_counter, expected_indexer_string, status))
                    else:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Activity [%s] are [%s]."\
                        % (BasicAssertion.checkpoint_counter, expected_indexer_string, status))
                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, page_type))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify whether summary navigator is passed or not
    # @result_should_be_true is a boolean value, True means result should be equal with expected
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_activity_container_summary_navigator_status(self, result_should_be_true):
        print_debug_info("Calling [check_activity_container_summary_navigator_status].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            page_object = self.get_page_object(Global.PageType.LESSON_PAGE)
            if page_object:
                actual_result = page_object.get_summary_navigator_status()

                if actual_result != result_should_be_true:
                    if result_should_be_true:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Summary navigator status is ['Normal']."\
                        % (BasicAssertion.checkpoint_counter))
                    else:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Summary navigator status is ['Passed']."\
                        % (BasicAssertion.checkpoint_counter))
                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, \
                    Global.PageType.ACTIVITY_CONTAINER_PAGE))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify the status of step on lesson page
    # @step_index is the index of the step on lesson page
    # @expected_status is a string value including passed, normal and perfect
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_lesson_step_status(self, step_index, expected_status):
        print_debug_info("Calling [check_lesson_step_status].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            page_object = self.get_page_object(Global.PageType.LESSON_PAGE)
            if page_object:
                actual_result = page_object.get_step_status_by_step_index(step_index)

                if actual_result != expected_status:
                    BasicAssertion._append_assertion_error_message(\
                    "[Checkpoint #%s] Step status is ['%s'] actually, and expected status is ['%s']."\
                    % (BasicAssertion.checkpoint_counter, actual_result, expected_status))
                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, \
                    Global.PageType.LESSON_PAGE))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify attributes on lesson page
    # @lesson_index is the index of the lesson on unit page
    # @attribute_name is a string value which could be any attributes of lesson page object
    # @expected_attribute_value is a string value of provided attribute name
    # @result_should_be_true is a boolean value, True means result should be equal with expected
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_lesson_attribute_value(self, lesson_index, attribute_name, \
        expected_attribute_value, result_should_be_true):
        print_debug_info("Calling [check_lesson_attribute_value].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            page_object = self.get_page_object(Global.PageType.UNIT_PAGE)
            if page_object:
                actual_attribute_value = str(getattr(page_object.lesson_page_objects[int(lesson_index) - 1], \
                    attribute_name))
                actual_result = actual_attribute_value == expected_attribute_value

                if actual_result != result_should_be_true:
                    if result_should_be_true:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Lesson #%s's %s is ['%s'] actually, but expecting is ['%s']." \
                        % (BasicAssertion.checkpoint_counter, lesson_index, attribute_name, \
                        actual_attribute_value, expected_attribute_value))
                    else:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Lesson #%s's %s is ['%s'] actually, but expecting is not ['%s']." \
                        % (BasicAssertion.checkpoint_counter, lesson_index, attribute_name, \
                        actual_attribute_value, expected_attribute_value))
                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, \
                    Global.PageType.UNIT_PAGE))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify unit dots status
    # @status is a string include active and inactive
    # @expected_status_string is a '1,2,3' formatted string
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_unit_dots_status(self, status, expected_status_string):
        print_debug_info("Calling [check_unit_dots_status].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            page_object = self.get_page_object(Global.PageType.LEVEL_PAGE)
            if page_object:
                actual_result = page_object.get_unit_dots_string_by_status(status)

                if actual_result != expected_status_string:
                    if status == 'active':
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Active unit dots index string is [%s], but expecting is [%s]."\
                        % (BasicAssertion.checkpoint_counter, actual_result, expected_status_string))
                    else:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Inactive unit dots index string is [%s], but expecting is [%s]."\
                        % (BasicAssertion.checkpoint_counter, actual_result, expected_status_string))

                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, \
                    Global.PageType.LEVEL_PAGE))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))

    # Verify lesson block status
    # @status is a string include active and inactive
    # @expected_status_string is a '1,2,3' formatted string
    @instance_counter_plus
    @wait_for_page_ready_to_check
    def check_lesson_block_status(self, status, expected_status_string):
        print_debug_info("Calling [check_lesson_block_status].")
        if not self._is_ready_to_check:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_NOT_READY_TO_CHECK)

        try:
            page_object = self.get_page_object(Global.PageType.UNIT_PAGE)
            if page_object:
                actual_result = page_object.get_lesson_block_view_string_by_status(status)

                if actual_result != expected_status_string:
                    if status == 'active':
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Active lesson index string is [%s], but expecting is [%s]."\
                        % (BasicAssertion.checkpoint_counter, actual_result, expected_status_string))
                    else:
                        BasicAssertion._append_assertion_error_message(\
                        "[Checkpoint #%s] Inactive lesson index string is [%s], but expecting is [%s]."\
                        % (BasicAssertion.checkpoint_counter, actual_result, expected_status_string))

                    return [False, str(BasicAssertion.checkpoint_counter)]
                else:
                    return [True, str(BasicAssertion.checkpoint_counter)]
            else:
                BasicAssertion._append_assertion_error_message( \
                    ERROR_MESSAGE_NOT_ON_RIGHT_PAGE % (BasicAssertion.checkpoint_counter, \
                    Global.PageType.UNIT_PAGE))
                return [False, str(BasicAssertion.checkpoint_counter)]

        except Exception, e:
            return BasicAssertion._terminate_when_checkpoint_raise_exception( \
                ERROR_MESSAGE_EXCEPTION_HAPPENS, (str(e),))