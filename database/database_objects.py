from sqlalchemy import Column, DateTime, Numeric, String, text, Integer, BigInteger, Date, Index, Table, \
    LargeBinary, Text
from sqlalchemy.dialects.oracle.base import RAW
from sqlalchemy.dialects.oracle import NUMBER, VARCHAR2, CLOB
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata

class Actor(Base):
    __tablename__ = 'sl$actor'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    name = Column(String(200))
    email = Column(String(200), unique=True)
    ssn = Column(String(80), index=True)
    ssn_type = Column(Numeric(1, 0, asdecimal=False))
    ssn_short = Column(String(8))
    credential = Column(RAW)
    failed_auth_cnt = Column(Numeric(2, 0, asdecimal=False))
    type = Column(Numeric(2, 0, asdecimal=False), nullable=False, index=True)
    acc_type = Column(Numeric(2, 0, asdecimal=False), index=True)
    relation = Column(Numeric(2, 0, asdecimal=False))
    subtype = Column(Numeric(2, 0, asdecimal=False))
    owner_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    admin_grp_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    prog_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    referer_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    last_login_d = Column(DateTime)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    cancel_d = Column(DateTime)
    a_status_d = Column(DateTime)
    b_status_d = Column(DateTime)
    l_status_d = Column(DateTime)
    t_status_d = Column(DateTime)
    a_status = Column(Numeric(1, 0, asdecimal=False))
    b_status = Column(Numeric(1, 0, asdecimal=False))
    l_status = Column(Numeric(1, 0, asdecimal=False))
    t_status = Column(Numeric(1, 0, asdecimal=False))
    u_status = Column(Numeric(2, 0, asdecimal=False), index=True)
    fname = Column(String(80))
    lname = Column(String(80))
    mname = Column(String(80))
    balance = Column(Numeric(12, 2))
    locked_for_inv = Column(Numeric(12, 2))
    advance_amt = Column(Numeric(12, 2))
    advance_override = Column(Numeric(12, 2))
    auto_ach_qp_end_d = Column(DateTime)
    dist_freeze_end_d = Column(DateTime)
    wave_fee_until_d = Column(DateTime)
    wave_lcfee_until_d = Column(DateTime)
    lending_state = Column(String(5))
    agree_compliant = Column(Numeric(1, 0, asdecimal=False))
    waroic = Column(Numeric(8, 6))
    flags = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    ytm = Column(Numeric(asdecimal=False))
    device_token_ids = Column(String(300))
    mobile_installation_d = Column(DateTime)
    email_optout = Column(Numeric(asdecimal=False))
    country_code = Column(String(5))
    vip_level = Column(Numeric(asdecimal=False))
    partner_id = Column(Numeric(scale=0, asdecimal=False))
    app_config_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    payment_password = Column(RAW)
    cellphone = Column(String(50), unique=True)
    profile_image_addr = Column(String(200))
    employee_id = Column(Numeric(38, 0, asdecimal=False))
    last_resetpwd_d = Column(DateTime)
    auto_reinvest = Column(Numeric(1, 0, asdecimal=False))
    parent_id = Column(Numeric(38, 0, asdecimal=False), index=True)
    register_channel_id = Column(Numeric(38, 0, asdecimal=False))
    credential_salt = Column(RAW)
    payment_password_salt = Column(RAW)

class Wallet(Base):
    __tablename__ = 'wm$wallet'
    __table_args__ = {u'schema': 'WMPROD'}
    table_tag = 'wm$'

    id = Column(Numeric(scale=0, asdecimal=True), primary_key=True)
    fname = Column(String(80))
    mname = Column(String(80))
    lname = Column(String(80))
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    type = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    status = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    balance = Column(Numeric(14, 2), nullable=False, server_default=text("0 "))
    pending_loads = Column(Numeric(14, 2), nullable=False, server_default=text("0 "))
    pending_withdrawals = Column(Numeric(14, 2), nullable=False, server_default=text("0 "))
    flags = Column(Numeric(scale=0, asdecimal=False), nullable=False, server_default=text("0 "))

class BorrowerConfig(Base):
    __tablename__ = 'sl$borrower_config'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(NUMBER(38), primary_key=True)
    name = Column(VARCHAR2(150))
    content = Column(CLOB)
    access_group = Column(VARCHAR2(1024))

