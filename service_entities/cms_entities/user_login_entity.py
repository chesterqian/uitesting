import json

from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler

DOMAIN_NAME = u'10.199.101.217:8091'
URL = u'http://%s/user/login'
BODY_DATA = u'{}'
_BODY_DATA = ''
if BODY_DATA:
    _BODY_DATA = json.loads(BODY_DATA)
QUERY_DATA = ''
METHOD_TYPE = u'post'
CONTENT_TYPE = 'form'
REQUEST_DATA = (_BODY_DATA or QUERY_DATA)
REQUEST_HEADERS = [{u'name': u'Cache-Control', u'value': u'max-age=0'},
                   {u'name': u'User-Agent',
                    u'value': u'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'},
                   {u'name': u'Content-Type', u'value': u'application/x-www-form-urlencoded'},
                   {u'name': u'Accept',
                    u'value': u'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'},
                   {u'name': u'Accept-Encoding', u'value': u'gzip, deflate'},
                   {u'name': u'Accept-Language', u'value': u'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2'}]
HAS_DATA_PATTERN = True

DATA_PATTERN = {
    "username": "zengqingxiao",
    "password": "2aa4fcc456c4db9dd2a5facf4f99bed9",
}


class UserLoginEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME):
        super(UserLoginEntity, self).__init__(domain_name=domain_name, url_string=URL, data=REQUEST_DATA,
                                              method_type=METHOD_TYPE, request_content_type=CONTENT_TYPE,
                                              request_headers=REQUEST_HEADERS, has_data_pattern=HAS_DATA_PATTERN)

    def _set_data_pattern(self, *args, **kwargs):
        self._current_data_pattern = DATA_PATTERN


if (__name__ == '__main__'):
    e = UserLoginEntity()
    e.send_request(username='zengqingxiao', password='2aa4fcc456c4db9dd2a5facf4f99bed9')
    for i in e.response_content.headers:
        print i,": ", e.response_content.headers[i]