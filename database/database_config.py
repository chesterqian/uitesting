__author__ = 'Shirley'

from oracle_database_operators import OracleDatabaseOperator
from loan_app_mysql_database_operators import LoanAppMySqlDatabaseOperator
from techops_mysql_database_operators import TechopsMySqlDatabaseOperator

DATABASE_OPERATOR_MAP_TAG_AND_TYPE = {
    'demo_oracle': OracleDatabaseOperator,
    'loan_biz_mysql': LoanAppMySqlDatabaseOperator,
    'loan_base_mysql': TechopsMySqlDatabaseOperator
}

ORACLE_DATABASE_TABLE_MAP_OPERATOR_METHOD = {
    'Actor': 'get_actor',
    'Wallet': 'get_wallet',
    'BorrowerConfig': 'select_from_borrower_config_by_name',
    'ActorBorrowerConfig': 'select_from_actor_borrower_config',
    'LoanApp': 'select_from_loan_app_by_loan_id',
    ('Pi', 'Addr'): 'select_from_pi_and_addr',
    ('LoanApp', 'CreditClass'): 'select_from_credit_class',
    'BdLoanApp': 'select_from_bd_loan_app_by_loan_id',
    'AssetLiability': 'select_asset_liability_by_loan_app_id',
    'Loan': 'select_loan_by_loan_id_and_status',
    'CfgItem': 'get_cfg_item_by_key',
    'Lpay': 'select_lpay_by_loan_id',
    'EntityProp': 'get_entity_prop_by_loan_id',
    'Account': 'get_account_by_aid_and_type',
    'Sr': 'get_sr_id_by_loan_id_special',
    'SrNote': 'get_sr_note_by_sr_id'
}

LOAN_APP_MYSQL_DATABASE_TABLE_MAP_OPERATOR_METHOD = {
    'LoanApp': 'get_loan_app_by_external_id',
    'UserIdentity': 'get_user_identity_by_card_num',
    'JobInfo': 'get_job_info_by_user_id',
    'ContactPerson': 'get_contact_person_by_user_id',
    'BankAccount': 'get_bank_account_by_user_id',
    'LoanTran': 'get_loan_trans_by_external_id',
    'ChannelProductQuota': 'get_channel_product_quota_by_channel_id'
}

TECHOPS_MYSQL_DATABASE_TABLE_MAP_OPERATOR_METHOD = {
    'UaRole': 'get_specific_role_by_role_id',
    'UaMenu': 'get_menu_by_domain_id_and_menu_name',
    'UaUriPattern': 'get_uri_pattern_by_domain_id_and_uri_name',
    'UaUser': 'get_user_by_email',
    'UaUserDomain': 'get_user_by_domain_id_and_user_id',
    'UaGroup': 'get_specific_group_by_group_id'
}

DATABASE_OPERATOR_MAP_TABLE_METHOD = {
    OracleDatabaseOperator: ORACLE_DATABASE_TABLE_MAP_OPERATOR_METHOD,
    LoanAppMySqlDatabaseOperator: LOAN_APP_MYSQL_DATABASE_TABLE_MAP_OPERATOR_METHOD,
    TechopsMySqlDatabaseOperator: TECHOPS_MYSQL_DATABASE_TABLE_MAP_OPERATOR_METHOD
}