class ActorBorrowerConfig(Base):
    __tablename__ = 'sl$actor_borrower_config'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    aid = Column(NUMBER(38), primary_key=True)
    config_id = Column(NUMBER(38))
    loan_app_id = Column(NUMBER(38))

class LoanApp(Base):
    __tablename__ = 'sl$loan_app'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    loan_id = Column(Numeric(asdecimal=False), primary_key=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    aid = Column(Numeric(asdecimal=False), nullable=False, unique=True)
    type = Column(Numeric(1, 0, asdecimal=False))
    status = Column(Numeric(2, 0, asdecimal=False))
    status_d = Column(DateTime)
    app_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    app_expire_d = Column(DateTime)
    name = Column(String(100))
    name_in_review = Column(String(80))
    description = Column(String(4000))
    description_in_review = Column(String(4000))
    purpose = Column(String(40))
    purpose_other = Column(String(120))
    desired_amnt = Column(Numeric(12, 2))
    desired_loan_type = Column(Numeric(1, 0, asdecimal=False))
    desired_duration = Column(Numeric(7, 0, asdecimal=False))
    app_amnt = Column(Numeric(12, 2))
    loan_type = Column(Numeric(1, 0, asdecimal=False))
    duration = Column(Numeric(7, 0, asdecimal=False))
    credit_class_id = Column(Numeric(3, 0, asdecimal=False), index=True)
    orig_fee_fraction = Column(Numeric(6, 6))
    lead_id = Column(String(60))
    prog_id = Column(Numeric(asdecimal=False), index=True)
    referer_id = Column(Numeric(asdecimal=False), index=True)
    parent_loan_id = Column(Numeric(asdecimal=False), index=True)
    ip_id = Column(Numeric(asdecimal=False), index=True)
    pi_id = Column(Numeric(asdecimal=False), index=True)
    cr_id = Column(Numeric(asdecimal=False), index=True)
    cv_id = Column(Numeric(asdecimal=False), index=True)
    ida_id = Column(Numeric(asdecimal=False), index=True)
    lap_proc_id = Column(Numeric(asdecimal=False), index=True)
    lc_debt_adj_dti = Column(Numeric(10, 2))
    dti4 = Column(Numeric(10, 2))
    entered_dob = Column(DateTime)
    orig_pi_id = Column(Numeric(asdecimal=False), index=True)
    orig_lc_debt_adj_dti = Column(Numeric(10, 2))
    orig_dti4 = Column(Numeric(10, 2))
    orig_income = Column(Numeric(15, 2))
    relation_to_prncp = Column(Numeric(2, 0, asdecimal=False))
    prncp_aid = Column(Numeric(asdecimal=False), index=True)
    prncp_pi_id = Column(Numeric(asdecimal=False), index=True)
    prncp_cr_id = Column(Numeric(asdecimal=False), index=True)
    prncp_cv_id = Column(Numeric(asdecimal=False), index=True)
    prncp_ida_id = Column(Numeric(asdecimal=False), index=True)
    prncp_lap_proc_id = Column(Numeric(asdecimal=False), index=True)
    prncp_lc_debt_adj_dti = Column(Numeric(10, 2))
    prncp_dti4 = Column(Numeric(10, 2))
    prncp_entered_dob = Column(DateTime)
    prncp_orig_pi_id = Column(Numeric(asdecimal=False), index=True)
    prncp_orig_dti4 = Column(Numeric(10, 2))
    prncp_orig_lc_debt_adj_dti = Column(Numeric(10, 2))
    prncp_orig_income = Column(Numeric(15, 2))
    agreement_id = Column(Numeric(asdecimal=False), index=True)
    til_doc_id = Column(Numeric(asdecimal=False), index=True)
    pn_doc_id = Column(Numeric(asdecimal=False), index=True)
    state_agree_doc_id = Column(Numeric(asdecimal=False))
    offer_take_d = Column(DateTime)
    auth_cnt = Column(Numeric(2, 0, asdecimal=False))
    base_cc_id = Column(Numeric(3, 0, asdecimal=False), index=True)
    flags = Column(Numeric(asdecimal=False))
    service_fee = Column(Numeric(12, 6))
    managment_fee = Column(Numeric(12, 6))
    payment_interest_mode = Column(Numeric(2, 0, asdecimal=False))
    upfront_management_fee = Column(Numeric(12, 6))
    reject_code = Column(Numeric(20, 0, asdecimal=False))
    industry_code = Column(Numeric(3, 0, asdecimal=False))
    company_code = Column(Numeric(3, 0, asdecimal=False))
    occupation_code = Column(Numeric(3, 0, asdecimal=False))
    credit_code = Column(Numeric(3, 0, asdecimal=False))
    review_flag = Column(Numeric(3, 0, asdecimal=False))
    interval_notification_rule = Column(Numeric(3, 0, asdecimal=False))
    payment_collection_frequency = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("2 "))
    early_payment_opportunity = Column(Numeric(8, 6))
    sales_description = Column(String(1000))
    loan_subtype = Column(Numeric(2, 0, asdecimal=False))
    first_payment_date = Column(DateTime)
    paid_off_date = Column(DateTime)
    desired_int_rate = Column(Numeric(8, 6))
    channel_id = Column(Numeric(38, 0, asdecimal=False))

