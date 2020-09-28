# coding: utf-8

import unittest
import time

from common.utility import Utility
from database import sgw_database_operator
from service_entities.har_entity_handle import HarEntityHandle
from service_entities.xjb_service_entities.main_xjbapp_service_entity import MainXjbAppServiceEntity


class MainXjbAppServiceEntityTest(unittest.TestCase):
    class XjbInfo():
        util = Utility()

        mobile = util.fake_cn.phone_number()
        login_password = 'a0000000'
        trade_password = '135790'
        card_no = '622202' + util.fake_cn.credit_card_number()
        name = 'H9TESTUAT' + str(time.time())
        certNo = util.fake_cn.create_id_card()

        account_1 = {
            'username': '15666666669',
            # login_password : a0000000
            'login_password': 'a0000000',
            # trade_password : 135790
            'trade_password': '135790',
            'bankCardId': '0000000001003120',
            'amt': '0.02',
            'bankNo': '804',
        }

        banding_card = {
            # 'bankNo': '804',
            # 'bankName': '中国银行',
            'cardNo': card_no,
            'name': name,
            'certNo': certNo,
        }

    def setUp(self):
        self.util = Utility()
        self.operator = sgw_database_operator
        self.main_service_entity = MainXjbAppServiceEntity()
        self.r = self.XjbInfo
        # print self.r.card_no
        # assert 0

    def test_register_not_binding_card(self):
        self.main_service_entity.get_mobile_code(mobile=self.util.fake_cn.phone_number())

        serial_no = self.main_service_entity.current_register_serialno
        mobile_code = self.main_service_entity.current_mobile_code

        self.main_service_entity.register_confirm(mobileCode=mobile_code,
                                                  password=self.r.login_password,
                                                  serialNo=serial_no)

    def test_register_binding_card(self):
        mobile = self.util.fake_cn.phone_number()
        self.main_service_entity.get_mobile_code(mobile=mobile)

        serial_no = self.main_service_entity.current_register_serialno
        mobile_code = self.main_service_entity.current_mobile_code

        self.main_service_entity.register_confirm(mobileCode=mobile_code,
                                                  password=self.r.login_password,
                                                  serialNo=serial_no)

        self.main_service_entity.set_trade_password(newPassword=self.r.trade_password)

        serial_no = self.main_service_entity.current_set_trade_passowrd_serialno
        card_no = self.r.banding_card['cardNo']
        name = self.r.banding_card['name']
        cert_no = self.r.banding_card['certNo']

        card_match_channel_entity = self.main_service_entity.card_match_channel(bin_no=card_no[:10])
        bank_no = card_match_channel_entity.bankChannel_bankNo
        bank_name = card_match_channel_entity.bankChannel_bankGroupName
        sms_mode = card_match_channel_entity.smsMode

        self.main_service_entity.binding_card_get_mobile_code(mobile=mobile,
                                                              serialNo=serial_no,
                                                              cardNo=card_no,
                                                              name=name,
                                                              certNo=cert_no,
                                                              smsMode=sms_mode,
                                                              bankName=bank_name,
                                                              bankNo=bank_no
                                                              )

        mobileCode = self.main_service_entity.current_mobile_code
        self.main_service_entity.binding_card_confirm(mobileCode=mobileCode,
                                                      serialNo=serial_no)

        binding_card_result = self.main_service_entity.current_binding_card_result
        cust_info_entity = self.main_service_entity.current_base_cust_info

        self.assertEqual(binding_card_result, 'Y')
        self.assertEqual(cust_info_entity.bankCardCount, '1')
        self.assertEqual(cust_info_entity.certNo, cert_no)
        self.assertEqual(cust_info_entity.mobile, mobile)
        self.assertEqual(cust_info_entity.name, name)
        self.assertEqual(cust_info_entity.isVerified, '1')
        self.assertEqual(cust_info_entity.hasTradePassword, '1')

    def test_home_page_recharge(self):
        self.main_service_entity.login(username=self.r.account_1['username'],
                                       password=self.r.account_1['login_password'])

        self.main_service_entity.recharge(bankCardId=self.r.account_1['bankCardId'],
                                          amt=self.r.account_1['amt'],
                                          bankNo=self.r.account_1['bankNo'])

        serial_no = self.main_service_entity.current_recharge_serialno

        self.main_service_entity.recharge_confirm(serialNo=serial_no,
                                                  password=self.r.account_1['trade_password'])

    def buy_product(self):
        self.main_service_entity.login(username=self.r.account_1['username'],
                                       password=self.r.account_1['login_password'])

        self.main_service_entity.purchase_product(
            productId='H9#H999137',
            payType='0',
            bankCardId='',
            amt='100',
        )

        serial_no = self.main_service_entity.current_purchase_product_serialno

        self.main_service_entity.purchase_product_confirm(serialNo=serial_no,
                                                          password=self.r.account_1['trade_password'])

    def redeem_product(self):
        self.main_service_entity.login(username=self.r.account_1['username'],
                                       password=self.r.account_1['login_password'])

        entity = self.main_service_entity.get_financial_list()

        harhandle = HarEntityHandle()
        print harhandle.get_product_id(entity, 'dataList_status', '0')


def suite():
    suite = unittest.TestSuite()
    # suite.addTest(MainXjbAppServiceEntityTest("test_register_not_binding_card"))
    # suite.addTest(MainXjbAppServiceEntityTest("test_register_binding_card"))
    # suite.addTest(MainXjbAppServiceEntityTest("test_home_page_recharge"))
    # suite.addTest(MainXjbAppServiceEntityTest("buy_product"))
    suite.addTest(MainXjbAppServiceEntityTest("redeem_product"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    suite()
