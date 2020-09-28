import json

from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler

DOMAIN_NAME = u'10.199.101.217:8091'
URL = u'http://%s/prodQuota/add'
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
  "mobileCheck": "true",
  "wechatCheck": "false",
  "backgroundCheck": "false",
  "hopCheck": "false",
  "prodId": "H9#H99994",
  "subCompanyNo": "00080000",
  "counterCheck": "false",
  "enterpriseCheck": "false",
  "companyNo": "0008",
  "pcCheck": "false"
}

class ProdquotaAddEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME):
        super(ProdquotaAddEntity, self).__init__(domain_name=domain_name, url_string=URL, data=REQUEST_DATA, method_type=METHOD_TYPE, request_content_type=CONTENT_TYPE, request_headers=REQUEST_HEADERS, has_data_pattern=HAS_DATA_PATTERN)

    def _set_data_pattern(self, *args, **kwargs):
        self._current_data_pattern = DATA_PATTERN
if (__name__ == '__main__'):
    e = ProdquotaAddEntity()
    e.send_request()