class Pi(Base):
    __tablename__ = 'sl$pi'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    aid = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    src = Column(Numeric(2, 0, asdecimal=False))
    honourific = Column(Numeric(1, 0, asdecimal=False))
    fname = Column(String(80))
    lname = Column(String(80))
    mname = Column(String(80))
    ph1 = Column(String(25))
    ph2 = Column(String(25))
    ph_work = Column(String(25))
    fax = Column(String(25))
    addr_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    emp_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    dob = Column(DateTime)
    marital_status = Column(Numeric(1, 0, asdecimal=False))
    ssn = Column(String(40))
    ssn_type = Column(Numeric(1, 0, asdecimal=False))
    income = Column(Numeric(15, 2))
    inc_verifiable = Column(Numeric(1, 0, asdecimal=False))
    self_fico = Column(Numeric(2, 0, asdecimal=False))
    housing_status = Column(Numeric(1, 0, asdecimal=False))
    cumulative_job_tenure = Column(Numeric(4, 0, asdecimal=False))
    flags = Column(Numeric(scale=0, asdecimal=False))
    education_level = Column(String(80))
    other_income = Column(Numeric(15, 2))
    other_income_src = Column(Numeric(2, 0, asdecimal=False))
    paid_tax = Column(Numeric(2, 0, asdecimal=False))
    own_car_num = Column(Numeric(2, 0, asdecimal=False))
    own_house_num = Column(Numeric(2, 0, asdecimal=False))
    children_status = Column(Numeric(2, 0, asdecimal=False))
    asset_other = Column(String(100))
    debt_status = Column(Numeric(38, 0, asdecimal=False))
    income_cert = Column(Numeric(38, 0, asdecimal=False))
    wechat_acct = Column(String(200))
    pretax_income = Column(Numeric(15, 2))
    children_num = Column(Numeric(3, 0, asdecimal=False))
    work_start_date = Column(DateTime)
    domicile_live_diff = Column(Numeric(2, 0, asdecimal=False))
    remark = Column(String(500))

class Addr(Base):
    __tablename__ = 'sl$addr'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    aid = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    cr_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    frep_d = Column(DateTime)
    lrep_d = Column(DateTime)
    reported_cnt = Column(Numeric(5, 0, asdecimal=False))
    source = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    verify_status = Column(Numeric(1, 0, asdecimal=False))
    verify_status_d = Column(DateTime)
    type = Column(Numeric(1, 0, asdecimal=False))
    ownership = Column(Numeric(1, 0, asdecimal=False))
    rent_amt = Column(Numeric(6, 0, asdecimal=False))
    street_no = Column(String(10))
    street = Column(String(256))
    mail_stop = Column(String(120))
    city = Column(String(60))
    state = Column(String(5))
    zip = Column(String(15))
    country = Column(String(40))
    latitude = Column(Numeric(10, 0, asdecimal=False))
    longitude = Column(Numeric(10, 0, asdecimal=False))
    years_lived = Column(String(30))
    area = Column(String(100))

class CreditClass(Base):
    __tablename__ = 'sl$credit_class'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(3, 0, asdecimal=False), primary_key=True)
    name = Column(String(80), unique=True)
    grade = Column(String(3), nullable=False)
    maturity = Column(Numeric(7, 0, asdecimal=False), nullable=False)
    version = Column(DateTime, server_default=text("sysdate"))
    int_rate = Column(Numeric(8, 6), nullable=False)
    fico_min = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    fico_max = Column(Numeric(5, 0, asdecimal=False), nullable=False)
    pdf = Column(Numeric(7, 6))

