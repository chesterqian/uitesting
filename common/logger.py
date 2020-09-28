'''
Created on Mar 27, 2014

@author: Jamous.Fu
'''

from common.global_config import Global

def print_debug_info(log_message=''):
    if Global.DEBUG_LOGGER_ENABLE:
        print(">>> DEBUG INFO >>> : " + log_message)