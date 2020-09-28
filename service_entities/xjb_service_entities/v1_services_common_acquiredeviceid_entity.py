import json
from common.basic_troop_service_entity_handler import BasicTroopServiceEntityHandler

DOMAIN_NAME = u'10.199.101.211:18088'
URL = u'http://%s//V1/services/common/acquireDeviceId'
BODY_DATA = u'{}'
_BODY_DATA = ''
if BODY_DATA:
    _BODY_DATA = json.loads(BODY_DATA)
QUERY_DATA = ''
METHOD_TYPE = u'post'
CONTENT_TYPE = 'json'
REQUEST_DATA = (_BODY_DATA or QUERY_DATA)
HAS_DATA_PATTERN = False


class V1ServicesCommonAcquiredeviceidEntity(BasicTroopServiceEntityHandler):
    """
    accessible attribute list for response data:
    %s
    ==================
    kwargs for request:
    Please refer to the constants BODY_DATA or QUERY_DATA request parameters
    """

    def __init__(self, domain_name=DOMAIN_NAME, **kwargs):
        super(V1ServicesCommonAcquiredeviceidEntity, self).__init__(domain_name=domain_name, url_string=URL,
                                                                    data=REQUEST_DATA, method_type=METHOD_TYPE,
                                                                    request_content_type=CONTENT_TYPE,
                                                                    has_data_pattern=HAS_DATA_PATTERN,
                                                                    **kwargs)

    def _set_data_pattern(self, *args, **kwargs):
        pass


if (__name__ == '__main__'):
    e = V1ServicesCommonAcquiredeviceidEntity()
    e.send_request()