class BdChannel(Base):
    __tablename__ = 'sl$bd_channel'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(10, 0, asdecimal=False), primary_key=True)
    name = Column(String(128))
    mgr_id = Column(Numeric(38, 0, asdecimal=False))
    referer_id = Column(Numeric(38, 0, asdecimal=False))
    total_amount = Column(Numeric(15, 2), server_default=text("0"))
    status = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    industry_code = Column(Numeric(3, 0, asdecimal=False))
    institution_code = Column(Numeric(3, 0, asdecimal=False))
    payment_day = Column(Numeric(2, 0, asdecimal=False))
    create_d = Column(DateTime, server_default=text("sysdate"))
    status_d = Column(DateTime, server_default=text("sysdate"))
    amount_d = Column(DateTime, server_default=text("sysdate"))
    type = Column(Numeric(2, 0, asdecimal=False), nullable=False, server_default=text("0 "))
    com_method = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    com_value = Column(Numeric(8, 2), server_default=text("0"))
    com_receiver = Column(Numeric(38, 0, asdecimal=False))

class WfRoleActor(Base):
    __tablename__ = 'sl$wf_role_actor'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    role_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True, nullable=False)
    actor_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True, nullable=False)

class WfResPerm(Base):
    __tablename__ = 'sl$wf_res_perm'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(38, 0, asdecimal=False), primary_key=True)
    type = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    name = Column(String(200), nullable=False)
    description = Column(String(200))
    res_type = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    res_id = Column(Numeric(38, 0, asdecimal=False))
    res_param = Column(String(1024))

class WfRoleResPerm(Base):
    __tablename__ = 'sl$wf_role_res_perm'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    role_id = Column(Numeric(38, 0, asdecimal=False), primary_key=True)
    perm_id = Column(Numeric(38, 0, asdecimal=False), primary_key=True)

class AssetLiability(Base):
    __tablename__ = 'sl$asset_liability'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(asdecimal=False), primary_key=True)
    loan_app_id = Column(Numeric(asdecimal=False), nullable=False)
    type = Column(Numeric(2, 0, asdecimal=False), server_default=text("0"))
    asset_type = Column(Numeric(2, 0, asdecimal=False))
    liability_type = Column(Numeric(2, 0, asdecimal=False))
    count = Column(Numeric(5, 0, asdecimal=False))
    house_addr = Column(String(250))
    house_estate = Column(String(250))
    all_owner = Column(String(100))
    relationship_with_applicant = Column(Numeric(10, 0, asdecimal=False))
    state = Column(Numeric(2, 0, asdecimal=False))
    loan_balance_status = Column(Numeric(2, 0, asdecimal=False))
    mortgage_status = Column(Numeric(2, 0, asdecimal=False))
    amount = Column(Numeric(12, 2))
    flag = Column(Numeric(2, 0, asdecimal=False))
    event_date = Column(DateTime)
    house_area = Column(Numeric(8, 3))
    loan_balance = Column(Numeric(12, 2))
    house_provide = Column(Numeric(2, 0, asdecimal=False))
    house_type = Column(Numeric(2, 0, asdecimal=False))
    second_house = Column(Numeric(2, 0, asdecimal=False))
    land_type = Column(Numeric(2, 0, asdecimal=False))
    mortgage_pledge_type = Column(Numeric(2, 0, asdecimal=False))
    mortgage_pledge_sub_type = Column(Numeric(2, 0, asdecimal=False))
    evaluate_type = Column(Numeric(2, 0, asdecimal=False))
    authority_number = Column(String(100))
    remark = Column(String(500))
    guarantee_type = Column(Numeric(2, 0, asdecimal=False))
    house_city = Column(String(60))

class BdLoanApp(Base):
    __tablename__ = 'sl$bd_loan_app'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    loan_app_id = Column(Numeric(38, 0, asdecimal=False), primary_key=True)
    channel_id = Column(Numeric(38, 0, asdecimal=False), nullable=False)
    name = Column(String(80))
    ssn = Column(String(40))
    cellphone = Column(String(25))
    company_name = Column(String(120))
    reg_code = Column(String(120))
    reg_no = Column(String(120))

