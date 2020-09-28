'''
Created on Aug 8, 2013

@author: Chester.Qian
'''
ERROR_MESSAGE_DESTINATION_PAGE_NAVIGATION = "Error occurred when going to page %s"
ERROR_MESSAGE_QUESTION_NAVIGATION = "Error occurred when going to question number which is %s"
ERROR_MESSAGE_ACTIVITY_NAVIGATION = "Error occurred when going to activity page whose id is %s"
ERROR_MESSAGE_COURSE_NAVIGATION = "Error occurred when going to course page"
ERROR_MESSAGE_NOT_SHOWN = "element not shown on the page, xpath:%s"

class PageExceptionType:
    ELEMENT_NOT_EXIST = 1
    PAGE_NAVIGATION_ERROR = 2
    QUESTION_NAVIGATION_ERROR = 3

class BasicPageException(Exception):
    # types of exception:
    # 1.element exists exception
    # 2.page navigation exception
    exception_type = None

    def __init__(self, page_object):
        self.page_object = page_object
        self.error_message = None

    def __str__(self):
        exception_msg = "Message: %s " % repr(self.error_message)
        return exception_msg
    
    def add_error_message(self, error_message):
        self.error_message = error_message

    def handle_exception(self):
        raise (NotImplementedError, "Should be implemented")

class BasicActivityPageException(BasicPageException):

    def __init__(self, page_object):
        '''
        Some activities(e.g.MatchingActivityPage,TypingActivityPage)
        have a feature that it randomly and selectively shows questions and answer element
        on page object from raw content which means if the expected element didn't show on
        the page then the page should raise its own type of exception to handle such circumstances
        as a kind of work around for testablily issues.
        '''        
        super(BasicActivityPageException, self).__init__(page_object)

        activity = self.page_object.activity
        self.number_of_questions_from_content = len(activity.questions)
        self.number_of_questions_in_runtime = activity.filtered_question_number

        self.length_difference = abs(cmp(self.number_of_questions_from_content, \
                                    self.number_of_questions_in_runtime))

    def handle_exception(self):
        # handle business level exception
        error_message = ERROR_MESSAGE_NOT_SHOWN%\
                                self.page_object.current_xpath_on_error

        if self.length_difference == 0:
            self.add_error_message(error_message)
            raise 

        self.number_of_questions_from_content -= 1
        if self.number_of_questions_from_content < \
            self.number_of_questions_in_runtime:
            self.add_error_message(error_message)
            raise
            
        pass

class MatchingActivityPageException(BasicActivityPageException):
    exception_type = PageExceptionType.ELEMENT_NOT_EXIST
    handled_times = 0

    def __init__(self, page_object):
        super(MatchingActivityPageException, self).__init__(page_object)

        self.error_message = ERROR_MESSAGE_NOT_SHOWN % \
            self.page_object.current_xpath_on_error

    def handle_exception(self, total_number_of_questions, number_of_questions_left):
        if self.page_object.activity.filtered_question_number > 5:
            self.handled_times += 1
            if self.handled_times > total_number_of_questions:
                raise    
        else:
            super(MatchingActivityPageException, self).handle_exception()

class TypingActivityPageException(BasicActivityPageException):
    exception_type = PageExceptionType.ELEMENT_NOT_EXIST

class SequencingActivityPageException(BasicActivityPageException):
    exception_type = PageExceptionType.ELEMENT_NOT_EXIST
    
    def __init__(self, page_object):
        super(SequencingActivityPageException, self).__init__(page_object)

        self.error_message = ERROR_MESSAGE_NOT_SHOWN % \
            self.page_object.current_xpath_on_error

        self.left_question_number = len(self.page_object.scoring_logic)

    def handle_exception(self):
        error_message = self.error_message

        if not self.left_question_number == len(self.page_object.scoring_logic):
            self.number_of_questions_from_content = len(self.page_object.scoring_logic)
            self.left_question_number = self.number_of_questions_from_content

        self.number_of_questions_from_content -= 1

        if self.number_of_questions_from_content == 0:
            self.add_error_message(error_message)
            raise
            
        pass

class GoToDestinationPageException(BasicPageException):
    exception_type = PageExceptionType.PAGE_NAVIGATION_ERROR
    
    def __init__(self, from_page_object, to_page_object):
        self.error_message = ERROR_MESSAGE_DESTINATION_PAGE_NAVIGATION % to_page_object.__class__.__name__
            
class GoToActivityPageException(BasicPageException):
    exception_type = PageExceptionType.PAGE_NAVIGATION_ERROR

    def __init__(self, from_page_object, to_page_object):
        super(GoToActivityPageException, self).__init__(from_page_object)

        self.error_message = ERROR_MESSAGE_ACTIVITY_NAVIGATION % \
            to_page_object.activity.activity_id
        self.from_page_object = from_page_object
        self.to_page_object = to_page_object

    def handle_exception(self):
        self.from_page_object.web_driver.get(self.from_page_object.destination_url)
        self.from_page_object.check_destination_page(self.to_page_object)

class GoToNextQuestionException(BasicPageException):
    exception_type = PageExceptionType.QUESTION_NAVIGATION_ERROR

    def __init__(self, from_page, expect_question_id):
        self.error_message = ERROR_MESSAGE_QUESTION_NAVIGATION % \
            expect_question_id
        self.from_page = from_page

    def handle_exception(self):
        self.add_error_message(self.error_message)
        self.from_page.check_question_index()
        
class GoToCoursePageException(BasicPageException):
    exception_type = PageExceptionType.PAGE_NAVIGATION_ERROR

    def __init__(self, from_page_object, to_page_object):
        super(GoToCoursePageException, self).__init__(from_page_object)

        self.error_message = ERROR_MESSAGE_COURSE_NAVIGATION
        self.from_page_object = from_page_object
        self.to_page_object = to_page_object

    def handle_exception(self):
        self.from_page_object.web_driver.get(self.from_page_object.destination_url)
        self.from_page_object.check_destination_page(self.to_page_object)