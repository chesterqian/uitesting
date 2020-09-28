'''
Created on Oct 8, 2014

@author: shirley.licp
'''

from common.database_assertion import DatabaseAssertion
from common.logger import print_debug_info
from controller.basic_controller import BasicController


class DatabaseAssertionController(BasicController):

    def get_column_value_in_table(self, table_name, column_name, *args, **kwargs):
    	print_debug_info("Calling [get_column_value_in_table] in %s." % (self.__class__.__name__))
    	return DatabaseAssertion.get_column_value_in_table(table_name, column_name, *args, **kwargs)