class BonusPointRule(Base):
    __tablename__ = 'sl$bonus_point_rule'
    table_tag = 'sl$'

    id = Column(Integer, primary_key=True, server_default=text("'0'"))
    event_type = Column(String(64, u'utf8_unicode_ci'), nullable=False, unique=True)
    description = Column(String(256, u'utf8_unicode_ci'))
    rule_class_name = Column(String(256, u'utf8_unicode_ci'))
    point_formula = Column(String(256, u'utf8_unicode_ci'))
    start_date = Column(Date)
    end_date = Column(Date)
    daily_max_point = Column(BigInteger, server_default=text("'-1'"))
    max_point = Column(BigInteger, server_default=text("'-1'"))
    updated_date = Column(DateTime)
    active = Column(Integer, nullable=False)

class DrCoinRule(Base):
    __tablename__ = 'sl$dr_coin_rule'
    table_tag = 'sl$'

    id = Column(Integer, primary_key=True, server_default=text("'0'"))
    event_type = Column(String(64, u'utf8_unicode_ci'), nullable=False, unique=True)
    description = Column(String(256, u'utf8_unicode_ci'))
    rule_class_name = Column(String(256, u'utf8_unicode_ci'))
    point_formula = Column(String(256, u'utf8_unicode_ci'))
    start_date = Column(Date)
    end_date = Column(Date)
    onetime_max_amount = Column(Numeric(20, 6), server_default=text("'-1.000000'"))
    daily_max_amount = Column(Numeric(20, 6), server_default=text("'-1.000000'"))
    max_amount = Column(Numeric(20, 6), server_default=text("'-1.000000'"))
    updated_date = Column(DateTime)
    active = Column(Integer, nullable=False)

class VipLevelRule(Base):
    __tablename__ = 'sl$vip_level_rule'
    table_tag = 'sl$'

    id = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    vip_level = Column(Integer)
    point_range = Column(BigInteger, server_default=text("'-1'"))
    principal_range = Column(BigInteger, server_default=text("'-1'"))
    bonus_point_rate = Column(Numeric(6, 2), server_default=text("'100.00'"))
    daily_point_rate = Column(Numeric(6, 2), server_default=text("'100.00'"))
    dr_coin_rate = Column(Numeric(6, 2), server_default=text("'100.00'"))
    daily_dr_coin_rate = Column(Numeric(6, 2), server_default=text("'100.00'"))
    description = Column(String(256, u'utf8_unicode_ci'), server_default=text("''"))
    updated_date = Column(DateTime)

class VipProfile(Base):
    __tablename__ = 'sl$vip_profile'
    table_tag = 'sl$'

    aid = Column(BigInteger, primary_key=True, server_default=text("'0'"))
    acc_bonus_point = Column(BigInteger, server_default=text("'0'"))
    daily_acc_point = Column(BigInteger, server_default=text("'0'"))
    acc_vip_level = Column(Integer, server_default=text("'0'"))
    last_downgrade_date = Column(DateTime)
    last_daily_job_time = Column(DateTime)
    acc_dr_coin_amount = Column(Numeric(20, 6), server_default=text("'0.000000'"))
    daily_acc_dr_coin_amount = Column(Numeric(20, 6), server_default=text("'0.000000'"))
    last_daily_bonus_point = Column(BigInteger, server_default=text("'0'"))
    total_bonus_point = Column(BigInteger, server_default=text("'0'"))
    last_daily_dr_coin_amount = Column(Numeric(20, 6), server_default=text("'0.000000'"))
    total_dr_coin_amount = Column(Numeric(20, 6), server_default=text("'0.000000'"))

class ActorMasterMapping(Base):
    __tablename__ = 'sl$actor_master_mapping'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    create_time = Column(DateTime)
    aid = Column(Numeric(scale=0, asdecimal=False))
    master_aid = Column(Numeric(scale=0, asdecimal=False))


class AccountBinding(Base):
    __tablename__ = 'sl$account_binding'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    account_id = Column(Numeric(22), nullable=True)
    agreement_no = Column(String(120))
    channel_type_id = Column(Numeric(8), nullable=True)
    ID = Column(Numeric(22), primary_key=True)
    resv1 = Column(String(60))
    resv2 = Column(String(120))
    resv3 = Column(Numeric(8))
    resv4 = Column(Numeric(20))
    verification_type_id = Column(Numeric(8))
    selected_status = Column(Numeric(1))
    channel_bank_code = Column(Numeric(120))


