# coding: utf-8
from sqlalchemy import Column, DateTime, Integer, SmallInteger, String, Text, text
from sqlalchemy.ext.declarative import declarative_base

from common import cif_database_tag

Base = declarative_base()
metadata = Base.metadata


class CifAccoRequestBankResult(Base):
    __tablename__ = 'cif_acco_request_bank_result'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    bank_serial_no = Column(String(24), nullable=False)
    cust_type = Column(String(1), server_default=text("''"))
    cust_no = Column(String(10), nullable=False)
    cust_name = Column(String(40), nullable=False)
    cert_type = Column(String(1), nullable=False)
    cert_no = Column(String(30), nullable=False)
    bank_no = Column(String(3), nullable=False)
    card_no = Column(String(30), nullable=False)
    bank_mobile = Column(String(20))
    apkind = Column(String(10), nullable=False)
    accept_mode = Column(String(10), nullable=False)
    bank_result = Column(String(1))
    bank_err_code = Column(String(10))
    bank_err_msg = Column(String(100))
    acco_result = Column(String(1))
    acco_err_code = Column(String(10))
    acco_err_msg = Column(String(100))
    inviter = Column(String(40))
    inviter_mobile = Column(String(20))
    ip = Column(String(20))
    source = Column(String(10))
    old_bank_no = Column(String(3))
    creator = Column(String(40))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifAgencyAcco(Base):
    __tablename__ = 'cif_agency_acco'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    trade_acco = Column(String(17), nullable=False)
    product_acco = Column(String(12), nullable=False)
    ta_no = Column(String(4), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifBankCardInfo(Base):
    __tablename__ = 'cif_bank_card_info'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    serial_id = Column(String(16), nullable=False)
    bank_group_id = Column(String(60))
    bank_no = Column(String(3))
    cust_no = Column(String(10), nullable=False)
    card_no = Column(String(30), nullable=False)
    display_no = Column(String(30), nullable=False)
    type = Column(String(1), server_default=text("''"))
    bank_mobile = Column(String(20))
    protocol = Column(String(100))
    is_delete = Column(String(1), nullable=False, server_default=text("'0'"))
    accept_mode = Column(String(1))
    is_main_card = Column(String(1))
    open_date = Column(String(8))
    close_date = Column(String(8))
    cert_type = Column(String(2))
    cert_no = Column(String(30))
    bank_acco_name = Column(String(100))
    bank_name = Column(String(50))
    protocal_exists = Column(String(2))
    protocal_no = Column(String(200))
    sub_bank_no = Column(String(3))
    branch = Column(String(9), nullable=False)
    bank_address = Column(String(400))
    cnaps_no = Column(String(20))
    capital_mode = Column(String(2), nullable=False)
    sign_type = Column(String(2))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifBankConf(Base):
    __tablename__ = 'cif_bank_conf'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    bank_no = Column(String(3), nullable=False)
    add_card_state = Column(String(1), nullable=False)
    add_card_tip = Column(String(400))
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifCompanyAttach(Base):
    __tablename__ = 'cif_company_attach'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    type = Column(String(2), nullable=False)
    attach_url = Column(String(400), nullable=False)
    thumbnail = Column(String(400))
    file_name = Column(String(100))
    source = Column(String(1), nullable=False)
    seq_no = Column(Integer, nullable=False, server_default=text("'1'"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class CifCompanyAttachLog(Base):
    __tablename__ = 'cif_company_attach_log'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    type = Column(String(2), nullable=False)
    attach_url = Column(String(400), nullable=False)
    thumbnail = Column(String(400))
    file_name = Column(String(100))
    source = Column(String(1), nullable=False)
    seq_no = Column(Integer, nullable=False, server_default=text("'1'"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class CifCompanyDetail(Base):
    __tablename__ = 'cif_company_detail'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    telephone = Column(String(20))
    fax_no = Column(String(20))
    address = Column(String(200))
    zipcode = Column(String(16))
    cert_valid_date = Column(String(8))
    org_no = Column(String(30))
    tax_reg_no = Column(String(30))
    legal_name = Column(String(40), nullable=False, server_default=text("''"))
    legal_cert_type = Column(String(1), nullable=False, server_default=text("''"))
    legal_cert_no = Column(String(20), nullable=False, server_default=text("''"))
    legal_cert_valid_date = Column(String(8), nullable=False, server_default=text("''"))
    remark = Column(String(200))
    oper_mobile = Column(String(20), nullable=False)
    oper_name = Column(String(40), nullable=False)
    oper_cert_type = Column(String(1), nullable=False)
    oper_cert_no = Column(String(30), nullable=False)
    oper_cert_valid_date = Column(String(8), nullable=False)
    oper_email = Column(String(256))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class CifCustBase(Base):
    __tablename__ = 'cif_cust_base'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    name = Column(String(40))
    mobile = Column(String(20))
    cert_type = Column(String(1))
    cert_no = Column(String(30))
    passwd = Column(String(64))
    passwd_seed = Column(String(32))
    status = Column(String(1), nullable=False)
    status_start_date = Column(DateTime)
    status_end_date = Column(DateTime)
    source = Column(String(2), nullable=False)
    level = Column(Integer, nullable=False, server_default=text("'0'"))
    is_verified = Column(String(1), nullable=False, server_default=text("'N'"))
    type = Column(String(1), nullable=False, server_default=text("''"))
    risk_level = Column(String(1), server_default=text("''"))
    qualified_date = Column(DateTime)
    ip = Column(String(20))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifCustChange(Base):
    __tablename__ = 'cif_cust_change'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    change_type = Column(String(2), nullable=False)
    change_from = Column(String(600), server_default=text("''"))
    change_to = Column(String(600), server_default=text("''"))
    created_at = Column(DateTime, nullable=False)
    operator_type = Column(String(1), server_default=text("'0'"))
    operator = Column(String(20))


class CifCustDetail(Base):
    __tablename__ = 'cif_cust_detail'
    table_tag = cif_database_tag
    
    cust_no = Column(String(10), primary_key=True)
    occupation = Column(String(40))
    email = Column(String(200))
    office_tel = Column(String(20))
    home_tel = Column(String(20))
    cert_valid_date = Column(String(10))
    cert_sign_org = Column(String(40))
    birthday = Column(String(8))
    gender = Column(String(1))
    address = Column(String(200))
    zipcode = Column(String(16))
    telephone = Column(String(20))
    risk_level_date = Column(DateTime)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))


class CifCustFrozen(Base):
    __tablename__ = 'cif_cust_frozen'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    frozen_type = Column(String(1), nullable=False)
    frozen_method = Column(String(1), nullable=False)
    frozen_start_date = Column(DateTime, nullable=False)
    frozen_end_date = Column(DateTime)
    created_at = Column(DateTime, nullable=False)


class CifCustLoginLog(Base):
    __tablename__ = 'cif_cust_login_log'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    login_time = Column(DateTime, nullable=False)
    login_result = Column(String(1), nullable=False)
    remote_ip = Column(String(20))
    server_ip = Column(String(20))
    imei = Column(String(64))
    client_info = Column(String(100))
    token = Column(String(64))
    remark = Column(String(100))


class CifCustPayPwd(Base):
    __tablename__ = 'cif_cust_pay_pwd'
    table_tag = cif_database_tag
    
    cust_no = Column(String(10), primary_key=True)
    passwd = Column(String(128))
    passwd_seed = Column(String(64))
    status = Column(String(1))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifCustProblem(Base):
    __tablename__ = 'cif_cust_problem'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    problem = Column(String(500), nullable=False)
    mobile = Column(String(20))
    operator = Column(String(20))
    feedback = Column(String(500))
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifCustRiskAnswer(Base):
    __tablename__ = 'cif_cust_risk_answer'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    question_no = Column(String(10))
    answer = Column(String(20))
    score = Column(Integer, nullable=False)
    risk_level = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifFundAccount(Base):
    __tablename__ = 'cif_fund_account'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    fund_acco = Column(String(12), nullable=False)
    ta_no = Column(String(6), nullable=False)
    cust_no = Column(String(10), nullable=False)
    open_date = Column(String(8), nullable=False, server_default=text("''"))
    status = Column(String(1), nullable=False, server_default=text("''"))
    type = Column(String(1), nullable=False)
    net_point = Column(String(12))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifInviteCode(Base):
    __tablename__ = 'cif_invite_code'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    code = Column(String(10), nullable=False, server_default=text("''"))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifInviter(Base):
    __tablename__ = 'cif_inviter'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    inviter_cust_no = Column(String(10))
    inviter_mobile = Column(String(20))
    status = Column(String(1), nullable=False)
    branch_code = Column(String(20))
    channel = Column(String(20))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifJointCard(Base):
    __tablename__ = 'cif_joint_card'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    system_code = Column(String(2))
    trans_no = Column(String(40))
    trans_type = Column(String(20))
    bank_trans_type = Column(String(20))
    outer_order_no = Column(String(40), nullable=False, server_default=text("''"))
    cust_no = Column(String(10), server_default=text("''"))
    name = Column(String(40), nullable=False)
    cert_type = Column(String(2), nullable=False, server_default=text("''"))
    cert_no = Column(String(30), nullable=False, server_default=text("''"))
    bank = Column(String(6), nullable=False)
    card_type = Column(String(2), server_default=text("''"))
    card_no = Column(String(32), nullable=False)
    bank_mobile = Column(String(20), nullable=False)
    status = Column(String(1), nullable=False)
    status_date = Column(DateTime)
    status_reason = Column(String(200))
    branch_code = Column(String(10))
    branch_name = Column(String(60))
    ap_date = Column(String(10))
    ap_time = Column(String(6))
    set_date = Column(String(10))
    oper_no = Column(String(8))
    open_date = Column(String(10))
    open_time = Column(String(10))
    card_valid_date = Column(String(10))
    operator = Column(String(10))
    reviewer = Column(String(10))
    cust_detail = Column(String(1000))
    extend_info = Column(String(4000))
    match_flag = Column(String(1))
    cms_operator = Column(String(40))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifJointCardBillCheck(Base):
    __tablename__ = 'cif_joint_card_bill_check'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    system_code = Column(String(2))
    trans_no = Column(String(40))
    trans_type = Column(String(20))
    bank_trans_type = Column(String(20))
    trans_date = Column(String(10))
    card_no = Column(String(40))
    cert_type = Column(String(2))
    cert_no = Column(String(40))
    name = Column(String(40))
    cert_valid_date = Column(String(8))
    mobile = Column(String(20))
    address = Column(String(100))
    zipcode = Column(String(6))
    line = Column(String(4000))
    status = Column(String(1))
    status_reason = Column(String(400))
    file_path = Column(String(200))
    operator = Column(String(40))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifJointCardLog(Base):
    __tablename__ = 'cif_joint_card_log'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    refer_id = Column(Integer, nullable=False)
    trans_type = Column(String(20), server_default=text("''"))
    bank_trans_type = Column(String(20))
    system_code = Column(String(2), nullable=False, server_default=text("''"))
    trans_no = Column(String(40), nullable=False, server_default=text("''"))
    outer_order_no = Column(String(40), server_default=text("''"))
    cust_no = Column(String(10), server_default=text("''"))
    name = Column(String(40), nullable=False)
    cert_type = Column(String(2), nullable=False, server_default=text("''"))
    cert_no = Column(String(30), nullable=False, server_default=text("''"))
    bank = Column(String(6), nullable=False)
    card_type = Column(String(2), server_default=text("''"))
    card_no = Column(String(32), nullable=False)
    bank_mobile = Column(String(20), nullable=False)
    status = Column(String(1), nullable=False)
    status_date = Column(DateTime)
    status_reason = Column(String(200))
    branch_code = Column(String(10))
    branch_name = Column(String(60))
    ap_date = Column(String(10))
    ap_time = Column(String(6))
    set_date = Column(String(10))
    oper_no = Column(String(8))
    open_date = Column(String(10))
    open_time = Column(String(10))
    card_valid_date = Column(String(10))
    operator = Column(String(10))
    reviewer = Column(String(10))
    cust_detail = Column(String(1000))
    extend_info = Column(String(4000))
    match_flag = Column(String(1))
    cms_operator = Column(String(40))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifMobileAudit(Base):
    __tablename__ = 'cif_mobile_audit'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    name = Column(String(20))
    old_mobile = Column(String(20), nullable=False)
    new_mobile = Column(String(20), nullable=False)
    id_pic_url = Column(String(200))
    status = Column(String(1), nullable=False)
    status_reason = Column(String(40))
    cert_type = Column(String(1))
    cert_no = Column(String(30))
    cert_area = Column(String(40))
    old_mobile_area = Column(String(40))
    new_mobile_area = Column(String(40))
    remark = Column(String(200))
    audit_type = Column(String(1), nullable=False)
    operator = Column(String(40))
    approver = Column(String(40))
    operator_date = Column(DateTime)
    approver_date = Column(DateTime)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifOpenFundRequest(Base):
    __tablename__ = 'cif_open_fund_request'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    ta_no = Column(String(6), nullable=False)
    cust_no = Column(String(10), nullable=False)
    app_sheet_serial_no = Column(String(24), nullable=False)
    certificate_type = Column(String(1), nullable=False)
    certificate_no = Column(String(30), nullable=False)
    investor_name = Column(String(120), nullable=False)
    transaction_date = Column(String(8), nullable=False)
    individual_or_institution = Column(String(1), nullable=False)
    institution_type = Column(String(1))
    transactor_cert_no = Column(String(30))
    transactor_cert_type = Column(String(1))
    transactor_name = Column(String(20))
    transaction_account_id = Column(String(17), server_default=text("''"))
    trade_acco = Column(String(17))
    ta_trade_acco = Column(String(17))
    distributor_code = Column(String(9))
    business_code = Column(String(3))
    branch_code = Column(String(9))
    transaction_time = Column(String(6), nullable=False)
    ta_account_id = Column(String(12))
    mobile_tel_no = Column(String(22))
    post_code = Column(String(6))
    email_address = Column(String(256))
    home_tel_no = Column(String(22))
    address = Column(String(120))
    open_date = Column(String(8), nullable=False)
    status = Column(String(1))
    status_reason = Column(String(4000))
    request = Column(Text)
    response = Column(Text)
    retry_count = Column(Integer)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifRiskQuestion(Base):
    __tablename__ = 'cif_risk_question'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    question_no = Column(String(6), nullable=False)
    topic_row = Column(SmallInteger, nullable=False)
    topic_id = Column(Integer, nullable=False)
    type = Column(String(1), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifRiskTestTopic(Base):
    __tablename__ = 'cif_risk_test_topic'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    question = Column(String(1000), nullable=False)
    selecta = Column(String(100))
    selectb = Column(String(100))
    selectc = Column(String(100))
    selectd = Column(String(100))
    scorea = Column(SmallInteger)
    scoreb = Column(SmallInteger)
    scorec = Column(SmallInteger)
    scored = Column(SmallInteger)
    type = Column(String(1), nullable=False)
    status = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifSysTransLog(Base):
    __tablename__ = 'cif_sys_trans_log'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    system_code = Column(String(2), nullable=False)
    trans_no = Column(String(40), nullable=False)
    trans_type = Column(String(20))
    request = Column(Text)
    response = Column(Text)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifTradeAccountInfo(Base):
    __tablename__ = 'cif_trade_account_info'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    trade_acco = Column(String(17), nullable=False)
    status = Column(String(1), nullable=False)
    open_date = Column(String(8), nullable=False)
    close_date = Column(String(8))
    type = Column(String(1), nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifTradeAccountRef(Base):
    __tablename__ = 'cif_trade_account_ref'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False, server_default=text("''"))
    trade_acco = Column(String(17), nullable=False)
    ta_trade_acco = Column(String(64))
    fund_acco = Column(String(12), nullable=False)
    ta_no = Column(String(6), nullable=False)
    status = Column(String(1))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class CifVaccountInfo(Base):
    __tablename__ = 'cif_vaccount_info'
    table_tag = cif_database_tag
    
    id = Column(Integer, primary_key=True)
    cust_no = Column(String(10), nullable=False)
    vacco_no = Column(String(10), nullable=False)
    product_id = Column(String(6), nullable=False)
    status = Column(String(1), nullable=False)
    open_date = Column(String(8), nullable=False)
    close_date = Column(String(8))
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
