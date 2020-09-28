# coding: utf-8


import unittest

from common.utility import Utility
from database import sgw_database_operator
from service_entities.cms_entities.main_cms_service_entity import MainCmsServiceEntity


class MainCmsServiceEntityTest(unittest.TestCase):
    class CmsInfo():
        cms_account = {
            'username': 'zengqingxiao',
            'password': '2aa4fcc456c4db9dd2a5facf4f99bed9',
        }

        product_info = {
            'productNo': 'H999139',
            'productFullName': '批量生成_139',
            'productShortName': 'PLSC_139',
            'issusdInfos_reservationEndTime': '20160910122100',  # 预约认购发起时间
            'issusdInfos_issueTime': '20161010094800',  # 认购开始时间
            'issusdInfos_dssubEndtime': '20170410094800',  # 认购结束时间
            'issusdInfos_bidTime': '20170510094800',  # 开放申购时间
            'issusdInfos_productExpiredtime': '201701110094800',  # 产品到期时间
            'issusdInfos_liquidationTime': '20171210094800',  # 清盘时间
            'productStatus': '1',  # 1为认购状态
            'hot': '1',  # 1为在热门中显示
            'confirmQualifiedInvestor': '1',  # 是否需要合格投资者, 0为否
            'onsaleFlag': '1',  # 是否上架, 1为上架
            'minSubscribeAmount': '1',  # 最低认购金额
            'minBuyAmount': '10',  # 最低申购金额
            'minRspAmount': '',  # 最低定投金额
            'minAddAmount': '100',  # 最低追加认购金额
            'maxSubscribeAmount': '10000',  # 最高认购金额
            'maxBuyAmount': '5000',  # 最高申购金额
            'minHoldAmount': '',  # 最低持有份额
            'rangeAmount': '100',  # 金额级差
            'minRedeemAmount': '100',  # 最低赎回份额
            'minConvertAmount': '',  # 最低转化金额
            'minAddSubscribe': '100',  # 最低追加申购金额
        }

        app_cache = {
            'allProductTypes': 'allProductTypes',
            'bankChannel': 'bankChannel',
            'riskTestTopic': 'riskTestTopic',
            'messageCentre': 'messageCentre',
            'helpCentre': 'helpCentre',
            'forceUpdate': 'forceUpdate',
            'categaryCode': 'categaryCode',
            'fund': 'fund',
            'productInfo': 'productInfo',
        }

    def setUp(self):
        self.util = Utility()
        self.operator = sgw_database_operator
        self.main_service_entity = MainCmsServiceEntity()
        self.r = self.CmsInfo

    def test_make_product(self):
        self.main_service_entity.login(username=self.r.cms_account['username'],
                                       password=self.r.cms_account['password'],
                                       )
        self.main_service_entity.new_product(productNo=self.r.product_info['productNo'],
                                             productFullName=self.r.product_info['productFullName'],
                                             productShortName=self.r.product_info['productShortName'],
                                             minSubscribeAmount=self.r.product_info['minSubscribeAmount'],
                                             issusdInfos_reservationEndTime=self.r.product_info[
                                                 'issusdInfos_reservationEndTime'],
                                             )
        product_id = self.main_service_entity.current_product_id
        product_ids = '["%s"]' % product_id

        self.main_service_entity.submit_product(productId=product_id)
        self.main_service_entity.check_product(productIds=product_ids)
        self.main_service_entity.update_product_channle(productid=product_id,
                                                        hot=self.r.product_info['hot'],
                                                        onsaleFlag=self.r.product_info['onsaleFlag'],
                                                        )
        self.main_service_entity.save_product_detail(productid=product_id,
                                                     productNo=self.r.product_info['productNo'],
                                                     confirmQualifiedInvestor=self.r.product_info[
                                                         'confirmQualifiedInvestor'],
                                                     )
        self.main_service_entity.add_product_quota(prodId=product_id)
        self.main_service_entity.change_product_quota(prodId=product_id)
        self.main_service_entity.change_product_count(prodId=product_id)
        self.main_service_entity.app_cache_update(code=self.r.app_cache['productInfo'])

    def test_modify_product(self):
        self.main_service_entity.login(username=self.r.cms_account['username'],
                                       password=self.r.cms_account['password'],
                                       )
        self.main_service_entity.update_product_channle(productid='H9#H999126',
                                                        onsaleFlag='test',
                                                        )

        self.main_service_entity.new_product(productNo=self.r.product_info['productNo'],
                                             productFullName=self.r.product_info['productFullName'],
                                             productShortName=self.r.product_info['productShortName'],
                                             minSubscribeAmount=self.r.product_info['minSubscribeAmount'],
                                             issusdInfos_reservationEndTime=self.r.product_info[
                                                 'issusdInfos_reservationEndTime'],
                                             )

        self.main_service_entity.app_cache_update(code=self.r.app_cache['productInfo'])


def suite():
    suite = unittest.TestSuite()

    suite.addTest(MainCmsServiceEntityTest("test_make_product"))
    # suite.addTest(MainCmsServiceEntityTest("test_modify_product"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    suite()