class Account(Base):
    __tablename__ = 'sl$account'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    aid = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    creation_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    type = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    name = Column(String(80))
    total_funds = Column(Numeric(22, 12))
    locked_funds = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))
    ext_holder_fname = Column(String(80))
    ext_holder_lname = Column(String(80))
    ext_holder_mname = Column(String(80))
    ext_institution = Column(String(80))
    acc_n = Column(String(80))
    brn = Column(String(80))
    bs_fs_id = Column(Numeric(scale=0, asdecimal=False))
    bs_w_id = Column(Numeric(scale=0, asdecimal=False))
    verify = Column(Numeric(4, 2))
    status_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    authorization_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    refresh_d = Column(DateTime)
    city = Column(String(60))
    state = Column(String(30))
    ext_branch_name = Column(String(80))
    reserved_phone = Column(String(20))

dr_coin_log = Table(
    'sl$dr_coin_log', metadata,
    Column('aid', BigInteger),
    Column('event_type', String(64, u'utf8_unicode_ci')),
    Column('amount', Numeric(20, 6), server_default=text("'0.000000'")),
    Column('event_args', String(256, u'utf8_unicode_ci')),
    Column('award_date', DateTime, index=True),
    Index('dr_coin_log_idx', 'aid', 'event_type')
)
dr_coin_log.table_tag = 'sl$'

class Loan(Base):
    __tablename__ = 'sl$loan'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    aid = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    acc_id = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    app_amnt = Column(Numeric(12, 2), nullable=False)
    duration = Column(Numeric(7, 0, asdecimal=False), nullable=False)
    type = Column(Numeric(2, 0, asdecimal=False))
    name = Column(String(100))
    amount = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))
    orig_fee = Column(Numeric(8, 2), nullable=False, server_default=text("0 "))
    int_rate = Column(Numeric(8, 6))
    term_penalty = Column(Numeric(6, 6))
    apr = Column(Numeric(8, 6))
    grade = Column(String(3))
    credit_class_id = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    start_d = Column(DateTime)
    book_d = Column(DateTime)
    interval_unit = Column(Numeric(1, 0, asdecimal=False), server_default=text("2"))
    interval = Column(Numeric(6, 0, asdecimal=False))
    originator = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    rpa = Column(Numeric(12, 2))
    pay_day = Column(Numeric(2, 0, asdecimal=False))
    pay_day_change_cnt = Column(Numeric(2, 0, asdecimal=False))
    status = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    status_d = Column(DateTime, server_default=text("sysdate"))
    sec_status = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    curr_lpay_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    next_lpay_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    waroic = Column(Numeric(8, 6))
    flags = Column(Numeric(scale=0, asdecimal=False))
    ytm = Column(Numeric(asdecimal=False))
    sold_to = Column(Numeric(3, 0, asdecimal=False))
    sold_d = Column(DateTime)
    review_flag = Column(Numeric(2, 0, asdecimal=False))
    rel_loan_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    vflag = Column(Numeric(2, 0, asdecimal=False))
    auto_issue = Column(Numeric(1, 0, asdecimal=False), server_default=text("0"))
    min_note_amount = Column(Numeric(scale=0, asdecimal=False))
    max_invest_amount = Column(Numeric(scale=0, asdecimal=False))
    subtype = Column(Numeric(2, 0, asdecimal=False))

class Lpd(Base):
    __tablename__ = 'sl$lpd'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    lp_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True, nullable=False, index=True)
    loan_id = Column(Numeric(scale=0, asdecimal=False), primary_key=True, nullable=False, index=True)
    note_id = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    parent_lp_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    amount = Column(Numeric(12, 2), nullable=False)
    new_amnt = Column(Numeric(22, 12), nullable=False)
    prncp_at_trade = Column(Numeric(22, 12), nullable=False)
    received_prncp = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))
    received_int = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))
    received_fee = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))
    received_lcfee = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))
    buy_price = Column(Numeric(12, 2), nullable=False)
    buy_d = Column(DateTime, server_default=text("sysdate"))
    sell_price = Column(Numeric(12, 2))
    status = Column(Numeric(2, 0, asdecimal=False), nullable=False, index=True)
    status_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    rpa = Column(Numeric(12, 2))
    prtf_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    type = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    int_adjustment = Column(Numeric(22, 12), nullable=False, server_default=text("0 "))

