# -*- coding:utf-8 -*-

__author__ = 'Shirley'

from common.lib.json_handler import handle_item_in_json
from database.database_config import DATABASE_OPERATOR_MAP_TABLE_METHOD, DATABASE_OPERATOR_MAP_TAG_AND_TYPE


class DatabaseAssertion(object):

    def __init__(self, database_tag='demo', database_type='oracle'):
        self.database_tag = database_tag
        self.database_type = database_type
        self._operator = None

    @property
    def operator(self):
        if not self._operator:
            self._operator = self._get_database_operator()
        return self._operator

    def _get_database_operator(self):
        """
        通过database_tag和database_type决定操作哪个数据库operator.
        """
        operator_key = self.database_tag + '_' + self.database_type
        operator = DATABASE_OPERATOR_MAP_TAG_AND_TYPE[operator_key]

        return operator

    def get_column_value_from_table(self, query_data):
        """
        查询某些表的某些列数据，目前支持单表查询、多表联合查询、多次查询单表。
        限制条件：每次查询数据返回只限一条。
        :param query_data: 格式为json
        例子一：查询单表，查询语句需要一个参数，返回某一列数据
        query_data = {
            "tables":
                {
                    "Actor": {
                        "columns": "id",
                        "args": "email"
                    }
                }
        }
        例子二：查询单表，查询语句需要多个参数，返回多列数据
        query_data = {
            "tables": {
                "Loan": {
                    "columns": ["id", "name"],
                    "args": ["loan_id", "status"]
                }
            }
        }
        例子三： 多次循环查询单表，tables为list
        query_data = {
            "tables": [
                {
                    "Actor": {
                        "columns": "id",
                        "args": "yuan_huang@sl.com"
                    }
                },
                {
                    "Loan": {
                        "columns": ["id", "name"],
                        "args": ["14801", "3"]
                    }
                }
            ]
        }
        例子四：多表联合查询，tables为dict, 分别返回多表的某些列数据
        query_data = {
            "tables": {
                "LoanApp": {
                    "columns": None,
                    "args": "14801"
                },
                "CreditClass": {
                    "columns": ["grade", "name"],
                    "args": None
                }
            }
        }
        例子五：单表查询，多表联合查询，分别返回对应表的某些列数据
        query_data = {
            "tables": [
                {
                    "LoanApp": {
                        "columns": None,
                        "args": "16217"
                    },
                    "CreditClass": {
                        "columns": ["grade", "name"],
                        "args": None
                    }
                },
                {
                    "Actor": {
                        "columns": "id",
                        "args": "yuan_huang@sl.com"
                    }
                },
                {
                    "Loan": {
                        "columns": ["aid", "credit_class_id"],
                        "args": ["14601", "19"]
                    }
                }
            ]
        }
        """
        def _get_json_key_value(json_data, primary_key, secondary_key):
            value_list = []
            handle_item_in_json(json_data, primary_key, secondary_key, value_list)

            if len(value_list) == 1:
                value_list = value_list.pop()

            return value_list

        def _get_query_table(query_json_data):
            tables_temp = _get_json_key_value(query_json_data, 'tables', None)

            query_tables = []
            if isinstance(tables_temp, dict):
                query_tables.append(tables_temp.keys())
            elif isinstance(tables_temp, list):
                [query_tables.append(table.keys()) for table in tables_temp]
            else:
                raise Exception("The temp tables(%s) format is not supported." % tables_temp)
            return query_tables

        tables = _get_query_table(query_data)

        # 实例化operator
        operator_instance = self.operator(self.database_tag)

        # 获取操作的数据库TABLE_METHOD
        table_method_dict = DATABASE_OPERATOR_MAP_TABLE_METHOD[self._operator]

        # 检查查询的数据库表是否存在
        for j in tables:
            if len(j) == 1 and j[0] in table_method_dict.keys() or tuple(j) in table_method_dict.keys():
                continue
            else:
                raise Exception("query tables(%s) are not in the supported tables." % j)

        # 查询对应的数据库表
        query_result = {}
        for i in tables:
            if len(i) == 1:
                i = i.pop()
                columns = _get_json_key_value(query_data, i, 'columns')
                method_args = _get_json_key_value(query_data, i, 'args')

                # 根据json数据中args个数，决定输入参数的形式
                if isinstance(method_args, list):
                    result = getattr(operator_instance, table_method_dict[i])(*method_args)
                elif method_args is None:
                    result = getattr(operator_instance, table_method_dict[i])()
                else:
                    result = getattr(operator_instance, table_method_dict[i])(method_args)

                # 判断json数据中对应表的columns个数
                if isinstance(columns, list):
                    temp = {}
                    for j in columns:
                        temp.update({j: getattr(result, j)})
                        query_result.update({i: temp})
                elif columns:
                    query_result.update({i: {columns: getattr(result, columns)}})
            else:
                all_method_args = []
                for k in i:
                    # 获取联合查询表方法需要的所有参数
                    method_args_temp = _get_json_key_value(query_data, k, 'args')
                    if isinstance(method_args_temp, list):
                        all_method_args.extend(method_args_temp)
                    elif method_args_temp:
                        all_method_args.append(method_args_temp)

                    result = getattr(operator_instance, table_method_dict[tuple(i)])(*all_method_args)

                    columns_temp = _get_json_key_value(query_data, k, 'columns')
                    if isinstance(columns_temp, list):
                        temp = {}
                        for j in columns_temp:
                            temp.update({j: getattr(result, j)})
                            query_result.update({k: temp})
                    elif columns_temp:
                        query_result.update({k: {columns_temp: getattr(result, columns_temp)}})

        return query_result

    def check_table_row_existence(self, table_columns, *query_values):
        """
        :param table_columns: 由表名、下划线和列名组成(单个)
        :param query_values: 多个或单个查询值
        """
        (table, column) = str(table_columns).split("_", 1)
        try:
            for values in query_values:
                query_json_data = {
                    "tables": {
                        table: {
                            "columns": column,
                            "args": str(values)
                        }
                    }
                }
                self.get_column_value_from_table(query_json_data)
            return True
        except:
            return False

    @staticmethod
    def assert_db_value(db_query_result, expect_values, *table_columns):
        """
        验证获取的数据库值是否与预期值相等。
        :param db_query_result: 指的是上述返回的query_result
        :param expect_values: 预期值，为str或list
        :param table_columns: 由表名、下划线和列名组成
        """
        if len(table_columns) == 1:
            table_columns = list(table_columns).pop()
            (table, column) = table_columns.split("_", 1)
            db_value = db_query_result[table][column]
            assert (db_value == expect_values)
        else:
            db_values = []
            for table_column in table_columns:
                (table, column) = table_column.split("_", 1)
                db_value = db_query_result[table][column]
                db_values.append(db_value)
            assert (db_values == expect_values)

    @staticmethod
    def assert_db_value_not_none(db_query_result, *table_columns):
        """
        验证获取的数据库值是否与预期值相等。
        :param db_query_result: 指的是上述返回的query_result
        :param table_columns: 由表名、下划线和列名组成
        """
        if len(table_columns) == 1:
            table_columns = list(table_columns).pop()
            (table, column) = table_columns.split("_", 1)
            db_value = db_query_result[table][column]
            assert db_value is not None
        else:
            for table_column in table_columns:
                (table, column) = table_column.split("_", 1)
                db_value = db_query_result[table][column]
                assert db_value is not None

if __name__ == "__main__":
    # 查询demo oracle数据库
    database_assertion = DatabaseAssertion()
    data = {
        "tables": [
            {
                "LoanApp": {
                    "columns": None,
                    "args": "16217"
                },
                "CreditClass": {
                    "columns": ["grade", "name"],
                    "args": None
                }
            },
            {
                "Actor": {
                    "columns": ["id", "name", 'ssn'],
                    "args": "yuan_huang@sl.com"
                }
            },
            {
                "Loan": {
                    "columns": ["aid", "credit_class_id"],
                    "args": ["14601", "19"]
                }
            }
        ]
    }
    result1 = database_assertion.get_column_value_from_table(data)
    print result1
    database_assertion.assert_db_value(result1, [10889623.0, 'yuan_huang_admin'], 'Actor_id', 'Actor_name')
    database_assertion.assert_db_value_not_none(result1, 'Actor_id')

