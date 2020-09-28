# -*- coding: utf-8 -*-
import threading
from service_entities.xjb_service_entities.main_xjbapp_service_entity import MainXjbAppServiceEntity
from common.utility import Utility

LOGIN_PASSWORD = 'XzNxJXYxpeZQFboxELoesQ=='
TRADE_PASSWORD = 'CdRySweFfmQ='


class XjbServiceController(object):
    def __init__(self):
        self.utility = Utility()
        self.main_service_entity = MainXjbAppServiceEntity(concurrent_mode=True)

    def register(self):
        mobile = self.utility.fake_cn.phone_number()
        self.main_service_entity.get_mobile_code(mobile=mobile)

        serial_no = self.main_service_entity.current_register_serialno
        mobile_code = self.main_service_entity.current_mobile_code

        entity = self.main_service_entity.register_confirm(mobileCode=mobile_code,
                                                           password='a0000000',
                                                           serialNo=serial_no,
                                                           )
        assert (entity.returnCode == '000000')
        print '== %s ==' % mobile


def cothread_run():
    controller = XjbServiceController()
    controller.register()


class TestCaseGenerator(threading.Thread):
    def run(self):
        cothread_run()


if __name__ == '__main__':
    import time

    for i in range(0, 120):
        threads = [TestCaseGenerator() for i in xrange(200)]
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
        time.sleep(10)
