from common.global_config import Global
from common.utility import Utility
from common.utility import des3_encrypt
from common.service_entity_factory import EntityFactory
from database.sgw_db_operator import SgwDataBaseOperator
from service_entities.xjb_service_entities.v1_services_card_getmobilecode_entity import \
    V1ServicesCardGetmobilecodeEntity
from service_entities.xjb_service_entities.v1_services_card_newbinding_entity import V1ServicesCardNewbindingEntity
from service_entities.xjb_service_entities.v1_services_card_settradepassword_entity import \
    V1ServicesCardSettradepasswordEntity
from service_entities.xjb_service_entities.v1_services_login_dologin_entity import V1ServicesLoginDologinEntity
from service_entities.xjb_service_entities.v1_services_register_getmobilecode_entity import \
    V1ServicesRegisterGetmobilecodeEntity
from service_entities.xjb_service_entities.v1_services_register_confirm_entity import V1ServicesRegisterConfirmEntity
from service_entities.xjb_service_entities.v1_services_trade_confirm_entity import V1ServicesTradeConfirmEntity
from service_entities.xjb_service_entities.v1_services_trade_enchargevalidate_entity import \
    V1ServicesTradeEnchargevalidateEntity
from service_entities.xjb_service_entities.v1_services_trade_myvipfinanciallist_entity import \
    V1ServicesTradeMyvipfinanciallistEntity
from service_entities.xjb_service_entities.v1_services_trade_purchasevalidate_entity import \
    V1ServicesTradePurchasevalidateEntity
from service_entities.xjb_service_entities.v1_services_common_acquiredeviceid_entity import \
    V1ServicesCommonAcquiredeviceidEntity
from v1_services_card_bindingresult_entity import V1ServicesCardBindingresultEntity
from v1_services_custinfo_getcustbaseinfo_entity import V1ServicesCustinfoGetcustbaseinfoEntity
from v1_services_card_matchchannel_entity import V1ServicesCardMatchchannelEntity

ENVIRONMENT_MAP_DOMAIN_NAME = {
    "uat": Global.Environment.HUXIN_XJB_UAT,
    "ci": Global.Environment.HUXIN_CMS_CI
}
ENVIRONMENT_MAP_DATABASE_TAG = {
    "uat": 'supergw_uat',
    'ci': 'spw'
}


