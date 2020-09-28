# -*- coding:utf-8 -*-
from sqlalchemy.orm.exc import NoResultFound
from database_factory import DataBaseFactory
from database_factory import connect_to_database
from cif_db_objects import CifCustBase
from cif_db_objects import CifBankCardInfo

class CifDbOperator(DataBaseFactory):
    def __init__(self, environment):
        super(CifDbOperator, self).__init__(environment, "mysql")

    @connect_to_database(CifCustBase)
    def get_cif_base_account(self, **filters):
        return self.get(CifCustBase, result_mode='one', **filters)

    @connect_to_database(CifCustBase)
    def get_cif_base_account_like(self, *args):
        return self.get_like(CifCustBase, *args)

    @connect_to_database(CifBankCardInfo)
    def get_cif_bank_card_info(self, **filters):
        try:
            return self.get(CifBankCardInfo, result_mode='all', **filters).pop()
        except (NoResultFound, IndexError):
            pass

    @connect_to_database
    def get_all_cif_bank_card(self, **filters):
        try:
            return self.get(CifBankCardInfo, result_mode='all', **filters)
        except NoResultFound:
            pass


if __name__ == '__main__':
    operator = CifDbOperator('cif_uat')
    r = operator.get_cif_base_account_like('name', 'H9TESTUAT%')
    for instance in r:
        print instance.mobile
    # r = operator.get_cif_bank_card_info(cust_no=r.cust_no)
    # print r.card_no
    r = operator.get_cif_base_account(mobile='13001807368')
    print r.cust_no

