import json

from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler

DOMAIN_NAME = u'10.199.101.217:8091'
URL = u'http://%s/pdcManager/updateProductChannle'
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
      "displayGainsType": "",
      "buyerLimitNum": "10000",
      "rushBuyTag": "",
      "clientType": "",
      "isSupportPoints": "0",
      "recommendTags": "",
      "allowBuyCancel": "0",
      "onsaleFlag": "1",
      "amplitudeTo": "",
      "rushBuyTime": "",
      "recommended": "0",
      "suspendFastRedeem": "",
      "hot": "1",
      "displayOrder": "",
      "isRedemAnytime": "0",
      "marketingTag": "",
      "supportBankPay": "1",
      "displayEstimatedCost": "",
      "rushBuyDescription": "",
      "amplitudeFrom": "",
      "fastRedeemCashratio": "",
      "productid": "H9#H99994",
      "soldOutDescription": "",
      "isArchive": "0",
      "activityEleven": "0",
      "recommendIntroduction": "",
      "onsaleStatus": "0",
      "supportFastRedeem": "",
      "redeemAnytimeDesc": "",
      "fastRedeemRate": "",
      "acceptMode": "M",
      "closePeriodPic": "",
      "onsaleTime": "20170110182200",
     }


class PdcmanagerUpdateproductchannleEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME):
        super(PdcmanagerUpdateproductchannleEntity, self).__init__(domain_name=domain_name, url_string=URL, data=REQUEST_DATA, method_type=METHOD_TYPE, request_content_type=CONTENT_TYPE, request_headers=REQUEST_HEADERS, has_data_pattern=HAS_DATA_PATTERN)

    def _set_data_pattern(self, *args, **kwargs):
      self._current_data_pattern = DATA_PATTERN
if (__name__ == '__main__'):
    e = PdcmanagerUpdateproductchannleEntity()
    e.send_request()