class BonusPointLog(Base):
    __tablename__ = 'sl$bonus_point_log'
    table_tag = 'sl$'

    aid = Column(BigInteger)
    event_type = Column(String(64, u'utf8_unicode_ci'))
    point = Column(Integer, server_default=text("'0'"))
    event_args = Column(String(256, u'utf8_unicode_ci'))
    award_date = Column(DateTime)
    vip_level = Column(Integer, server_default=text("'0'"))
    event_type_desc = Column(String(255, u'utf8_unicode_ci'))
    acc_point = Column(BigInteger, server_default=text("'0'"))
    principal_point = Column(BigInteger, server_default=text("'0'"))
    id = Column(BigInteger, primary_key=True)

class ChallengeLog(Base):
    __tablename__ = 'sl$challenge_log'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    aid = Column(Numeric(scale=0, asdecimal=False), nullable=False)
    target = Column(String(200), nullable=False)
    ip_addr = Column(String(40))
    type = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    challenge_d = Column(DateTime)
    create_d = Column(DateTime)
    action = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    result = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    result_code = Column(String(250))

class CfgItem(Base):
    __tablename__ = 'sl$cfg_item'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    cfg_id = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    key = Column(String(120), nullable=False)
    val = Column(String(3500))

class Lpay(Base):
    __tablename__ = 'sl$lpay'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    loan_id = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    prncp_out = Column(Numeric(22, 12), nullable=False)
    prncp_paid = Column(Numeric(22, 12), nullable=False)
    prncp_bal = Column(Numeric(22, 12), nullable=False)
    int_accr = Column(Numeric(22, 12), nullable=False)
    int_paid = Column(Numeric(22, 12), nullable=False)
    int_bal = Column(Numeric(22, 12), nullable=False)
    fee_accr = Column(Numeric(12, 2), nullable=False)
    fee_paid = Column(Numeric(12, 2), nullable=False)
    fee_bal = Column(Numeric(12, 2), nullable=False)
    lcfee_accr = Column(Numeric(12, 2), nullable=False)
    lcfee_paid = Column(Numeric(12, 2), nullable=False)
    lcfee_bal = Column(Numeric(12, 2), nullable=False)
    type = Column(Numeric(1, 0, asdecimal=False), nullable=False, server_default=text("1 "))
    status = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    status_d = Column(DateTime)
    due_d = Column(DateTime)
    due_amt = Column(Numeric(12, 2))
    pull_d = Column(DateTime)
    pull_amt = Column(Numeric(12, 2))
    received_d = Column(DateTime)
    received_amt = Column(Numeric(12, 2))
    case_id = Column(String(36))
    roi = Column(Numeric(asdecimal=False))
    ytm = Column(Numeric(asdecimal=False))
    sl_managment_fee_accr = Column(Numeric(22, 12))
    sl_managment_fee_paid = Column(Numeric(22, 12))
    sl_managment_fee_ba = Column(Numeric(22, 12))
    fee_d = Column(DateTime)

class Employment(Base):
    __tablename__ = 'sl$employment'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    aid = Column(Numeric(scale=0, asdecimal=False), nullable=False, index=True)
    cr_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    frep_d = Column(DateTime)
    lrep_d = Column(DateTime)
    reported_cnt = Column(Numeric(5, 0, asdecimal=False))
    source = Column(Numeric(1, 0, asdecimal=False), nullable=False)
    verify_status = Column(Numeric(1, 0, asdecimal=False))
    verify_status_d = Column(DateTime)
    title = Column(String(80))
    occupation = Column(Numeric(2, 0, asdecimal=False))
    status = Column(Numeric(1, 0, asdecimal=False))
    emp_name = Column(String(120))
    salary = Column(Numeric(15, 2))
    url = Column(String(200))
    emp_addr_id = Column(Numeric(scale=0, asdecimal=False), index=True)
    start_d = Column(DateTime)
    end_d = Column(DateTime)
    misc = Column(Numeric(scale=0, asdecimal=False))
    company_size = Column(String(30))
    company_segment = Column(String(40))
    company_phone = Column(String(25))
    company_type = Column(String(40))
    establish_d = Column(DateTime)
    applicant_share = Column(Numeric(12, 6))
    org_code = Column(String(250))
    reg_no = Column(String(250))
    emp_opt_addr_id = Column(Numeric(asdecimal=False), index=True)
    opt_income = Column(Numeric(12, 2))
    opt_cost = Column(Numeric(12, 2))
    profit = Column(Numeric(12, 6))
    customers = Column(String(250))
    suppliers = Column(String(250))
    loan_state = Column(Numeric(2, 0, asdecimal=False))
    mortgage_state = Column(Numeric(2, 0, asdecimal=False))
    lawsuit_state = Column(Numeric(2, 0, asdecimal=False))
    paid_tax_state = Column(Numeric(2, 0, asdecimal=False))
    profession = Column(Numeric(2, 0, asdecimal=False))
    reg_name = Column(String(120))
    merchant_no = Column(String(4000))
    calculated_income = Column(Numeric(15, 2))
    mcc_code = Column(String(250))
    remark = Column(String(500))
    nature_company_location = Column(Numeric(2, 0, asdecimal=False))
    manage_related_company = Column(Numeric(2, 0, asdecimal=False))
    profession_start_d = Column(DateTime)
    history_bad_record = Column(Numeric(2, 0, asdecimal=False))
    loan_app_id = Column(Numeric(scale=0, asdecimal=False))


