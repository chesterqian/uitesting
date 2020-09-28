# -*- coding:utf-8 -*-

__author__ = 'Shirley'

import random
import string
import uuid

class RandomObject(object):
    @staticmethod
    def create_random_username():
        return 'python-' + str(uuid.uuid1())

    @staticmethod
    def create_random_chinese_username():
        chinese_dict = {
            '0': u'借', '1': u'款', '2': u'中', '3': u'国', '4': u'点',
            '5': u'融', '6': u'网', '7': u'投', '8': u'资', '9': u'列',
            '10': u'表', '11': u'团', '12': u'团', '13': u'赚', '14': u'债',
            '15': u'权', '16': u'转', '17': u'让', '18': u'申', '19': u'请',
            '20': u'华', '21': u'人', '22': u'民', '23': u'共', '24': u'和'}
        key_1, key_2 = [str(random.randint(0, chinese_dict.__len__() - 1)),
                        str(random.randint(0, chinese_dict.__len__() - 1))]
        return chinese_dict[key_1] + chinese_dict[key_2] + str(random.randint(0, 99))

    @staticmethod
    def create_random_email(username):
        return username + '@sl.com'

    @staticmethod
    def create_random_string(length):
        """
        create arbitrary length of password which is composed of numbers and chars.
        """
        number_length = random.randrange(1, length)
        char_length = length - number_length
        random_list = []
        random_list.extend([random.choice(string.digits) for i in range(1, number_length + 1)])
        random_list.extend([random.choice(string.ascii_letters) for i in range(1, char_length + 1)])
        random.shuffle(random_list)
        return ''.join(random_list)

    @staticmethod
    def get_random_choice(param):
        """
        get a random choice from a list of param.
        """
        return random.choice(param)

    @staticmethod
    def create_random_phone():
        phone_prefix = ['13', '14', '15', '17', '18']
        random_phone_prefix = random.choice(phone_prefix)
        return random_phone_prefix + ''.join([random.choice(string.digits) for i in range(1, 10)])

    @staticmethod
    def create_random_float_number():
        """
        return a float number which just keeps two decimal.
        """
        return round(random.uniform(0, 1), 2)

    @staticmethod
    def create_mobile_username():
        return 'mobile-' + str(random.randrange(100000))

    @staticmethod
    def create_random_mobile_email(mobile_name):
        return mobile_name + '@163.com'
