"""
Created on Sep 21, 2013

@author: Chester.Qian
"""

import time
from functools import wraps
from selenium.common.exceptions import TimeoutException
from common.global_config import Global
from common.global_config import DOMAIN_NAME_DICT
from common.basic_assertion import BasicAssertion

DEFAULT_DEMO_DOMAIN_TAG = 'demo'

def decompose_url(func):
    """
    A decorator for url decomposing and retrieving some ids.
    It will retrieve student course id and activity_id
    both from current page url and partial url
    while the page is performing a page navigation.
    Note: All pages should derive from BasicSchoolPage to 
    access to this decorator.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        page = args[0]
        partial_url = args[1]
        page.update_node_ids_in_session(partial_url)
                
        return func(*args, **kwargs)

    return wrapper


def wait_for_page_to_load(func):
    """
    It needs time for browser to render the full page
    so that the performing action on page elements
    should be held over until the page is loaded completely
    within endurable time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        page = args[0]    
        time_sleep = Global.PageTimeout.RETRY_INTERVAL
        retry = 0

        def load_page_status():
            conditions = [getattr(page, condition) for condition
                          in Global.PageLoadingConditons.conditions if hasattr(page, condition)]

            values = []
            condition_counts = 0

            for condition in conditions:
                if condition:
                    if page.element_exists(condition, Global.PageTimeout.LOADING_CONDITION_IGNORE):
                        try:
                            values.append(getattr(page.get_element(condition), 'is_displayed')())
                            condition_counts += 1
                        except TimeoutException:
                            pass

            value = [v for v in values if v]

            if value:
                status_for_is_loaded = False
            else:
                status_for_is_loaded = True
    
            setattr(page, 'is_assumed_fully_loaded', status_for_is_loaded)

            return status_for_is_loaded

        try:
            while not (load_page_status()):
                time.sleep(time_sleep)
                retry += 1
                print("Retry times #%s after %s seconds..." % (retry, time_sleep))
                if retry > 10:
                    raise Exception("Timeout when page loading for %s!" % func.__name__)
        except AttributeError:
            pass
           
        return func(*args, **kwargs)

    return wrapper


def set_domain_name_for_global_session(function):
    """
    Add global level domain_name.

    Note: must be used for none-static cls method and
        receives tag string as the 2nd argument.
    """
    @wraps(function)
    def wrapper(*args, **kwargs):
        if len(args) == 1:
            tag = DEFAULT_DEMO_DOMAIN_TAG
        else:
            tag = args[1]

        domain_name = DOMAIN_NAME_DICT[tag]
        Global.SESSION['current_domain_name'] = domain_name

        return function(*args, **kwargs)

    return wrapper


def reset_page_load_status(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        page = args[0]
        page.is_assumed_fully_loaded = False

        return func(*args, **kwargs)

    return wrapper


def instance_counter_plus(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        # sleep 3 seconds for waiting for css attribute changes
        time.sleep(Global.PageTimeout.RETRY_INTERVAL)
        BasicAssertion.checkpoint_counter += 1

        return func(*args, **kwargs)

    return wrapper


def retry_on_exception(retry_times, exception_type):
    """
    Retry the decorated function for zero to maximal retry_times when exception_type occurs.
    Will raise exception when exceeding the maximal retry_times.
    """
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            current_retry_times = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exception_type:
                    current_retry_times += 1
                    if current_retry_times > retry_times:
                        raise
        return wrapper
    
    return deco


def add_login_cookies(func):

    @wraps(func)
    def wrapper(page, *args, **kwargs):
        func(page, *args, **kwargs)
        Global.COOKIES['cookies'] = page.web_driver.get_cookies()

    return wrapper