class QrtzTrigger(Base):
    __tablename__ = 'qrtz_triggers'
    __table_args__ = {u'schema': 'quartz'}
    table_tag = 'qrtz_triggers'

    sched_name = Column(String(120), primary_key=True, nullable=False)
    trigger_name = Column(String(200), primary_key=True, nullable=False)
    trigger_group = Column(String(200), primary_key=True, nullable=False)
    job_name = Column(String(200), nullable=False)
    job_group = Column(String(200), nullable=False)
    description = Column(String(250))
    next_fire_time = Column(Numeric(13, 0, asdecimal=False))
    prev_fire_time = Column(Numeric(13, 0, asdecimal=False))
    priority = Column(Numeric(13, 0, asdecimal=False))
    trigger_state = Column(String(16), nullable=False)
    trigger_type = Column(String(8), nullable=False)
    start_time = Column(Numeric(13, 0, asdecimal=False), nullable=False)
    end_time = Column(Numeric(13, 0, asdecimal=False))
    calendar_name = Column(String(200))
    misfire_instr = Column(Numeric(2, 0, asdecimal=False))
    job_data = Column(LargeBinary)


class Sr(Base):
    __tablename__ = 'sl$sr'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    filer_id = Column(Numeric, index=True)
    filer_email = Column(String(100))
    assignee_id = Column(Numeric, nullable=False, index=True)
    summary = Column(String(400))
    description = Column(Text)
    priority = Column(Numeric(2, 0, asdecimal=False))
    severity = Column(Numeric(2, 0, asdecimal=False))
    type = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    subject = Column(Numeric(2, 0, asdecimal=False), nullable=False, index=True)
    topic = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    status = Column(Numeric(2, 0, asdecimal=False), nullable=False, index=True)
    aid = Column(Numeric, index=True)
    loan_id = Column(Numeric, index=True)
    trans_id = Column(Numeric, index=True)
    dup_of_sr_id = Column(Numeric, index=True)
    dep_on_sr_id = Column(Numeric, index=True)
    cost_estimate_orig = Column(Numeric(6, 1))
    cost_estimate = Column(Numeric(6, 1))
    hours_worked = Column(Numeric(6, 1))
    hours_left = Column(Numeric(6, 1))
    due_d = Column(DateTime)
    impersonate_level = Column(Numeric(1, 0, asdecimal=False))
    flags = Column(Numeric(scale=0, asdecimal=False))


class SrNote(Base):
    __tablename__ = 'sl$sr_note'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(scale=0, asdecimal=False), primary_key=True)
    sr_id = Column(Numeric, nullable=False, index=True)
    creator = Column(String, nullable=False, index=True)
    create_d = Column(DateTime, nullable=False, server_default=text("sysdate "))
    type = Column(Numeric(3, 0, asdecimal=False), nullable=False)
    note = Column(Text)
    event_d = Column(DateTime)
    scheduled_d = Column(DateTime)
    flags = Column(Numeric(scale=0, asdecimal=False))



class EntityProp(Base):
    __tablename__ = 'sl$entity_prop'
    __table_args__ = {u'schema': 'SLPROD'}
    table_tag = 'sl$'

    id = Column(Numeric(38, 0, asdecimal=False), primary_key=True)
    entity_type = Column(Numeric(10, 0, asdecimal=False), nullable=False)
    entity_id = Column(Numeric(38, 0, asdecimal=False), nullable=False)
    key = Column(Numeric(38, 0, asdecimal=False), nullable=False)
    nval = Column(Numeric(38, 10))
    enabled = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    sval = Column(String(400))
