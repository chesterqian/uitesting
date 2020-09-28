# -*- coding:utf-8 -*-
"""
Created on Sep 21, 2013

@author: Chester.Qian
"""
import re
from functools import wraps
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_
from sqlalchemy import desc, asc, text
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
import pymysql
from common.global_config import Global

ENVIRONMENT_MAP_DB_CONNECTIONS = {
    "supergw_uat": (Global.DBConnect.UatSwgMySqlDB,),
    "cif_uat": (Global.DBConnect.UatCifMySqlDB,),
    "spw": (Global.DBConnect.PerfSwgMySqlDB,),
    "cif": (Global.DBConnect.PerfCifMySqlDB,)
}


def get_database_type_map_connection_info(environment, database_type):
    connections = ENVIRONMENT_MAP_DB_CONNECTIONS[environment]
    iterator = iter(connections)
    while True:
        try:
            db_connection_cls = iterator.next()
            name = db_connection_cls.__name__.lower()
            if re.search(database_type, name):
                return db_connection_cls.ENGINE_URL_PATTERN, db_connection_cls.DB_CONNECT_INFO
        except StopIteration:
            break
    raise Exception("no db connections info found!")


def connect_to_database(*tables_cls, **kwargs):
    """
    DB connection and session management
    Multiple cross database support
    e.g.
    connect_to_database(tableA_from_db1, tableB_from_db1, tablec_from_db2, etc..)
    def get_actor(self, email):
        ...
        ...
        ...

    When get_actor is called :
    1.Firstly engines for db1 and db2 will be created separately.
    2.After get_actor is finished, those sessions will be closed and removed from db factory.
    """
    sql_mode = 'sql_mode' in kwargs and kwargs['sql_mode'] or 'ORM'

    def deco(func):
        @wraps(func)
        def wrapper(database_factory, *args, **kwargs):
            session_should_be_closed = False
            try:
                # handle all tables, which are input to do things like 'DB
                # connection and session management'
                for table_cls in tables_cls:
                    database_tag = hasattr(table_cls,
                                           'table_tag') and table_cls.table_tag
                    if not database_tag:
                        raise Exception(
                            "%s database_tag is invalid or not set." % table_cls.__name__)

                    environment = database_factory.environment
                    database_type = database_factory.database_type
                    connect_string_pattern, connect_info_map = \
                        get_database_type_map_connection_info(environment,
                                                              database_type)
                    # decide which connection url to be used
                    connect_info = connect_info_map[database_tag]
                    session_existed = database_tag in database_factory.database_tag_map_session
                    engine_pool = database_factory.engine_pool
                    # create and add engine to engine_pool if the db has never
                    # been acquired
                    if database_tag not in engine_pool:
                        engine = database_factory._build_engine(
                            connect_string_pattern % connect_info)

                        engine_pool.update({database_tag: engine})
                    else:
                        database_factory.engine = engine_pool[database_tag]

                    engine = engine_pool[database_tag]

                    if sql_mode == 'ORM':
                        # create and add session to database_tag_map_session if
                        # the session has never been acquired
                        if not session_existed:
                            Session = sessionmaker(bind=engine)
                            session = Session()
                            database_factory.database_tag_map_session.update(
                                {database_tag: session})
                            session_should_be_closed = True
                    elif sql_mode == 'RAW':
                        database_factory.connection = engine.connect()
                    else:
                        raise Exception("sql_mode %s is invalid." % sql_mode)

                try:
                    # calling decorated function between context
                    result = func(database_factory, *args, **kwargs)
                finally:
                    if session_should_be_closed:
                        # close all db session if necessary
                        awaiting_objects = database_factory.database_tag_map_session
                        for k in awaiting_objects:
                            getattr(awaiting_objects[k], 'close')()

                return result
            finally:
                if sql_mode == "RAW":
                    if database_factory:
                        database_factory.connection.close()
                        database_factory.connection = None

                if session_should_be_closed:
                    database_factory.database_tag_map_session = {}

        return wrapper

    return deco


class SessionProvider(object):
    """
    A reflected class for session as a proxy
    to provide different sessions for different db tables
    """

    def __init__(self, database_factory):
        self.database_factory = database_factory

    def __getattr__(self, attribute):
        def wrapper(target, *args, **kwargs):
            mapper = self.database_factory.database_tag_map_session
            table_cls = hasattr(target, "class_") and target.class_ \
                        or target
            database_tag = hasattr(table_cls, 'table_tag') \
                           and table_cls.table_tag

            if not database_tag:
                raise Exception("database_tag %s is invalid." % database_tag)

            result = None
            try:
                session = mapper[database_tag]
                if session:
                    attr_map_params = {
                        "query": (target,),
                        "commit": ()}
                    try:
                        params = attr_map_params[attribute]
                    except KeyError:
                        if hasattr(session, attribute):
                            params = args
                        else:
                            raise Exception(
                                'Attribute not available: %s' % attribute)
                    try:
                        result = getattr(session, attribute)(*params, **kwargs)
                    except SQLAlchemyError, e:
                        session.rollback()
                        raise Exception(e)
            except KeyError:
                raise Exception('Session is not available!')

            return result

        return wrapper


