# coding=utf-8
# 数据库得分保存地址

username = "system"
pwd = "oracle"
ip = "127.0.0.1"
tns = "oradb"

# 正式文件
save_address = "/etc/vsfox/score.txt"
# 测试文本
save_address_test = './test.txt'

oracle_sql_3 = "/examdata/result/conf_table.log"
oracle_sql_7 = "/examdata/result/query_obj_tbs02.log"
oracle_sql_8 = "/examdata/result/query_scott_tbl02.log"
oracle_sql_9 = "/examdata/result/query_ind.log"
oracle_sql_10 = "/examdata/result/query_reb_ind.log"
oracle_sql_12 = "/examdata/result/view_dept_emp.log"
oracle_sql_13 = "/examdata/result/seq_dept.log"
oracle_sql_14 = "/examdata/result/synonym_dept.log"

import cx_Oracle
import os
import re


class Cat_score_1(object):
    """题目一"""

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目一:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            with open(save_address, "w") as f:
                # 查看参数undo_retention值
                sql = "SELECT INDEX_TYPE FROM DBA_INDEXES WHERE INDEX_NAME IN ( SELECT DISTINCT INDEX_NAME FROM DBA_IND_COLUMNS WHERE table_name='CUSTOMERS' AND table_owner='SH' AND column_name='COUNTRY_ID')"
                self.cr.execute(sql)
                rs = self.cr.fetchone()
                # 文件判断保存
                if rs[0] == "bitmap":
                    f.write(("数据库数据段管理课件题目一:查看创建的索引为%s类型正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库数据段管理课件题目一:查看创建的索引为%s类型错误,---error" + '\n') % rs[0])

        except:
            print("操作数据库数据段管理课件题目一:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库数据段管理课件题目一:成功")


