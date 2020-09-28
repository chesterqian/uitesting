# -*- coding:utf-8 -*-
import time
import datetime
import re

from database_factory import DataBaseFactory
from database_factory import connect_to_database
from sqlalchemy.orm.exc import NoResultFound
from sgw_db_objects import SgwSm


class SgwDataBaseOperator(DataBaseFactory):
    def __init__(self, environment):
        super(SgwDataBaseOperator, self).__init__(environment, "mysql")

    @connect_to_database(SgwSm)
    def get_sms(self, **filters):
        try:
            return self.get(SgwSm, order_by_column_name='desc_created_at',
                            result_mode='all', limit=1, **filters).pop()
        except IndexError:
            raise NoResultFound

    def get_verification_code(self, sgw_sms_mobile, template_id):

        time_stamp = datetime.datetime.now()
        year = time_stamp.year
        month = time_stamp.month
        day = time_stamp.day
        hour = time_stamp.hour
        minute = time_stamp.minute

        time_delta = datetime.timedelta(minutes=0)
        new_time_stamp = datetime.datetime(year, month, day, hour, minute)
        new_time_stamp += time_delta
        counter = 0

        r = None
        while True:
            counter += 1
            if counter > 10:
                break
            try:
                r = self.get_sms(sgw_sms_mobile=sgw_sms_mobile, template_id=template_id)

                if r.created_at < new_time_stamp:
                    time.sleep(1)
                    continue
                else:
                    break
            except NoResultFound:
                time.sleep(1)
        if not r:
            error_message = 'sms not found, mobile: %s, template id: %s'
            raise NoResultFound(error_message % (sgw_sms_mobile, template_id))

        if template_id == 'cif_bindBankCard':
            code = re.findall(r'\d+', r.sgw_sms_content)[1]
        else:
            code = re.search(r'\d+', r.sgw_sms_content).group()

        return code


if __name__ == '__main__':
    from database import sgw_database_operator

    operator = sgw_database_operator
    r = operator.get_verification_code(sgw_sms_mobile='13176981056', template_id='cif_bindBankCard')
    print r
