# coding: utf-8

import json

from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler

DOMAIN_NAME = u'10.199.101.217:8091'
URL = u'http://%s/pdcManager/doInsertProductBasecfg'
BODY_DATA = u'{}'
_BODY_DATA = ''
if BODY_DATA:
    _BODY_DATA = json.loads(BODY_DATA)
QUERY_DATA = ''
METHOD_TYPE = u'post'
CONTENT_TYPE = 'form'
REQUEST_DATA = (_BODY_DATA or QUERY_DATA)

REQUEST_HEADERS = ''
HAS_DATA_PATTERN = True

DATA_PATTERN = {
    "productid": "",
    "productNo": "H99998",
    "institutionProductCategoryCode": "H901",
    "taNo": "H9",
    "issueFacevalue": "1",
    "shareClass": "",
    "displayFundType": "",
    "ackBuyDay": "",
    "transferDays": "",
    "productFullName": "批量生成098",
    "taName": "华信资管ta",
    "currencyType": "156",
    "productRisklevel": "",
    "navFracnum": "",
    "ackRedeemDay": "",
    "deliveryDay": "",
    "productShortName": "批量生成098",
    "productType": "3",
    "shareType": "*",
    "fundType": "0",
    "navFracmode": "",
    "buyDay": "",
    "dividendDay": "",
    "minSubscribeAmount": "100",
    "minBuyAmount": "10",
    "minRspAmount": "",
    "minAddAmount": "100",
    "maxSubscribeAmount": "10000",
    "maxBuyAmount": "5000",
    "minHoldAmount": "",
    "rangeAmount": "100",
    "minRedeemAmount": "100",
    "minConvertAmount": "",
    "minAddSubscribe": "100",
    "issusdInfos": '''[{"acceptMode":"",
                         "issueTime":"20161010094800",
                         "dssubEndtime":"20170410094800",
                         "bidTime":"20170510094800",
                         "productExpiredtime":"20171110094800",
                         "liquidationTime":"20171210094800",
                         "productStatus":"4",
                         "reservationEndTime":"20160910122100"}]''',
    "allowChangeDividendWay": "",
    "dividendSettlementDay": "",
    "fundManagerCode": "",
    "ackSubscribeDate": "",
    "highWealthType": "0",
    "pageNo": "1",
    "pageSize": "100",
}


class PdcmanagerDoinsertproductbasecfgEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME):
        super(PdcmanagerDoinsertproductbasecfgEntity, self).__init__(domain_name=domain_name, url_string=URL,
                                                                     data=REQUEST_DATA, method_type=METHOD_TYPE,
                                                                     request_content_type=CONTENT_TYPE,
                                                                     request_headers=REQUEST_HEADERS,
                                                                     has_data_pattern=HAS_DATA_PATTERN)

    def _set_data_pattern(self, *args, **kwargs):
        self._current_data_pattern = DATA_PATTERN


if (__name__ == '__main__'):
    e = PdcmanagerDoinsertproductbasecfgEntity()
    # e.send_request(issusdInfos_reservationEndTime='20160910122100')
    e.send_request()
