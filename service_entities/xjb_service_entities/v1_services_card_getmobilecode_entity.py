# coding: utf-8

import json
from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler
from common.global_config import Global

DOMAIN_NAME = u'10.199.101.211:18088'
URL = u'http://%s//V1/services/card/getMobileCode'
BODY_DATA = u'{}'
_BODY_DATA = ''
if BODY_DATA:
    _BODY_DATA = json.loads(BODY_DATA)
QUERY_DATA = ''
METHOD_TYPE = u'post'
CONTENT_TYPE = 'json'
REQUEST_DATA = (_BODY_DATA or QUERY_DATA)
HAS_DATA_PATTERN = True

DATA_PATTERN = {"mobile": "14737081792",
                "serialNo": "",
                "smsMode": "N",
                "bankNo": "804",
                "bankName": "中国银行",
                "cardNo": "62178549614637810",
                "name": "H9TESTUAT1484636220.6",
                "certNo": "350625194504125834",
                "appKind": "8",
                "certType": "0",
                "accptMode": "M"}


class V1ServicesCardGetmobilecodeEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME, token=None, **kwargs):
        super(V1ServicesCardGetmobilecodeEntity, self).__init__(domain_name=domain_name, url_string=URL,
                                                                data=REQUEST_DATA, method_type=METHOD_TYPE,
                                                                request_content_type=CONTENT_TYPE,
                                                                has_data_pattern=HAS_DATA_PATTERN,
                                                                token=token, **kwargs)

    def _set_data_pattern(self, *args, **kwargs):
        self._current_data_pattern = DATA_PATTERN


if (__name__ == '__main__'):
    e = V1ServicesCardGetmobilecodeEntity()
    e.send_request()
