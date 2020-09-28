'''
Created on Sep 29, 2014

@author: shirley.licp
'''
from common.logger import print_debug_info


class BasicAssertion():
    
    errors = list()
    checkpoint_counter = 0

    @staticmethod
    def _append_assertion_error_message(error_message):
        BasicAssertion.errors.append(error_message)
        print_debug_info(error_message)

    @staticmethod
    def _terminate_when_checkpoint_raise_exception(error_message, message_parameters=()):
        print_debug_info("Calling [_terminate_when_checkpoint_raise_exception].")
        message_parameters = (BasicAssertion.checkpoint_counter,) + message_parameters

        BasicAssertion._append_assertion_error_message(error_message % message_parameters)
        return [False, str(BasicAssertion.checkpoint_counter)]
