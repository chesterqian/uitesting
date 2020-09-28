from common.global_config import Global
from service_entities.cms_entities.app_cache_update_entity import AppCacheUpdateEntity
from service_entities.cms_entities.pdcmanager_doinsertproductbasecfg_entity import \
    PdcmanagerDoinsertproductbasecfgEntity
from service_entities.cms_entities.pdcmanager_doproductbasechecklist_entity import \
    PdcmanagerDoproductbasechecklistEntity
from service_entities.cms_entities.pdcmanager_doproductbasesubcheck_entity import \
    PdcmanagerDoproductbasesubcheckEntity
from service_entities.cms_entities.pdcmanager_saveproductdetailcof_entity import \
    PdcmanagerSaveproductdetailcofEntity
from service_entities.cms_entities.pdcmanager_updateproductchannle_entity import \
    PdcmanagerUpdateproductchannleEntity
from service_entities.cms_entities.prodquota_add_entity import ProdquotaAddEntity
from service_entities.cms_entities.prodquota_changecount_entity import ProdquotaChangecountEntity
from service_entities.cms_entities.prodquota_changequato_entity import ProdquotaChangequatoEntity
from service_entities.cms_entities.user_login_entity import UserLoginEntity

ENVIRONMENT_MAP_DOMAIN_NAME = {
    "uat": Global.Environment.HUXIN_CMS_UAT,
}

class MainCmsServiceEntity():
    def __init__(self, environment='uat'):
        self._domain_name = ENVIRONMENT_MAP_DOMAIN_NAME[environment]

    @property
    def current_product_id(self):
        return self._current_product_id

    def login(self, **kwargs):
        entity = UserLoginEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def new_product(self, **kwargs):
        entity = PdcmanagerDoinsertproductbasecfgEntity(self._domain_name)
        entity.send_request(**kwargs)
        self._current_product_id = entity.productid
        return entity

    def submit_product(self, **kwargs):
        entity = PdcmanagerDoproductbasesubcheckEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def check_product(self, **kwargs):
        entity = PdcmanagerDoproductbasechecklistEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def update_product_channle(self, **kwargs):
        entity = PdcmanagerUpdateproductchannleEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def save_product_detail(self, **kwargs):
        entity = PdcmanagerSaveproductdetailcofEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def add_product_quota(self, **kwargs):
        entity = ProdquotaAddEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def change_product_quota(self, **kwargs):
        entity = ProdquotaChangequatoEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def change_product_count(self, **kwargs):
        entity = ProdquotaChangecountEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity

    def app_cache_update(self, **kwargs):
        entity = AppCacheUpdateEntity(self._domain_name)
        entity.send_request(**kwargs)
        return entity