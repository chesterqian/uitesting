'''
Created on Otc 31, 2013

@author: Jamous.Fu
'''

from locator.course_page_xpath import *

from common.global_config import Global
from common.logger import print_debug_info
from controller.basic_controller import BasicController


class PageAssertionController(BasicController):

    def destory_page_assertion_object(self):
        self.page_assertion_obj = None

    def element_should_be_existing(self, xpath="\\"):
        print_debug_info("Calling [element_should_be_existing].")
        return self.page_assertion_obj.is_existing(xpath, True)

    def element_should_not_be_existing(self, xpath="\\"):
        print_debug_info("Calling [element_should_not_be_existing].")
        return self.page_assertion_obj.is_existing(xpath, False)

    def elements_should_be_existing_with_expected_number(self, xpath="\\", expected_number=15):
        # 15,this default number, is the maximum number of words can be displayed on one page.
        print_debug_info("Calling[elements_should_be_existing_with_expected_number].")
        return self.page_assertion_obj.check_element_count(xpath, expected_number)

    def collect_checkpoint_error_results(self):
        print_debug_info("Calling [collect_checkpoint_error_results].")
        self.page_assertion_obj.collect_checkpoint_results()

    def text_should_be_existing(self, text):
        print_debug_info("Calling [text_should_be_existing].")
        return self.page_assertion_obj.is_text_existing(text, True)

    def text_should_not_be_existing(self, text):
        print_debug_info("Calling [text_should_not_be_existing].")
        return self.page_assertion_obj.is_text_existing(text, False)

    def current_url_should_end_with(self, partial_url):
        print_debug_info("Calling [current_url_should_end_with].")
        return self.page_assertion_obj.is_on_right_page(partial_url, True, 'endwith')

    def current_url_should_contains(self, partial_url):
        print_debug_info("Calling [current_url_should_contains].")
        return self.page_assertion_obj.is_on_right_page(partial_url, True)

    def current_url_should_not_contain(self, partial_url):
        print_debug_info("Calling [current_url_should_not_contain].")
        return self.page_assertion_obj.is_on_right_page(partial_url, False)

    def element_should_be_displayed(self, xpath="\\"):
        print_debug_info("Calling [element_should_be_displayed].")
        return self.page_assertion_obj.element_is_displayed(xpath, True)

    def element_should_not_be_displayed(self, xpath="\\"):
        print_debug_info("Calling [element_should_not_be_displayed].")
        return self.page_assertion_obj.element_is_displayed(xpath, False)

    def element_should_be_enabled(self, xpath="\\"):
        print_debug_info("Calling [element_should_be_enabled].")
        return self.page_assertion_obj.element_is_enabled(xpath, True)

    def element_should_be_disabled(self, xpath="\\"):
        print_debug_info("Calling [element_should_be_disabled].")
        return self.page_assertion_obj.element_is_enabled(xpath, False)

    def innertext_of_element_should_be(self, xpath="\\", text=""):
        print_debug_info("Calling [innertext_of_element_should_be].")
        return self.page_assertion_obj.element_is_displayed_with_text(xpath, text, True)

    def innertext_of_element_should_contain(self, xpath="\\", text=""):
        print_debug_info("Calling [innertext_of_element_should_contain].")
        return self.page_assertion_obj.element_is_displayed_with_text(xpath, text, False)

    def element_should_have_css_class_name(self, xpath="\\", css_class_name=""):
        print_debug_info("Calling [element_should_have_css_class_name].")
        return self.page_assertion_obj.element_has_css_class_name(xpath, css_class_name, True)

    def element_should_not_have_css_class_name(self, xpath="\\", css_class_name=""):
        print_debug_info("Calling [element_should_not_have_css_class_name].")
        return self.page_assertion_obj.element_has_css_class_name(xpath, css_class_name, False)

    def current_activity_navigation_status_should_be_passed(self):
        print_debug_info("Calling [current_activity_navigation_status_should_be_passed].")
        return self.page_assertion_obj.check_activity_navigator_status(True)

    def current_activity_navigation_status_should_be_normal(self):
        print_debug_info("Calling [current_activity_navigation_status_should_be_normal].")
        return self.page_assertion_obj.check_activity_navigator_status(False)

    def epaper_should_be_expanded(self):
        print_debug_info("Calling [epaper_should_be_expanded].")
        return self.page_assertion_obj.check_epaper_is_expanded(True)

    def epaper_should_not_be_expanded(self):
        print_debug_info("Calling [epaper_should_not_be_expanded].")
        return self.page_assertion_obj.check_epaper_is_expanded(False)

    def element_should_have_blurb_id(self, xpath="\\", blurb_id=""):
        print_debug_info("Calling [element_should_have_blurb_id].")
        return self.page_assertion_obj.check_element_blurb_id(xpath, blurb_id, True)

    def element_should_not_have_blurb_id(self, xpath="\\", blurb_id=""):
        print_debug_info("Calling [element_should_not_have_blurb_id].")
        return self.page_assertion_obj.check_element_blurb_id(xpath, blurb_id, False)

    def element_should_be_displayed_same_value_as_blurb_id(self, xpath="\\", blurb_id=""):
        print_debug_info("Calling [element_should_be_displayed_same_value_as_blurb_id].")
        return self.page_assertion_obj.check_element_text_by_blurb_id(xpath, blurb_id, True)

    def element_should_not_be_displayed_same_value_as_blurb_id(self, xpath="\\", blurb_id=""):
        print_debug_info("Calling [element_should_not_be_displayed_same_value_as_blurb_id].")
        return self.page_assertion_obj.check_element_text_by_blurb_id(xpath, blurb_id, False)

    def node_should_be_passed(self, course_query_string):
        print_debug_info("Calling [node_should_be_passed].")
        return self.page_assertion_obj.check_specific_node_is_passed(course_query_string, True)

    def node_should_not_be_passed(self, course_query_string):
        print_debug_info("Calling [node_should_not_be_passed].")
        return self.page_assertion_obj.check_specific_node_is_passed(course_query_string, False)

    def activity_container_normal_navigator_indexer_should_be(self, expected_indexer_string):
        print_debug_info("Calling [activity_container_normal_navigator_indexer_should_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.ACTIVITY_CONTAINER_PAGE, 'normal', expected_indexer_string, True)

    def activity_container_normal_navigator_indexer_should_not_be(self, expected_indexer_string):
        print_debug_info("Calling [activity_container_normal_navigator_indexer_should_not_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.ACTIVITY_CONTAINER_PAGE, 'normal', expected_indexer_string, False)

    def activity_container_passed_navigator_indexer_should_be(self, expected_indexer_string):
        print_debug_info("Calling [activity_container_passed_navigator_indexer_should_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.ACTIVITY_CONTAINER_PAGE, 'passed', expected_indexer_string, True)

    def activity_container_passed_navigator_indexer_should_not_be(self, expected_indexer_string):
        print_debug_info("Calling [activity_container_passed_navigator_indexer_should_not_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.ACTIVITY_CONTAINER_PAGE, 'passed', expected_indexer_string, False)

    def activity_container_summary_navigator_should_be_passed(self):
        print_debug_info("Calling [activity_container_summary_navigator_should_be_pass].")
        return self.page_assertion_obj.check_activity_container_summary_navigator_status(True)

    def activity_container_summary_navigator_should_be_normal(self):
        print_debug_info("Calling [activity_container_summary_navigator_should_not_be_pass].")
        return self.page_assertion_obj.check_activity_container_summary_navigator_status(False)

    def step_summary_normal_navigator_indexer_should_be(self, expected_indexer_string):
        print_debug_info("Calling [step_summary_normal_navigator_indexer_should_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.STEP_SUMMARY_PAGE, 'normal', expected_indexer_string, True)

    def step_summary_normal_navigator_indexer_should_not_be(self, expected_indexer_string):
        print_debug_info("Calling [step_summary_normal_navigator_indexer_should_not_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.STEP_SUMMARY_PAGE, 'normal', expected_indexer_string, False)

    def step_summary_passed_navigator_indexer_should_be(self, expected_indexer_string):
        print_debug_info("Calling [step_summary_passed_navigator_indexer_should_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.STEP_SUMMARY_PAGE, 'passed', expected_indexer_string, True)

    def step_summary_passed_navigator_indexer_should_not_be(self, expected_indexer_string):
        print_debug_info("Calling [step_summary_passed_navigator_indexer_should_not_be].")
        return self.page_assertion_obj.check_activity_navigator_status_by_page_type( \
            Global.PageType.STEP_SUMMARY_PAGE, 'passed', expected_indexer_string, False)

    def lesson_step_should_be_passed(self, step_index):
        print_debug_info("Calling [lesson_step_should_be_passed].")
        return self.page_assertion_obj.check_lesson_step_status(step_index, 'passed')

    def lesson_step_should_be_perfect(self, step_index):
        print_debug_info("Calling [lesson_step_should_be_perfect].")
        return self.page_assertion_obj.check_lesson_step_status(step_index, 'perfect')

    def lesson_step_should_be_normal(self, step_index):
        print_debug_info("Calling [lesson_step_should_be_normal].")
        return self.page_assertion_obj.check_lesson_step_status(step_index, 'normal')

    def lesson_step_index_should_be(self, step_index, index_text):
        print_debug_info("Calling [lesson_step_index_should_be].")
        return self.page_assertion_obj.element_is_displayed_with_text( \
            STEP_ITEM_INDEX_PATTERN % step_index, index_text, True)

    def lesson_step_category_should_be(self, step_index, category_text):
        print_debug_info("Calling [lesson_step_category_should_be].")
        return self.page_assertion_obj.element_is_displayed_with_text( \
            STEP_ITEM_CATEGORY_PATTERN % step_index, category_text, True)

    def lesson_step_title_should_be(self, step_index, title_text):
        print_debug_info("Calling [lesson_step_title_should_be].")
        return self.page_assertion_obj.element_is_displayed_with_text( \
            STEP_ITEM_TITLE_PATTERN % step_index, title_text, True)

    def lesson_step_should_have_start_button(self, step_index):
        print_debug_info("Calling [lesson_step_should_have_start_button].")
        return self.page_assertion_obj.element_is_displayed( \
            STEP_ITEM_START_BUTTON_PATTERN % step_index, True)

    def lesson_step_should_not_have_start_button(self, step_index):
        print_debug_info("Calling [lesson_step_should_not_have_start_button].")
        return self.page_assertion_obj.element_is_displayed( \
            STEP_ITEM_START_BUTTON_PATTERN % step_index, False)

    def lesson_step_should_have_continue_button(self, step_index):
        print_debug_info("Calling [lesson_step_should_have_continue_button].")
        return self.page_assertion_obj.element_is_displayed( \
            STEP_ITEM_CONTINUE_BUTTON_PATTERN % step_index, True)

    def lesson_step_should_not_have_continue_button(self, step_index):
        print_debug_info("Calling [lesson_step_should_not_have_continue_button].")
        return self.page_assertion_obj.element_is_displayed( \
            STEP_ITEM_CONTINUE_BUTTON_PATTERN % step_index, False)

    def unit_lesson_title_should_be(self, lesson_index, lesson_title_text):
        print_debug_info("Calling [unit_lesson_title_should_be].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'title', lesson_title_text, True)

    def unit_lesson_score_should_display(self, lesson_index, score_value):
        print_debug_info("Calling [unit_lesson_score_should_display].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'lesson_score', score_value, True)

    def unit_lesson_score_should_not_display(self, lesson_index, score_value):
        print_debug_info("Calling [unit_lesson_score_should_not_display].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'lesson_score', score_value, False)

    def unit_lesson_status_should_be_normal(self, lesson_index):
        print_debug_info("Calling [unit_lesson_status_should_be_normal].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'status', 'normal', True)

    def unit_lesson_status_should_be_passed(self, lesson_index):
        print_debug_info("Calling [unit_lesson_status_should_be_passed].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'status', 'passed', True)

    def unit_lesson_status_should_be_locked(self, lesson_index):
        print_debug_info("Calling [unit_lesson_status_should_be_locked].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'status', 'locked', True)

    def unit_lesson_status_should_not_be_locked(self, lesson_index):
        print_debug_info("Calling [unit_lesson_status_should_not_be_locked].")
        return self.page_assertion_obj.check_lesson_attribute_value(lesson_index, 'status', 'locked', False)

    def active_unit_dots_string_should_be(self, active_unit_dots_string):
        print_debug_info("Calling [active_unit_dots_string_should_be].")
        return self.page_assertion_obj.check_unit_dots_status('active', active_unit_dots_string)

    def inactive_unit_dots_string_should_be(self, inactive_unit_dots_string):
        print_debug_info("Calling [inactive_unit_dots_string_should_be].")
        return self.page_assertion_obj.check_unit_dots_status('inactive', inactive_unit_dots_string)

    def active_lesson_block_string_should_be(self, active_lesson_block_string=''):
        print_debug_info("Calling [active_lesson_block_string_should_be].")
        return self.page_assertion_obj.check_lesson_block_status('active', active_lesson_block_string)

    def inactive_lesson_block_string_should_be(self, inactive_lesson_block_string):
        print_debug_info("Calling [inactive_lesson_block_string_should_be].")
        return self.page_assertion_obj.check_lesson_block_status('inactive', inactive_lesson_block_string)