class Cat_score_2(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目二:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = '''select COMPRESSION from dba_indexes where index_name in (select index_name from dba_ind_columns where column_name='COUNTRY_ID' and table_name='CUSTOMERS' AND TABLE_OWNER='SH' intersect select index_name from dba_ind_columns where column_name='CUST_CITY' and table_name='CUSTOMERS' AND TABLE_OWNER='SH') '''
                self.cr.execute(sql)
                rs = self.cr.fetchone()
                # 文件判断保存
                if rs[0] == "ENABLED":
                    f.write("数据库数据段管理课件题目二:查看索引是压缩,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目二:查看索引没压缩,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目二:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库数据段管理课件题目二:成功")


class Cat_score_3(object):

    def query_status_instance(self):

        try:
            file_name = oracle_sql_3

            if os.path.exists(file_name):
                # 判断文件是否存在
                with open(save_address, "a+") as f:

                    f.write(("数据库数据段管理课件题目三:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "Create table sh.costs_1 as select * from sh.costs"
                str_2 = "Create table sh.costs_2 as select * from sh.costs"
                str_3 = "Delete sh.costs_1"
                str_4 = "Delete sh.costs_2"
                str_5 = 'Truncate table sh.costs_1'
                str_6 = 'Truncate table sh.costs_2'

                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:
                    if str_1 in read_str and str_2 in read_str and str_3 in read_str and str_4 in read_str and str_5 in read_str and str_6 in read_str:
                        f.write(("数据库数据段管理课件题目三:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目三:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目三:文件%s不存在,---error" + '\n') % file_name)


        except:
            print("操作数据库数据段管理课件题目三:失败")

        else:
            print("操作数据库数据段管理课件题目三:成功")


class Cat_score_4(object):
    """题目 4"""

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目四:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:

            # 查看参数db_16k_cache_size值
            with open(save_address, "a+") as f:

                sql = "select view_name,text,read_only from dba_views where view_name='V_EMP_1'"
                self.cr.execute(sql)
                rs = self.cr.fetchall()

                a = 0
                if len(rs) > 0:
                    for i in rs:
                        if i[0] in ["V_EMP_1", "select ename", "job", "hiredate", "sal from scott.emp where sal>2500", "Y"]:
                            a += 1
                else:
                    a = 0

                # 查询文件判断保存
                if a >= 6:
                    f.write("数据库数据段管理课件题目四:确认视图为v_emp_1,且视图满足查询条件和视图为只读 正确,---ok" + '\n')

                else:
                    f.write("数据库数据段管理课件题目四:确认视图为v_emp_1,且视图满足查询条件和视图为只读 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目四:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库数据段管理课件题目四:成功")


class Cat_score_5(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目五:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:

            with open(save_address, "a+") as f:

                sql = "select REFRESH_METHOD from dba_mviews where MVIEW_NAME='MV_EMP' AND OWNER='SCOTT'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 查询文件判断保存
                if rs[0] == 'FORCE':
                    f.write("数据库数据段管理课件题目五:查看物化视图更新方式 正确,---ok" + '\n')

                else:
                    f.write("数据库数据段管理课件题目五:查看物化视图更新方式 错误,---error" + '\n')

            # 物化视图的查询语句
            with open(save_address, "a+") as f:

                sql = "Select query from dba_mviews where MVIEW_NAME='MV_EMP' AND OWNER='SCOTT'"
                self.cr.execute(sql)
                rs = self.cr.fetchall()

                a = 0
                if len(rs) > 0:
                    for i in rs:
                        if i[0] in ["select ename", "job", "hiredate", "sal from scott.emp where sal>2000"]:
                            a += 1
                else:
                    a = 0

                # 查询文件判断保存
                if a >= 4:
                    f.write("数据库数据段管理课件题目五:确认物化视图的查询语句 正确,---ok" + '\n')

                else:
                    f.write("数据库数据段管理课件题目五:确认物化视图的查询语句 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目五:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库数据段管理课件题目五:成功")


class Cat_score_6(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目六:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select PARTITIONING_TYPE  from dba_part_tables where owner='SCOTT' AND table_name='TABLE_A'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == "RANGE":
                    f.write("数据库数据段管理课件题目六:确认表table_a分区方式 正确,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目六:确认表table_a分区方式 错误,---error" + '\n')


            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select COLUMN_NAME from dba_part_key_columns where owner='SCOTT' AND table_name='TABLE_A'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = ('True',)

                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == "order_date":
                    f.write("数据库数据段管理课件题目六:确认分区键 正确,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目六:确认分区键 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目六:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库数据段管理课件题目六:成功")


class Cat_score_7(object):

    def query_status_instance(self):

        try:
            file_name = oracle_sql_7

            if os.path.exists(file_name):
                # 判断文件是否存在
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目七:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "dba_segments"
                str_2 = "bytes"
                str_3 = "SH"
                str_4 = "COSTS"

                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:
                    if str_1 in read_str and str_2 in read_str and str_3 in read_str and str_4 in read_str:
                        f.write(("数据库数据段管理课件题目七:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目七:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目七:文件%s不存在,---error" + '\n') % file_name)

        except:
            print("操作数据库数据段管理课件题目七:失败")

        else:
            print("操作数据库数据段管理课件题目七:成功")


class Cat_score_8(object):

    def query_status_instance(self):

        try:
            file_name = oracle_sql_8


            if os.path.exists(file_name):
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目八:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "Object_name"
                str_2 = "Object_type"
                str_3 = "Dba_objects"
                str_4 = "OWNE"
                str_5 = "SCOTT"

                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:

                    if str_1 in read_str and str_2 in read_str and str_3 in read_str and str_4 in read_str and str_5 in read_str:
                        f.write(("数据库数据段管理课件题目八:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目八:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目八:文件%s不存在,---error" + '\n') % file_name)

        except:
            print("操作数据库数据段管理课件题目八:失败")

        else:
            print("操作数据库数据段管理课件题目八:成功")


class Cat_score_9(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目九:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            file_name = oracle_sql_9


            if os.path.exists(file_name):
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目九:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "Tablespace_name"
                str_2 = "Bytes"
                str_3 = "Dba_segments"
                str_4 = "id_idx"

                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:

                    if str_1 in read_str and str_2 in read_str and str_3 in read_str and str_4 in read_str:
                        f.write(("数据库数据段管理课件题目九:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目九:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目九:文件%s不存在,---error" + '\n') % file_name)


            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select column_name from dba_ind_columns where index_name='ID_IDX'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == "ID":
                    f.write("数据库数据段管理课件题目九:确认索引列是否为id 正确,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目九:确认索引列是否为id 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目九:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库数据段管理课件题目九:成功")


class Cat_score_10(object):

    def query_status_instance(self):

        try:
            file_name = oracle_sql_10

            if os.path.exists(file_name):
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目十:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "STATUS"
                str_2 = "Dba_indexes"
                str_3 = "Table_name='EMPLOYEES'"

                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:

                    if str_1 in read_str and str_2 in read_str and str_3 in read_str:
                        f.write(("数据库数据段管理课件题目十:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目十:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目十:文件%s不存在,---error" + '\n') % file_name)

        except:
            print("操作数据库数据段管理课件题目十:失败")

        else:
            print("操作数据库数据段管理课件题目十:成功")


class Cat_score_11(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目十一:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select count(*) from dba_indexes where index_name='EMP_FUN_IND' and owner='HR'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == 1:
                    f.write("数据库数据段管理课件题目十一:确认索引emp_fun_ind存在 正确,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目十一:确认索引emp_fun_ind存在 错误,---error" + '\n')

            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select column_name from dba_ind_columns where index_name='EMP_FUN_IND'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = ('True',)
                else:
                    rs = rs

                re_str = re.match("SYS.*", rs[0])

                if re_str == None:
                    f.write("数据库数据段管理课件题目十一:确认索引列为函数upper(last_name) 错误,---error" + '\n')

                else:
                    f.write("数据库数据段管理课件题目十一:确认索引列为函数upper(last_name) 正确,---ok" + '\n')

        except:
            print("操作数据库数据段管理课件题目十一:失败")

        else:
            print("操作数据库数据段管理课件题目十一:成功")


class Cat_score_12(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目十二:数据库打开错误")

        else:
            self.cr = cr
            self.db = db


    def query_status_instance(self):

        try:
            file_name = oracle_sql_12


            if os.path.exists(file_name):
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目十二:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "Create view"
                str_2 = "Dname"
                str_3 = "Loc"
                str_4 = "Ename"
                str_5 = "Sal"
                str_6 = "job"
                str_7 = "dept"
                str_8 = "emp"


                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:

                    if str_1 in read_str and str_2 in read_str and str_3 in read_str and str_4 in read_str and str_5 in read_str and str_6 in read_str and str_7 in read_str and str_8 in read_str:
                        f.write(("数据库数据段管理课件题目十二:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目十二:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目十二:文件%s不存在,---error" + '\n') % file_name)

            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select count(*) from dba_views where view_name='VIEW_DEPT_EMP' AND OWNER='SCOTT'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == 1:
                    f.write("数据库数据段管理课件题目十二:确认视图view_dept_emp是否存在 正确,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目十二:确认视图view_dept_emp是否存在 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目十二:失败")

        else:
            print("操作数据库数据段管理课件题目十二:成功")


class Cat_score_13(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目十三:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            file_name = oracle_sql_13

            if os.path.exists(file_name):
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目十三:文件%s存在,---ok" + '\n') % file_name)

                # 判断文件中是否存在语句
                str_1 = "Deptno_seq.currval"
                str_2 = "Deptno_seq.nextval"
                str_3 = "User_sequences"
                str_4 = "SEQUENCE_NAME"
                str_5 = "MAX_VALUE"
                str_6 = "INCREMENT_BY"

                read_str = ""
                f_read = open(file_name, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    read_str += line

                f.close()

                # 遍历文件查看
                with open(save_address, 'a+') as f:

                    if str_1 in read_str and str_2 in read_str and str_3 in read_str and str_4 in read_str and str_5 in read_str and str_6 in read_str:
                        f.write(("数据库数据段管理课件题目十三:文件%s存在信息,---ok" + '\n') % file_name)

                    else:
                        f.write(("数据库数据段管理课件题目十三:文件%s不存在信息,---error" + '\n') % file_name)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库数据段管理课件题目十三:文件%s不存在,---error" + '\n') % file_name)

            with open(save_address, "a+") as f:

                sql = "Select count(*) from dba_sequences where SEQUENCE_OWNER='SCOTT' and SEQUENCE_NAME='DEPTNO_SEQ'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == 1:
                    f.write("数据库数据段管理课件题目十三:序列deptno_seq是否已创建 正确,---ok" + '\n')
                else:
                    f.write("数据库数据段管理课件题目十三:序列deptno_seq是否已创建 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目十三:失败")

        else:
            print("操作数据库数据段管理课件题目十三:成功")


class Cat_score_14(object):

    def __init__(self):
        """数据库账号密码初始化"""
        self.username = username
        self.pwd = pwd
        self.ip = ip
        self.sql_name = tns

        try:
            # 创建数据库连接
            # db = cx_Oracle.connect('system/oracle@192.168.32.77/sql_name')
            db = cx_Oracle.connect(self.username + '/' + self.pwd + '@' + self.ip + '/' + self.sql_name)

            # 建立cursor
            cr = db.cursor()

        except:
            print("数据库数据段管理课件题目十四:数据库打开错误")

        else:
            self.cr = cr
            self.db = db


    def query_status_instance(self):

        try:
            file_name = oracle_sql_14

            # 判断文件是否存在
            with open(save_address, "a+") as f:

                if os.path.exists(file_name):
                    f.write(("数据库数据段管理课件题目十四:文件%s存在,---ok" + '\n') % file_name)

                else:
                    f.write(("数据库数据段管理课件题目十四:文件%s不存在,---error" + '\n') % file_name)

            with open(save_address, "a+") as f:

                sql = "select count(*) from dba_synonyms where TABLE_owner='SCOTT' AND SYNONYM_NAME='PRIVATE_EMP'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == 1:
                    f.write("数据库数据段管理课件题目十四:确认同义词PUBLIC_EMP是否已创建 正确,---ok" + '\n')

                else:
                    f.write("数据库数据段管理课件题目十四:确认同义词PUBLIC_EMP是否已创建 错误,---error" + '\n')

            with open(save_address, "a+") as f:

                sql = "select count(*) from dba_synonyms where TABLE_owner='SCOTT' AND SYNONYM_NAME='PRIVATE_EMP'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:

                    rs = ('True',)
                else:
                    rs = rs

                # 文件判断保存
                if rs[0] == 1:
                    f.write("数据库数据段管理课件题目十四:确认同义词PUBLIC_EMP是否已创建 正确,---ok" + '\n')

                else:
                    f.write("数据库数据段管理课件题目十四:确认同义词PUBLIC_EMP是否已创建 错误,---error" + '\n')

        except:
            print("操作数据库数据段管理课件题目十四:失败")

        else:
            print("操作数据库数据段管理课件题目十四:成功")



def run():
    Cat_score_1().query_status_instance()
    Cat_score_2().query_status_instance()
    Cat_score_3().query_status_instance()
    Cat_score_4().query_status_instance()
    Cat_score_5().query_status_instance()
    Cat_score_6().query_status_instance()
    Cat_score_7().query_status_instance()
    Cat_score_8().query_status_instance()
    Cat_score_9().query_status_instance()
    Cat_score_10().query_status_instance()
    Cat_score_11().query_status_instance()
    Cat_score_12().query_status_instance()
    Cat_score_13().query_status_instance()
    Cat_score_14().query_status_instance()

run()
