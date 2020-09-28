import json
from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler
from common.global_config import Global

DOMAIN_NAME = u'10.199.101.211:18088'
URL = u'http://%s//V1/services/card/setTradePassword'
BODY_DATA = u'{}'
_BODY_DATA = ''
if BODY_DATA:
    _BODY_DATA = json.loads(BODY_DATA)
QUERY_DATA = ''
METHOD_TYPE = u'post'
CONTENT_TYPE = 'json'
REQUEST_DATA = (_BODY_DATA or QUERY_DATA)
HEADERS_DEVICE_ID = Global.HeaderContentType.HEADERS_DEVICES_ID
REQUEST_HEADERS = [{u'name': u'deviceId', u'value': HEADERS_DEVICE_ID},
                   {u'name': u'clientVersion', u'value': u'a-1.5.1'}, ]
HAS_DATA_PATTERN = True

DATA_PATTERN = {"newPassword": "CdRySweFfmQ="}


class V1ServicesCardSettradepasswordEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME, token=None, **kwargs):
        super(V1ServicesCardSettradepasswordEntity, self).__init__(domain_name=domain_name, url_string=URL,
                                                                   data=REQUEST_DATA, method_type=METHOD_TYPE,
                                                                   request_content_type=CONTENT_TYPE,
                                                                   # request_headers=REQUEST_HEADERS,
                                                                   has_data_pattern=HAS_DATA_PATTERN,
                                                                   token=token,
                                                                   **kwargs)

    def _set_data_pattern(self, *args, **kwargs):
        self._current_data_pattern = DATA_PATTERN


if (__name__ == '__main__'):
    e = V1ServicesCardSettradepasswordEntity()
    e.send_request()
