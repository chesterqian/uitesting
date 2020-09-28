import json
from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler

DOMAIN_NAME = u'10.199.101.211:18088'
URL = u'http://%s//V1/services/custinfo/getCustBaseInfo'
BODY_DATA = u'{}'
_BODY_DATA = ''
if BODY_DATA:
    _BODY_DATA = json.loads(BODY_DATA)
QUERY_DATA = ''
METHOD_TYPE = u'post'
CONTENT_TYPE = 'json'
REQUEST_DATA = (_BODY_DATA or QUERY_DATA)
REQUEST_HEADERS = [{u'name': u'deviceId', u'value': u'CjBu3oW19FnKC9WpvguIqQ'},
                   {u'name': u'token', u'value': u'0e473fa1-f60a-47e2-adbb-0e47ab56b87b'},
                   {u'name': u'clientVersion', u'value': u'a-1.5.1'},
                   {u'name': u'Content-Type', u'value': u'application/json; charset=utf-8'},
                   {u'name': u'Content-Length', u'value': u'2'}, {u'name': u'Host', u'value': u'10.199.101.211:18088'},
                   {u'name': u'Connection', u'value': u'Keep-Alive'}, {u'name': u'Accept-Encoding', u'value': u'gzip'},
                   {u'name': u'User-Agent', u'value': u'okhttp/3.2.0'}]
HAS_DATA_PATTERN = False


class V1ServicesCustinfoGetcustbaseinfoEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME):
        super(V1ServicesCustinfoGetcustbaseinfoEntity, self).__init__(domain_name=domain_name, url_string=URL,
                                                                      data=REQUEST_DATA, method_type=METHOD_TYPE,
                                                                      request_content_type=CONTENT_TYPE,
                                                                      request_headers=REQUEST_HEADERS,
                                                                      has_data_pattern=HAS_DATA_PATTERN)

    def _set_data_pattern(self, *args, **kwargs):
        pass


if (__name__ == '__main__'):
    e = Foo()
    e.send_request()
