# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

from common import sgw_database_tag

Base = declarative_base()
metadata = Base.metadata


class SgwCert(Base):
    __tablename__ = 'sgw_cert'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    channel_system_id = Column(String(32))
    private_key = Column(String(1024))
    public_key = Column(String(1024))
    com_key = Column(String(1024))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    memo = Column(String(256))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwChannelSystem(Base):
    __tablename__ = 'sgw_channel_system'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    channel_system_id = Column(String(16), nullable=False, server_default=text("''"))
    channel_system_name = Column(String(32))
    from_channel_system_id = Column(String(16))
    to_channel_system_id = Column(String(32))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    memo = Column(String(256), server_default=text("''"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwCheckAccountFile(Base):
    __tablename__ = 'sgw_check_account_file'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    channel_system_id = Column(String(32), nullable=False, server_default=text("''"))
    trans_type_id = Column(String(16), nullable=False, server_default=text("''"))
    file_path = Column(String(128))
    workdate = Column(String(16), nullable=False, server_default=text("''"))
    status = Column(String(16))
    memo = Column(String(16))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    lock_status = Column(String(16))


class SgwCheckParseTransaction(Base):
    __tablename__ = 'sgw_check_parse_transaction'
    table_tag = sgw_database_tag

    id = Column(BigInteger, primary_key=True)
    channel_system_id = Column(String(32), nullable=False, server_default=text("''"))
    trans_type_id = Column(String(16), nullable=False, server_default=text("''"))
    order_no = Column(String(64), nullable=False, server_default=text("''"))
    amt = Column(String(64))
    status = Column(String(16))
    workdate = Column(String(16))
    tradeacco = Column(String(32))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    memo = Column(String(2048))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwCommunication(Base):
    __tablename__ = 'sgw_communication'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    protocol_type = Column(String(16))
    trans_type_id = Column(String(16), nullable=False, server_default=text("''"))
    channel_system_id = Column(String(32), nullable=False)
    uri = Column(String(128))
    timeout = Column(String(8))
    memo = Column(String(256))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwCustIdentityVerify(Base):
    __tablename__ = 'sgw_cust_identity_verify'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    idno = Column(String(18), nullable=False)
    invnm = Column(String(20), nullable=False)
    photo_address = Column(String(200))
    status = Column(String(10))
    is_mate = Column(String(1))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    out_order_no = Column(String(32), nullable=False)


class SgwLogonStatu(Base):
    __tablename__ = 'sgw_logon_status'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    channel_system_id = Column(String(32), nullable=False, server_default=text("''"))
    session_id = Column(String(64))
    status = Column(String(16))
    expire_time = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwMessageParam(Base):
    __tablename__ = 'sgw_message_param'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    channel_system_id = Column(String(32), nullable=False, server_default=text("''"))
    param_name = Column(String(64))
    param_value = Column(String(64))
    memo = Column(String(64))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwMsgTemplate(Base):
    __tablename__ = 'sgw_msg_template'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    template_id = Column(String(40), nullable=False)
    template_name = Column(String(40), nullable=False, server_default=text("''"))
    template_type = Column(Integer, nullable=False, server_default=text("'0'"))
    template = Column(String(500))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwSm(Base):
    __tablename__ = 'sgw_sms'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    sgw_sms_mobile = Column(String(11), nullable=False, server_default=text("''"))
    sgw_sms_content = Column(String(5000), nullable=False, server_default=text("''"))
    sgw_sms_status = Column(String(16), nullable=False, server_default=text("''"))
    sgw_sms_channel = Column(String(16), nullable=False, server_default=text("''"))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    out_order_no = Column(String(32), nullable=False)
    template_id = Column(String(40), nullable=False, server_default=text("''"))


class SgwTransactionContent(Base):
    __tablename__ = 'sgw_transaction_content'
    table_tag = sgw_database_tag

    id = Column(BigInteger, primary_key=True)
    transaction_online_id = Column(BigInteger, nullable=False)
    trans_type_id = Column(String(16))
    from_trans_content_req = Column(String(2560))
    from_trans_content_res = Column(String(4000))
    to_trans_content_req = Column(String(2560))
    to_trans_content_res = Column(String(4000))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    memo = Column(String(256))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwTransactionOnline(Base):
    __tablename__ = 'sgw_transaction_online'
    table_tag = sgw_database_tag

    id = Column(BigInteger, primary_key=True)
    out_order_no = Column(String(32))
    trans_type_id = Column(String(16))
    status = Column(String(16))
    retry_count = Column(String(2))
    gmt_sended = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
    gmt_returned = Column(DateTime)
    trans_result = Column(String(16))
    is_sync = Column(String(2), nullable=False, server_default=text("'0'"))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    memo = Column(String(255))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwTransactionOnlineMapping(Base):
    __tablename__ = 'sgw_transaction_online_mapping'
    table_tag = sgw_database_tag

    id = Column(BigInteger, primary_key=True)
    out_order_no = Column(String(32))
    refer_order_no = Column(String(64))
    inner_order_no = Column(String(64))
    first_order_no = Column(String(64))
    second_order_no = Column(String(64))
    third_order_no = Column(String(64))
    memo = Column(String(255))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwTransactionType(Base):
    __tablename__ = 'sgw_transaction_type'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    channel_system_id = Column(String(16))
    trans_type_id = Column(String(16), nullable=False, server_default=text("''"))
    trans_type_name = Column(String(32))
    max_counter = Column(String(2))
    uniqueable = Column(String(1))
    uri = Column(String(128))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    memo = Column(String(256))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SgwTransactionUnique(Base):
    __tablename__ = 'sgw_transaction_unique'
    table_tag = sgw_database_tag

    id = Column(BigInteger, primary_key=True)
    out_order_no = Column(String(32), nullable=False, server_default=text("''"))
    trans_type_id = Column(String(16), nullable=False, server_default=text("''"))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))


class SupergwBankcardValidLog(Base):
    __tablename__ = 'supergw_bankcard_valid_log'
    table_tag = sgw_database_tag

    id = Column(Integer, primary_key=True)
    out_order_no = Column(String(32))
    bank_acco = Column(String(28))
    id_no = Column(String(30))
    invnm = Column(String(40))
    mobile_no = Column(String(20))
    accept_md = Column(String(1))
    valid_result = Column(String(1))
    is_delete = Column(Integer, nullable=False, server_default=text("'0'"))
    created_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    updated_at = Column(DateTime, nullable=False, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
