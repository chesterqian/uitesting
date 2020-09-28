__author__ = 'Shirley'

import functools
import csv
import os
import re
import inspect
import random
import codecs
from collections import namedtuple

RELATIVE_TEST_DATA_PATH = os.sep + 'resources'


def get_resource_root_path():
    """
    get top source code path.
    It bases on your project directory.It's divided by 'dianrong'.
    """
    string_separator = 'dianrong'
    # string_separator = 'dianrong_dev/automation/dianrong'
    current_module_path = inspect.getmodule(get_resource_root_path).__file__
    init_path = re.split(string_separator, current_module_path)[0]
    resource_path = os.path.normpath(os.path.join(init_path, string_separator))
    return resource_path

resource_root_path = get_resource_root_path()


def find_file(start, name):
    """
    It finds the file based on top directory.
    :param start: The top directory of search path.
    :param name: The searched file's name.
    :return: absolute path of searched file.
    """
    for rel_path, dirs, files in os.walk(start):
        if name in files:
            full_path = os.path.join(start, rel_path, name)
            return os.path.normpath(os.path.abspath(full_path))
    else:
        raise Exception("No such file %s under the directory %s" % (name, start))


class CsvData(object):

    def __init__(self, func=None):
        self.func = func

    def __call__(self, *args):
        current_func_name = self.func.__name__
        current_cls_name = str(args[0]).split('.')[1].split(')')[0]
        file_name = current_cls_name + '.' + current_func_name + '.csv'

        start_dir = os.path.normpath(resource_root_path + RELATIVE_TEST_DATA_PATH)
        found_file = find_file(start_dir, file_name)

        resource_data = self.get_content_from_csv(found_file)
        return self.func(args[0], resource_data)

    def __get__(self, obj, obj_type):
        return functools.partial(self.__call__, obj)

    @staticmethod
    def get_content_from_csv(file_name):
        """
        The function is used to get csv content.
        It distinguishes the number of rows in csv content.
        If the row of content is bigger than one except csv header,we get the random row.If one,we get the current one.
        """
        with codecs.open(file_name, 'r') as f_csv:
            csv_content = csv.reader(f_csv)
            csv_header = next(csv_content)
            data = namedtuple('Data', csv_header)
            csv_list = []
            for r in csv_content:
                csv_list.append(r)

            if len(csv_list) == 1:
                return data(*csv_list.pop())
            elif len(csv_list) > 1:
                row = random.choice(csv_list)
                return data(*row)
            else:
                raise Exception("The csv file is empty and please input the required parameters.")
