from service_entities.xjb_service_entities.main_xjbapp_service_entity import MainXjbAppServiceEntity


class HarEntityHandle():
    def __init__(self):
        self.property = {}
        self.product_id = {}


    def get_product_id(self, entity, property, value):
        j = 0
        k = 0

        for i in getattr(entity, property):
            j = j + 1
            self.property[j] = i

        for i in getattr(entity, 'dataList_productId'):
            k = k + 1
            self.product_id[k] = i

        for i in self.property:
            if self.property[i] == value:
                return self.product_id[i]