class DataBaseFactory(object):
    def __init__(self, environment="demo", database_type="oracle"):
        # environment is "demo" or "dev" or "vip"
        # database_type is "oracle" or "mysql"
        self.database_type = database_type
        self.environment = environment
        self.engine_pool = {}
        self.connection = None
        self.session = None
        self.tables_cls = None
        self.tables_name = None
        self.database_tag_map_session = {}
        self.session_provider = SessionProvider(self)

    def _build_engine(self, connect_string):
        # build engine parameter to connect data table
        parameters = self.database_type is "oracle" and {"echo": True,
                                                         "arraysize": 50,
                                                         "coerce_to_unicode": True} or \
                     self.database_type is "mysql" and {"echo": True}
        self.engine = create_engine(connect_string, **parameters)
        return self.engine

    def select_table(self, select_string):
        result = self.connection.execute(select_string)
        self.connection.close()

        return result

    def update_table(self, update_string):
        with self.connection.begin() as trans:
            try:
                self.connection.execute(update_string)
                trans.commit()
            except SQLAlchemyError:
                trans.rollback()
            finally:
                self.connection.close()

    def refresh_record(self, record, column_name=None):
        self.session_provider.refresh(record, record, column_name)

        return record

    def update_record_for_table(self, table_model, update_columns, **filters):
        if not isinstance(update_columns, dict):
            raise Exception("Please provide valid filters or update columns.")

        if not filters:
            raise Exception("Please provide valid filters.")

        filters = [getattr(table_model, k) == v
                   for k, v in filters.items()]

        self.session_provider.query(table_model).filter(*filters). \
            update(update_columns, synchronize_session='fetch')
        self.session_provider.commit(table_model)

    def delete_record_from_table(self, table_model, **filters):
        if not filters:
            raise Exception("Please provide valid filters.")
        query_filter = [getattr(table_model, k) == v
                        for k, v in filters.items()]
        self.session_provider.query(table_model).filter(*query_filter).delete()
        self.session_provider.commit(table_model)

    def get_record_from_table(self, table_model, query_columns=[],
                              order_by_column_name=None, query_func="one",
                              **filters):
        """
        此方法用于查询单个数据库表。
        :param table_model: 数据库表的映射类
        :param query_columns: 查询的数据库表对应的列值，比如查询actor表中的id和name，
                            query_columns=['id', 'name']
        :param order_by_column_name: 由排列模式、_、列名组成，比如根据创建时间降序
                                    排列，则order_by_column_name='desc_create_d'
        :param query_func: 查询函数，默认是one，例如还可为first、all等
        :param filters: 查询字典，比如根据email查询，filters传入为
                        email='test@sl.com'
        """
        if not query_columns:
            sql = self.session_provider.query(table_model)
        else:
            query_columns = [getattr(table_model, column)
                             for column in query_columns]
            sql = self.session_provider.query(*query_columns)

        if not filters:
            sql = sql
        else:
            query_filter = []
            for k, v in filters.items():
                if isinstance(v, list):
                    flt = [getattr(table_model, k) == i for i in v]
                    query_filter.append(or_(*flt))
                else:
                    query_filter.append(getattr(table_model, k) == v)
            sql = sql.filter(*query_filter)

        if not order_by_column_name:
            sql = sql
        else:
            order_by_mode, order_by_column = order_by_column_name.split("_", 1)
            if order_by_mode == "desc":
                sql = sql.order_by(desc(getattr(table_model, order_by_column)))
            else:
                sql = sql.order_by(asc(getattr(table_model, order_by_column)))

        result = getattr(sql, query_func)()
        return result

    def get_record_from_joined_tables(self, table_cls_1, table_cls_2,
                                      joined_keys=[],
                                      order_by_column_1=None,
                                      order_by_column_2=None,
                                      query_func_1='one', query_func_2='one',
                                      **filters_1):
        if not joined_keys:
            raise Exception("Please provide exact joined keys.")

        result_temp = self.get_record_from_table(
            table_cls_1,
            order_by_column_name=order_by_column_1,
            query_func=query_func_1, **filters_1)

        filters_2 = {joined_keys[1]: str(getattr(result_temp, joined_keys[0]))}

        result = self.get_record_from_table(
            table_cls_2,
            order_by_column_name=order_by_column_2,
            query_func=query_func_2, **filters_2)
        return result

    def get(self, table_cls, order_by_column_name=None, result_mode="all",
            limit=10, **filters):
        """
        :param order_by_column_name: 由排列模式、_、列名组成，比如根据创建时间降序
                            排列，则order_by_column_name='desc_create_d'
        :param phone_number: 11位手机号码
        :param filters: 查询字典，比如根据email查询，filters传入为
                        email='test@sl.com'
        """
        sql_query = self.session_provider.query(table_cls).filter_by(
            **filters)

        if order_by_column_name:
            order_by_mode, order_by_column = order_by_column_name.split("_", 1)
            order_by_func = getattr(sqlalchemy, order_by_mode)
            sql_query = sql_query.order_by(
                order_by_func(getattr(table_cls, order_by_column)))

        return getattr(sql_query.limit(limit), result_mode)()

    def get_like(self, db_cls, col, value):
        r = self.session_provider.query(db_cls).filter(getattr(db_cls, col).like(value)).all()
        return r

if __name__ == '__main__':
    engine = create_engine("mysql+pymysql://dbexecute:dbexecute321@10.199.101.18:3306/cif_uat", echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()