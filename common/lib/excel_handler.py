# coding: utf-8
import random
import time

import xlwt

from common.utility import Utility


class Excel_Handler():

    def __init__(self):
        self.util = Utility()

    def createSalary(self):
        integer = random.randint(8000, 12000)
        decimal = random.randint(0, 99)
        num = str(integer) + '.' + str(decimal)
        return num

    def createBankCard(self):

        # 招商银行借记卡16位,交通银行借记卡17位,其他借记卡19位
        bank_card = {'621785': 'BOC',
                     # '103000': '农业银行',
                     # '415599': '民生银行',
                     # '402791': '工商银行',
                     # '421437': '中信银行',
                     }

        num_1 = ''
        num_2 = ''
        chars = '1234567890'
        length = len(chars) - 1
        for j in range(11):
            num_1 += chars[random.randint(0, length)]
        bank_no = random.choice(list(bank_card.keys()))
        num_2 += bank_no + num_1 + '-' + bank_card[bank_no]
        return num_2

    def excel_write(self):
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet('test')
        i = 0
        while (i < 1000):
            i = i + 1

            sheet.write(i, 0, self.util.fake_cn.name_male())
            sheet.write(i, 1, self.util.fake_cn.phone_number())
            sheet.write(i, 2, self.util.fake_cn.create_id_card())
            sheet.write(i, 3, self.createBankCard().split('-')[0])
            sheet.write(i, 4, self.createBankCard().split('-')[1])
            sheet.write(i, 5, self.createSalary())
            workbook.save('/Users/linkinpark/Desktop/jgdf333')

    def test(self):
        # print self.util.fake_cn.phone_number()
        # print self.util.fake_cn.create_id_card()
        # # print self.util.fake_cn.name_male()
        # print 'H9TESTUAT'+str(time.time())
        print self.createBankCard().split('-')[0]
        # print self.createSalary()


if __name__ == '__main__':
    eh = Excel_Handler()
    # eh.test()
    eh.excel_write()