class MainXjbAppServiceEntity(object):
    def __init__(self, environment='uat', concurrent_mode=False):
        self._domain_name = ENVIRONMENT_MAP_DOMAIN_NAME[environment]
        self.operator = SgwDataBaseOperator(ENVIRONMENT_MAP_DATABASE_TAG[environment])
        self.util = Utility()
        self._current_mobile = None
        self._current_recharge_serialno = None
        self._current_mobile_code = None
        self._current_login_token = None
        self._current_register_serialno = None
        self._current_purchase_product_serialno = None
        self._current_set_trade_passowrd_serialno = None
        self._current_device_id = None
        self._common_headers = None
        self._current_biding_card_result = None
        self._current_base_cust_info = None
        self._entity_factory = EntityFactory(concurrent_mode=concurrent_mode)

    @property
    def current_login_token(self):
        return self._current_login_token

    @property
    def current_register_serialno(self):
        return self._current_register_serialno

    @property
    def current_mobile(self):
        return self._current_mobile

    @property
    def current_mobile_code(self):
        return self._current_mobile_code

    @property
    def current_recharge_serialno(self):
        return self._current_recharge_serialno

    @property
    def current_set_trade_passowrd_serialno(self):
        return self._current_set_trade_passowrd_serialno

    @property
    def current_purchase_product_serialno(self):
        return self._current_purchase_product_serialno

    @property
    def current_device_id(self):
        if not self._current_device_id:
            self._current_device_id = self.get_device_id()

        return self._current_device_id

    @property
    def common_headers(self):
        if not self._common_headers:
            self._common_headers = {'clientVersion': 'a-1.5.1'}
            device_id = self.current_device_id

            if device_id:
                self._common_headers.update({'deviceId': device_id})
            else:
                raise Exception('device id is not generated!')

        return self._common_headers

    @property
    def current_binding_card_result(self):
        self._current_biding_card_result = self.get_binding_card_result()
        return self._current_biding_card_result.authResult

    @property
    def current_base_cust_info(self):
        self._current_base_cust_info = self.get_base_cust_info()
        return self._current_base_cust_info

    def _encrypt_password(self, password):
        key = self.current_device_id + '00'
        ivect = 'sh-hx-zq'
        password = des3_encrypt(str(key), ivect, password)

        return password

    def get_mobile_code(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesRegisterGetmobilecodeEntity, self._domain_name,
            **{'request_headers': self.common_headers})

        entity.send_request(**kwargs)
        self._current_register_serialno = entity.body_serialNo
        self._current_mobile_code = \
            self.operator.get_verification_code(sgw_sms_mobile=kwargs['mobile'],
                                                template_id='cif_register')
        return entity

    def register_confirm(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesRegisterConfirmEntity, self._domain_name,
            **{'request_headers': self.common_headers})

        password = kwargs['password']
        kwargs['password'] = self._encrypt_password(password)

        entity.send_request(**kwargs)

        self._current_login_token = entity.body_token
        return entity

    def login(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesLoginDologinEntity, self._domain_name,
            **{'request_headers': self.common_headers})

        password = kwargs['password']
        kwargs['password'] = self._encrypt_password(password)

        entity.send_request(**kwargs)

        self._current_login_token = entity.body_token
        return entity

    def recharge(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesTradeEnchargevalidateEntity,
            self._domain_name, token=self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request(**kwargs)

        self._current_recharge_serialno = entity.body_serialNo
        return entity

    def recharge_confirm(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesTradeConfirmEntity,
            self._domain_name, token=self.current_login_token,
            **{'request_headers': self.common_headers})

        password = kwargs['password']
        kwargs['password'] = self._encrypt_password(password)

        entity.send_request(**kwargs)
        return entity

    def purchase_product(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesTradePurchasevalidateEntity,
            self._domain_name, token=self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request(**kwargs)
        self._current_purchase_product_serialno = entity.body_serialNo
        return entity

    def purchase_product_confirm(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesTradeConfirmEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        password = kwargs['password']
        kwargs['password'] = self._encrypt_password(password)

        entity.send_request(**kwargs)
        return entity

    def set_trade_password(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesCardSettradepasswordEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        password = kwargs['newPassword']
        kwargs['newPassword'] = self._encrypt_password(password)

        entity.send_request(**kwargs)
        self._current_set_trade_passowrd_serialno = entity.body_serialNo
        return entity

    def binding_card_get_mobile_code(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesCardGetmobilecodeEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request(**kwargs)
        self._current_mobile_code = \
            self.operator.get_verification_code(sgw_sms_mobile=kwargs['mobile'],
                                                template_id='cif_bindBankCard')
        return entity

    def binding_card_confirm(self, **kwargs):
        entity = self._entity_factory.get_entity(
            V1ServicesCardNewbindingEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request(**kwargs)
        return entity

    def get_device_id(self):
        entity = self._entity_factory.get_entity(
            V1ServicesCommonAcquiredeviceidEntity, self._domain_name,
            **{'request_headers': self.common_headers})

        entity.send_request()
        return entity.deviceId

    def get_financial_list(self, **kwargs):
        entity = V1ServicesTradeMyvipfinanciallistEntity(
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request(**kwargs)

        return entity

    def get_binding_card_result(self):
        entity = self._entity_factory.get_entity(
            V1ServicesCardBindingresultEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        serialno = self.current_set_trade_passowrd_serialno
        entity.send_request(serialNo=serialno)

        return entity

    def get_base_cust_info(self):
        entity = self._entity_factory.get_entity(
            V1ServicesCustinfoGetcustbaseinfoEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request()

        return entity

    def card_match_channel(self, bin_no):
        entity = self._entity_factory.get_entity(
            V1ServicesCardMatchchannelEntity,
            self._domain_name, self.current_login_token,
            **{'request_headers': self.common_headers})

        entity.send_request(bin=bin_no)

        return entity
