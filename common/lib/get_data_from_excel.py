#coding=utf-8
#coding=gbk
'''
Created on Jun 14, 2013

@author: Chester.Qian
'''

import picalo
import os
import string
from apihelper import info
import time
import re

def clearFilter(func):
    def wrapper(*args, **kwargs):
        try:
            args[0].clear_filter()
        except AttributeError:
            args[0].table.clear_filter()
        return func(*args, **kwargs)
    return wrapper

class ExcelData:
    class __ExcelData(object):
        def __init__(self,kargs):
            self.file_path = None
            '数据表中原有的字段值'
            self.original_info = []
            self.current_testcase_id = None
            self.filename = kargs['filename']
            self.table=picalo.load_excel(**kargs)
            self.cns = self.table.get_column_names()
#            print self.cns
            '为文件对象添加字段'
            [self.table.set_name(self.cns.index(self.cns[i],i),self.cns[i])
             for i in range(len(self.cns))]

        def getData(self, content, column = 'id' ):
            '根据字段和内容获取数据表中的字段值'
            self.table.filter("%s == '%s'"%(column,content))
            self.current_testcase_id = self.table[0].id
            return self.table

        @clearFilter
        def getDataSetIndex(self, columns_content_dict):
            return self.table.find(**columns_content_dict)

        def setData(self,test_case_id,record,columns_content_dict):
            '修改数据表中的字段值'
            original_columns_content_dict = {}
            @clearFilter
            def __saveData(table,file_path):
                table.save_excel(file_path)
            for k in columns_content_dict.keys():
                original_columns_content_dict.update({k:getattr(record,k)})
                setattr(record,k,columns_content_dict[k])
            self.original_info.append((test_case_id,original_columns_content_dict))
            __saveData(self.table,self.file_path)
            return record

        @clearFilter
        def insertData(self,table,index,postion,columns_content_dict):
            table.insert(index+postion,columns_content_dict)
            table.save_excel(self.file_path)

        def updateData(self,test_case_id,columns_content_dict):
            pass

        def get_original_columns_content_dict(self):
            pass

        def getDataReferenceFrom(self,data):
            '获取相关文件记录,一对一关系'
            self.table.filter("reference_id == '%s'"%(data.filename.split('.')[0]+ '_' + data.current_testcase_id))
            self.current_testcase_id = self.table[0].id
            pass

        def getDataReferenceTo(self,test_case_id):
            pass

    instances = []
    filenames = []
    file_path_list =[]

    def __init__(self,file_dir,kargs):
        os.chdir(file_dir)
        if not ExcelData.instances or not kargs['filename'] in ExcelData.filenames:
            self.current_instance = ExcelData.__ExcelData(kargs)
            file_path = file_dir + '/' + self.current_instance.filename
            self.current_instance.file_path = file_path
            ExcelData.instances.append(self.current_instance)
            ExcelData.filenames.append(ExcelData.instances[-1].filename)
            ExcelData.file_path_list.append(file_path)
        elif kargs['filename'] in ExcelData.filenames:
            [setattr(self,'current_instance',inst) for inst in ExcelData.instances
             if kargs['filename'] == inst.filename]

    def __str__(self):
        return self.current_instance.filename

    def __getattr__(self,name):
        return getattr(self.current_instance,name)

 