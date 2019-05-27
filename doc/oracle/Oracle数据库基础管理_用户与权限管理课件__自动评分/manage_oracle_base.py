# coding=utf-8
# 数据库得分保存地址

username = "system"
pwd = "oracle"
ip = "127.0.0.1"
tns = "oradb"

save_address = "/etc/vsfox/score.txt"
num_4_sql = "/examdata/result/reset_password.sql"
num_5_sql = "/examdata/result/granted_sysdba_user.sql"
num_8_log = "/examdata/result/query_user200.log"
num_12_log = "/examdata/result/grant_object_priv.log"
num_13_log = "/examdata/result/grant_user217_priv.log"
num_16_log = "/examdata/result/exam_role_priv200.log"
num_17_log = "/examdata/result/exam_role_obj201.log"
num_18_log = "/examdata/result/user207_role_priv.log"
num_19_log = "/examdata/result/user_priv5.log"
num_20_log = "/examdata/result/query_profile_value.log"
num_23_log = "/examdata/result/query_profile_user212.log"

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
            print("用户与角色管理课件题目一:数据库打开错误")
            raise

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):
        """
        select status from v$instance;
        """
        try:
            # 数据库状态
            sql = "select status from v$instance"
            self.cr.execute(sql)
            rs = self.cr.fetchall()
            if len(rs) > 0:
                rs_statu = rs[0][0]
            else:
                rs_statu = rs

            # 数据库查询文件保存
            with open(save_address, "w") as f:
                if rs_statu == "OPEN":
                    f.write("用户与角色管理课件题目一:数据库状态是打开的,---ok" + '\n')
                else:
                    f.write("用户与角色管理课件题目一:数据库状态是关闭的,---error" + '\n')

            # 锁定用户exam_user5
            sql_user5 = "select account_status from dba_users where username='EXAM_USER5'"
            self.cr.execute(sql_user5)
            rs_user5 = self.cr.fetchall()

            if len(rs_user5) > 0:
                rs_user5_a = rs_user5[0][0]
            else:
                rs_user5_a = rs_user5

            # 数据库查询文件保存
            with open(save_address, "a+") as f:
                if rs_user5_a == "LOCKED":
                    f.write("用户与角色管理课件题目一:数据库用户 exam_user5 是正确的, ---ok" + '\n')
                else:
                    f.write("用户与角色管理课件题目一:用户 exam_user5 是错误的,---error" + '\n')

            # 解锁用户exam_user6
            sql_user6 = "select account_status from dba_users where username='EXAM_USER6'"
            self.cr.execute(sql_user6)
            rs_user6 = self.cr.fetchone()

            if len(rs_user6) > 0:
                rs_user6_a = rs_user6[0][0]
            else:
                rs_user6_a = rs_user6

            # 数据库查询文件保存
            with open(save_address, "a+") as f:
                if rs_user6_a == "OPEN":
                    f.write("用户与角色管理课件题目一:用户 exam_user6 是正确的,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目一:用户 exam_user6 是错误的, ---error" + '\n')

        except:
            print("操作用户与角色管理课件题目一:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目一:成功")


class Cat_score_2(object):
    """
    题目二
    并将所操作命令保存在/examdata/result/exam_user7.result文件中：
    """

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
            print("用户与角色管理课件题目二:数据打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_user7(self):
        """用户7 内容"""
        try:
            sql = "select DEFAULT_TABLESPACE from dba_users where username='EXAM_USER7'"

            sql_1 = "select max_bytes/1024/1024 from dba_ts_quotas where tablespace_name='USERS' AND username='EXAM_USER7'"

            sql_2 = "select TEMPORARY_TABLESPACE from dba_users where username='EXAM_USER7'"

            # 表空间
            self.cr.execute(sql)
            # 一次返回所以查询集
            rs = self.cr.fetchall()

            if len(rs) > 0:
                rs_user_7 = rs[0][0]
            else:
                rs_user_7 = rs

            # 数据库查询文件保存
            with open(save_address, "a+") as f:
                if rs_user_7 == "USERS":
                    f.write("用户与角色管理课件题目二:用户 test_user7 表空间是正确的 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二:用户 test_user7 表空间是错误的 , ---error" + '\n')

            # test_user7 最大配额大小
            self.cr.execute(sql_1)
            # 一次返回所以查询集
            rs_max = self.cr.fetchall()

            if len(rs_max) > 0:
                rs_user_max = rs_max[0][0]
            else:
                rs_user_max = rs_max

            with open(save_address, "a+") as f:
                if rs_user_max == 10:
                    f.write("用户与角色管理课件题目二:用户 test_user7 最大配额大小是正确的,---ok" + '\n')

                # elif len(rs) == 0:
                #     f.write("确认data01表空间配额是错误 ,---error" + '\n')

                else:
                    f.write("用户与角色管理课件题目二:用户 test_user7 最大配额大小是错误的, ---error" + '\n')

            # test_user7 可试探空间
            self.cr.execute(sql_2)
            # 一次返回所以查询集
            rs_room = self.cr.fetchone()

            if len(rs_room) > 0:
                rs_user_room = rs_room[0][0]
            else:
                rs_user_room = rs_room

            # 数据库查询文件保存
            with open(save_address, "a+") as f:
                if rs_user_room == "TEMP5":
                    f.write("用户与角色管理课件题目二:用户 test_user7 可试探空间是正确的,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二:用户 test_user7 可试探空间是错误的, ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目二:失败')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目二:成功")


class Cat_score_3(object):
    """
    题目三
    examuser20
    """

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
            print("用户与角色管理课件题目三:数据打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_user20(self):
        try:
            sql = "select status from v$instance"
            sql_1 = "select account_status from dba_users where username='EXAM_USER20'"

            # 用户 test_user20数据库
            self.cr.execute(sql)
            # 一次返回所以查询集
            rs = self.cr.fetchall()

            if len(rs) > 0:
                rs_use_20 = rs[0][0]
            else:
                rs_use_20 = rs

            with open(save_address, "a+") as f:

                if rs_use_20 == "OPEN":
                    f.write("用户与角色管理课件题目三:用户 test_user20 数据库打开是正确的 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目三:用户 test_user20 数据库打开是错误的 , ---error" + '\n')

            # 用户 test_user20数据库实例状态
            self.cr.execute(sql_1)
            # 一次返回所以查询集
            rs_user = self.cr.fetchall()

            if len(rs_user) > 0:
                rs_user_20 = rs_user[0]
            else:
                rs_user_20 = rs_user

            # 数据库查询文件保存
            with open(save_address, "a+") as f:

                if rs_user_20 == "OPEN":

                    f.write("用户与角色管理课件题目三:用户 test_user20 数据库实例状态是正确的 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目三:用户 test_user20 数据库实例状态是错误的 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目三:失败')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目三:成功")


class Cat_score_4(object):
    """
    题目四
    dbuser1、dbuser2和dbuser3三个业务帐号
    """

    def Search_file(self):
        try:
            filename = num_4_sql

            with open(save_address, "a+") as f:

                if os.path.exists(filename):
                    f.write("用户与角色管理课件题目四:文件/examdata/result/reset_password.sql存在,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目四:文件/examdata/result/reset_password.sql不存在,---error" + '\n')

            if os.path.exists(filename):

                a = 0
                f = open(num_4_sql)
                line_list = []

                for line in f.readlines():
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)

                str_1 = re.findall(
                    r'alter user dbuser1 identified by|alter user dbuser2 identified by|alter user dbuser3 identified by',
                    line_str)

                if "alter user dbuser1 identified by" in str_1 and "alter user dbuser2 identified by" in str_1 and "alter user dbuser3 identified by" in str_1:
                    a += 1

                if a == 1:
                    with open(save_address, "a+") as f:
                        f.write("用户与角色管理课件题目四:文件/examdata/result/reset_password.sql存在sql命令,---ok" + '\n')

                else:
                    with open(save_address, "a+") as f:
                        f.write("用户与角色管理课件题目四:文件/examdata/result/reset_password.sql不存在sql命令,---error" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目四:文件/examdata/result/reset_password.sql不存在sql命令,---error" + '\n')


        except:
            print('操作用户与角色管理课件题目四:失败')

        else:
            f.close()
            print('操作用户与角色管理课件题目四:成功')


class Cat_score_5(object):
    """
    题目五
    找出oradb数据库中所有被授予SYSDBA特权的用户
    """

    def Search_file(self):

        str_list = []
        a = 0

        filename = num_5_sql

        if os.path.exists(filename):
            try:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目五:文件/examdata/result/granted_sysdba_user.sql存在,---ok" + '\n')

                f = open(num_5_sql)
                lines = f.readlines()

                for line in lines:
                    line = line.strip('\n')
                    str_test = re.findall('V_\$PWFILE_USERS', line)

                    str_list.append(str_test)

                for i in str_list:
                    if "V_$PWFILE_USERS" in i:
                        a += 1

                if a != 0:
                    with open(save_address, "a+") as f:
                        f.write("用户与角色管理课件题目五:文件V_$PWFILE_USERS存在,---ok" + '\n')
                else:
                    with open(save_address, "a+") as f:
                        f.write("用户与角色管理课件题目五:文件V_$PWFILE_USERS不存在,---error" + '\n')

            except:
                print('操作用户与角色管理课件题目五:失败')

            else:
                f.close()


        else:
            with open(save_address, "a+") as f:
                f.write("用户与角色管理课件题目五:文件/examdata/result/granted_sysdba_user.sql不存在,---error" + '\n')


class Cat_score_6(object):
    """
    题目六
    在oradb数据库中建立adams用户
    """

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
            print('操作用户与角色管理课件题目六:失败')

        else:
            self.cr = cr
            self.db = db

    def query_oracle_adams(self):
        rs_list = []

        try:
            sql = "select default_tablespace,temporary_tablespace from dba_users where username='ADAMS'"
            sql_1 = "select max_bytes from dba_ts_quotas where tablespace_name='DATA01' AND username='ADAMS'"
            sql_2 = "select max_bytes from dba_ts_quotas where tablespace_name='DATA02' AND username='ADAMS'"

            self.cr.execute(sql)
            rs = self.cr.fetchall()
            for i in rs:
                rs_list.append(i[0][0])

            # 确认用户adams用户默认表空间、临时表空间
            with open(save_address, "a+") as f:
                if "USERS" in rs_list and "TEMP" in rs_list:
                    f.write("用户与角色管理课件题目六:用户adams用户默认表空间、临时表空间是正确的 ,---ok" + '\n')
                else:
                    f.write("用户与角色管理课件题目六:用户adams用户默认表空间、临时表空间是错误 ,---error" + '\n')

            # 确认data01表空间配额
            self.cr.execute(sql_1)
            rs1 = self.cr.fetchall()

            if len(rs1) > 0:
                rs_data01 = rs1[0][0]
            else:
                rs_data01 = rs1

            with open(save_address, "a+") as f:

                if rs_data01 == 10:
                    f.write("用户与角色管理课件题目六:确认data01表空间配额是正确的 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目六:确认data01表空间配额是错误 ,---error" + '\n')

            # 确认data02表空间配额
            self.cr.execute(sql_2)
            rs2 = self.cr.fetchall()

            if len(rs2) > 0:
                rs_data02 = rs2[0][0]
            else:
                rs_data02 = rs2

            with open(save_address, "a+") as f:
                # if len(rs2) == 0:
                #     f.write("确认data02表空间配额是错误 ,---error" + '\n')

                if rs_data02 == 20:
                    f.write("用户与角色管理课件题目六:确认data02表空间配额是正确的 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目六:确认data02表空间配额是错误 ,---error" + '\n')

        except:
            print("操作用户与角色管理课件题目六:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目六:成功")


class Cat_score_7(object):
    """
    题目六
    在oradb数据库中建立james用户
    """

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
            print("用户与角色管理课件题目七:数据打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_james(self):
        rs_list = []

        try:
            sql = "select default_tablespace,temporary_tablespace from dba_users where username='JAMES'"
            sql_1 = "Select account_status from dba_users where username='JAMES'"

            # 确认用户james用户默认表空间
            self.cr.execute(sql)
            rs = self.cr.fetchall()
            for i in rs:
                rs_list.append(i[0][0])

            with open(save_address, "a+") as f:
                if "DATA03" in rs_list and "TEMP_GROUP5" in rs_list:
                    f.write("用户与角色管理课件题目七:用户james用户默认表空间是正确的 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目七:用户james用户默认表空间是错误 ,---error" + '\n')

            # 确认用户james状态
            self.cr.execute(sql_1)
            rs1 = self.cr.fetchall()
            if len(rs1) > 0:
                rs_user_james = rs1[0][0]
            else:
                rs_user_james = rs1

            with open(save_address, "a+") as f:
                if rs_user_james == "LOCKED":
                    f.write("用户与角色管理课件题目七:用户james状态是正确的 ,---ok" + '\n')
                else:
                    f.write("用户与角色管理课件题目七:用户james状态是错误 ,---error" + '\n')


        except:
            print("操作用户与角色管理课件题目七:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目七:成功")


class Cat_score_8(object):
    """
    题目八
    数据库中查询examuser200用户的建立时间、默认表空间和临时表空间
    """

    def Search_log(self):

        filename_log = num_8_log
        filename_sql = num_5_sql

        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目八:文件/examdata/result/query_user200.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:

                    f.write("用户与角色管理课件题目八:文件/examdata/result/query_user200.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_sql):

                f = open(filename_sql)
                lines = f.readlines()
                line_list = []
                str_sql = "select created,default_tablespace,TEMPORARY_TABLESPACE from dba_users where username='EXAMUSER200';"

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                f.close()
                # re匹配关键词
                line_str = " ".join(line_list)

                str_1 = re.findall(
                    r"select created,default_tablespace,TEMPORARY_TABLESPACE from dba_users where username='EXAMUSER200';",
                    line_str)

                if str_sql in str_1:
                    with open(save_address, "a+") as f:
                        f.write("用户与角色管理课件题目八:文件/examdata/result/granted_sysdba_user存在关键信息,---ok" + '\n')
                else:
                    with open(save_address, "a+") as f:
                        f.write("用户与角色管理课件题目八:文件/examdata/result/granted_sysdba_user不存在关键信息,---error" + '\n')
            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目八:文件/examdata/result/granted_sysdba_user.sql不存在,---error" + '\n')

        except:
            print('操作用户与角色管理课件题目八:失败')

        else:
            print("操作用户与角色管理课件题目八:成功")


class Cat_score_9(object):
    """
    题目9
    删除oradb数据库中的examuser202和examuser203用户
    """

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
            print("用户与角色管理课件题目九:打开数据错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_examuser202(self):

        try:
            sql = "select count(*) from dba_users where username='EXAMUSER202'"
            sql_1 = "select count(*) from dba_users where username='EXAMUSER203'"

            # 用户examuser202是否存在
            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()

            if rs == None:
                rs_examuser202 = rs

            else:
                rs_examuser202 = rs[0]

            with open(save_address, "a+") as f:

                if rs_examuser202 == 0:
                    f.write("用户与角色管理课件题目九:用户examuser202存在 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目九:用户examuser202不存在 , ---error" + '\n')

            # 用户examuser203是否存在
            self.cr.execute(sql_1)
            rs1 = self.cr.fetchone()

            if rs1 == None:
                rs_examuser203 = rs1
            else:
                rs_examuser203 = rs1[0]

            # 数据库查询文件保存
            with open(save_address, "a+") as f:
                if rs_examuser203 == 0:
                    f.write("用户与角色管理课件题目九:用户examuser203存在 ,---ok" + '\n')
                else:
                    f.write("用户与角色管理课件题目九:用户examuser203不存在 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目九:失败')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目九:成功")


class Cat_score_10(object):
    """
    题目10
    为examuser204用户授予系统权限create session、crea
    """

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
            print("用户与角色管理课件题目十:数据打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_examuser204(self):
        rs_list = []

        try:
            sql = "select privilege,admin_option from dba_sys_privs where grantee='EXAMUSER204'"
            sql_1 = "select count(*) from dba_tables where owner='EXAMUSER204' and table_name='TEST1'"

            # 确认用户james用户默认表空间
            self.cr.execute(sql)
            rs = self.cr.fetchall()
            for i in rs:
                rs_list.append(i[0][0])

            with open(save_address, "a+") as f:
                if "CREATE TABLE" in rs_list and "CREATE SESSION" in rs_list:
                    f.write("用户与角色管理课件题目十:用户examuser204具备系统权限 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十:用户examuser204不具备系统权限 ,---error" + '\n')

            # 确认用户test1状态
            self.cr.execute(sql_1)
            rs1 = self.cr.fetchall()
            if len(rs1) > 0:
                rs_user_test1 = rs1[0][0]
            else:
                rs_user_test1 = rs1

            with open(save_address, "a+") as f:
                if rs_user_test1 == 1:
                    f.write("用户与角色管理课件题目十:用户examuser204拥有表test1 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十:用户examuser204不拥有表test1 ,---error" + '\n')

        except:
            print("操作用户与角色管理课件题目十:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目十:成功")


class Cat_score_11(object):
    """
    题目11
    sys用户登录数据库，回收examuser205用户的系create any table统权限。
    """

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
            print("用户与角色管理课件题目十一:数据打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_examuser205(self):
        """查询用户examuser205系统权限"""

        try:
            sql = "select count(*) from dba_sys_privs where grantee='EXAMUSER205' and privilege='CREATE ANY TABLE'"

            # 用户examuser202是否存在
            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()

            if rs == None:
                rs_examuser202 = rs
            else:
                rs_examuser202 = rs[0]

            with open(save_address, "a+") as f:

                if rs_examuser202 == 0:
                    f.write("用户与角色管理课件题目十一:用户examuser205系统权限存在 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十一:用户examuser205系统权限不存在 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十一:失败')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目十一:成功")


class Cat_score_12(object):
    """
    题目12
    将查询scott.dept表的对象权限授予用户examuser206
    """

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
            print("用户与角色管理课件题目十二:数据库打开失败")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_examuser206(self):

        filename_log = num_12_log

        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十二:文件/examdata/result/grant_object_priv.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十二:文件/examdata/result/grant_object_priv.log不存在,---error" + '\n')

            sql = "select count(*) from dba_tab_privs where grantee='EXAMUSER206' and owner='SCOTT' AND TABLE_NAME='DEPT' and PRIVILEGE='SELECT'"
            sql_1 = "select loc,dname from scott.dept where deptno=10"

            # 查询用户examuser206是否具备对象权限
            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()

            if rs == None:
                rs_examuser206 = rs
            else:
                rs_examuser206 = rs[0]

            with open(save_address, "a+") as f:

                if rs_examuser206 == 1:
                    f.write("用户与角色管理课件题目十二:用户examuser206具备对象权限 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十二:用户examuser206不具备对象权限 , ---error" + '\n')

            # 查询表scott.dept表数据是否已更新
            self.cr.execute(sql_1)
            # 获取一条记录
            rs_updata = self.cr.fetchall()

            if len(rs_updata) > 0:
                rs_updatas = rs_updata[0]
            else:
                rs_updatas = rs_updata

            with open(save_address, "a+") as f:
                if "AAA" in rs_updatas and "BBB" in rs_updatas:
                    f.write("用户与角色管理课件题目十二:表scott.dept表数据已更新 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十二:表scott.dept表数据未更新 ,--- erro" + '\n')


        except:
            print('操作用户与角色管理课件题目十二:失败')

        else:
            f.close()
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目十二:成功")


class Cat_score_13(object):
    """
    题目13
    查询examuser217用户被授予的对象权限和列权限，然后显示该用户授出的对象权限
    """

    def query_oracle_examuser217(self):

        filename_log = num_13_log

        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十三:文件/examdata/result/grant_user217_priv.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十三:文件/examdata/result/grant_user217_priv.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):

                f = open(num_13_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'dba_tab_privs|all_tab_privs|dba_col_privs|all_col_privs', line_str)

                if "dba_tab_privs" in str_1 or "all_tab_privs" in str_1:
                    a += 1

                if "dba_col_privs" in str_1 or "all_col_privs" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a >= 2:
                        f.write("用户与角色管理课件题目十三:文件/examdata/result/grant_user217_priv.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目十三:文件/examdata/result/grant_user217_priv.log不存在关键信息,---error" + '\n')
            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十三:文件/examdata/result/grant_user217_priv.log不存在关键信息,---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十三:失败')

        else:
            f.close()
            print("操作用户与角色管理课件题目十三:成功")


class Cat_score_14(object):
    """
    题目14
    以SCOTT用户登录到oradb数据库，收回examuser207用户查询DEPT表的权限。
    """

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
            print("用户与角色管理课件题目十四:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_examuser207(self):
        """查询用户examuser207系统权限"""

        try:
            sql = "select count(*) from user_tab_privs where grantee='EXAMUSER207' and TABLE_NAME='DEPT' and PRIVILEGE='SELECT'"

            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()

            if rs == None:
                rs_examuser207 = rs
            else:
                rs_examuser207 = rs[0]

            with open(save_address, "a+") as f:

                if rs_examuser207 == 0:
                    f.write("用户与角色管理课件题目十四:用户examuser207权限存在 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十四:用户examuser207权限不存在 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十四:失败')


        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目十四:成功")


class Cat_score_15(object):
    """
    题目14
    以SCOTT用户登录到oradb数据库，收回examuser207用户查询DEPT表的权限。
    """

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
            print("用户与角色管理课件题目十五:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_def_role(self):
        """查询用户examuser207系统权限"""

        try:
            sql = "select count(*) from dba_roles where role='DEF_ROLE'"
            sql_1 = "select AUTHENTICATION_TYPE from dba_roles where role='DEF_ROLE'"
            sql_2 = "select GRANTED_ROLE from dba_role_privs where grantee='DEF_ROLE'"
            sql_3 = "select privilege from role_sys_privs where role='DEF_ROLE'"
            sql_4 = "select count(*) from role_tab_privs where role='DEF_ROLE' and PRIVILEGE='SELECT' AND owner='SCOTT' AND TABLE_NAME='DEPT'"

            # 查询角色def_role是否存在
            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()

            if rs == None:
                rs_def_role = rs
            else:
                rs_def_role = rs[0]

            with open(save_address, "a+") as f:

                if rs_def_role == 1:
                    f.write("用户与角色管理课件题目十五:用户examuser207权限存在 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十五:用户examuser207权限不存在 , ---error" + '\n')

            # 查询角色验证方式
            self.cr.execute(sql_1)
            # 获取一条记录
            rs_1 = self.cr.fetchone()

            if rs_1 != None:
                rs_1 = rs_1[0]

            with open(save_address, "a+") as f:

                if rs_1 == "NONE":
                    f.write("用户与角色管理课件题目十五:查询角色验证方式正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十五:查询角色验证方式错误 , ---error" + '\n')

            # 查询角色赋予的系统角色
            self.cr.execute(sql_2)
            # 获取一条记录
            rs_2 = self.cr.fetchone()

            if rs_2 != None:
                rs_2 = rs_2[0]

            with open(save_address, "a+") as f:

                if rs_2 == "RESOURCE":
                    f.write("用户与角色管理课件题目十五:查询角色赋予的系统角色正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十五:查询角色赋予的系统角色错误 , ---error" + '\n')

            # 查询角色赋予的系统权限
            self.cr.execute(sql_3)
            # 获取一条记录
            rs_3 = self.cr.fetchone()

            if rs_3 != None:
                rs_3 = rs_3[0]

            with open(save_address, "a+") as f:

                if rs_3 == "CREATE SESSION":
                    f.write("用户与角色管理课件题目十五:查询角色赋予的系统权限正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十五:查询角色赋予的系统权限错误 , ---error" + '\n')

            # 查询角色赋予的对象权限
            self.cr.execute(sql_4)
            # 获取一条记录
            rs_4 = self.cr.fetchone()

            if rs_4 != None:
                rs_4 = rs_4[0]

            with open(save_address, "a+") as f:

                if rs_4 == 1:
                    f.write("用户与角色管理课件题目十五:查询角色赋予的对象权限正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十五:查询角色赋予的对象权限错误 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十五:')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目十五:成功")


class Cat_score_16(object):
    """
    题目16
    检索角色exam_role200具有的系统授权，
    """

    def query_oracle_exam_role200(self):

        filename_log = num_16_log

        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十六:文件/examdata/result/exam_role_priv200.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十六:文件/examdata/result/exam_role_priv200.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):
                f = open(num_16_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'EXAM_ROLE200|dba_sys_prvis|all_tab_privs', line_str)

                if "EXAM_ROLE200" in str_1 and "dba_sys_prvis" in str_1:
                    a += 1

                if "EXAM_ROLE200" in str_1 and "all_tab_privs" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write("用户与角色管理课件题目十六:文件/examdata/result/exam_role_priv200.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目十六:文件/examdata/result/exam_role_priv200.log不存在关键信息,---error" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十六:文件/examdata/result/exam_role_priv200.log不存在关键信息,---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十六:失败')

        else:
            f.close()
            print("操作用户与角色管理课件题目十六:成功")


class Cat_score_17(object):
    """
    题目17
    显示角色exam_role201具有的对象授权和列权限，
    """

    def query_oracle_exam_role201(self):

        filename_log = num_17_log

        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十七:文件/examdata/result/exam_role_obj201.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十七:文件/examdata/result/exam_role_obj201.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):
                f = open(num_17_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # 匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'EXAM_ROLE201|dba_tab_privs|dba_col_privs', line_str)

                if "EXAM_ROLE201" in str_1 and "dba_tab_privs" in str_1 and "dba_col_privs" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write("用户与角色管理课件题目十七:文件/examdata/result/exam_role_obj201.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目十七:文件/examdata/result/exam_role_obj201.log不存在关键信息,---error" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十七:文件/examdata/result/exam_role_obj201.log不存在关键信息,---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十七:失败')

        else:
            f.close()
            print("操作用户与角色管理课件题目十七:成功")


class Cat_score_18(object):
    """
    题目18
    显示角色examuser207具有角色信息
    """

    def query_oracle_examuser207(self):

        filename_log = num_18_log
        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十八:文件/examdata/result/user207_role_priv.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十八:文件/examdata/result/user207_role_priv.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):
                f = open(num_18_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'EXAMUSER207|dba_role_privs', line_str)

                if "EXAMUSER207" in str_1 and "dba_role_privs" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write("用户与角色管理课件题目十八:文件/examdata/result/exam_role_priv200.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目十八:文件/examdata/result/exam_role_priv200.log不存在关键信息,---error" + '\n')
            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十八:文件/examdata/result/exam_role_priv200.log不存在关键信息,---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十八:失败')

        else:
            f.close()
            print("操作用户与角色管理课件题目十八:成功")


class Cat_score_19(object):
    """
    题目19
    通过数据库包，实现精细访问控制
    """

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
            print("用户与角色管理课件题目十九:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_examuser208_09_10(self):

        filename_log = num_19_log
        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十九:文件/examdata/result/user_priv5.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十九:文件/examdata/result/user_priv5.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):
                f = open(num_19_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'examuser209|examuser210|SCOTT.EMP', line_str)

                if "examuser209" in str_1 and "examuser210" in str_1 and "SCOTT.EMP" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write("用户与角色管理课件题目十九:文件/examdata/result/user_priv5.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目十九:文件/examdata/result/user_priv5.log不存在关键信息,---error" + '\n')
            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目十九:文件/examdata/result/user_priv5.log不存在关键信息,---error" + '\n')

            # 查询用户examuser208具有权限
            sql = "select privilege from dba_tab_privs where grantee='EXAMUSER208' and owner='SCOTT' AND table_name='EMP'"

            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchall()
            rs_list = []

            # rs_list_tuple = [("SELECT",), ("INSERT",), ("DELETE",)]

            for rs_tuple in rs:
                rs_list.append(rs_tuple[0])

            with open(save_address, "a+") as f:

                if "SELECT" in rs_list and "INSERT" in rs_list and "DELETE" in rs_list:
                    f.write("用户与角色管理课件题目十九:用户examuser208具有权限 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目十九:用户examuser208不具有权限 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目十九:失败')

        else:
            f.close()
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目十九:成功")


class Cat_score_20(object):
    """
    题目20
    登录oradb数据库，建立PROFILE
    """

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
            print("用户与角色管理课件题目二十:数据打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_PROFILE(self):

        try:

            # 查询用户examuser208具有权限
            sql = "select limit from dba_profiles where resource_name='FAILED_LOGIN_ATTEMPTS' and profile='PASSWORD_MANAGEMENT'"
            sql_validity = "select limit from dba_profiles where resource_name='PASSWORD_LIFE_TIME' and profile='PASSWORD_MANAGEMENT'"
            sql_time = "select limit from dba_profiles where resource_name='PASSWORD_REUSE_TIME' and profile='PASSWORD_MANAGEMENT'"
            sql_file = "select count(*) from dba_users where username='EXAMUSER211' and profile='PASSWORD_MANAGEMENT'"

            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()
            if rs == None:
                rs = rs

            else:
                rs = rs[0]

            with open(save_address, "a+") as f:

                if rs == 8:
                    f.write("用户与角色管理课件题目二十:查询password_management  profile 文件最大登陆失败次数正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十:查询password_management  profile 文件最大登陆失败次数错误 , ---error" + '\n')

            # 查询password_management profile文件口令有效期
            self.cr.execute(sql_validity)
            # 获取一条记录
            rs_validity = self.cr.fetchone()

            if rs_validity == None:
                rs_validity = rs_validity

            else:
                rs_validity = rs_validity[0]

            with open(save_address, "a+") as f:

                if rs_validity == 120:
                    f.write("用户与角色管理课件题目二十:查询password_management  profile 文件口令有效期正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十:查询password_management  profile 文件口令有效期错误 , ---error" + '\n')

            # 查询password_management  profile 文件口令重用时间
            self.cr.execute(sql_time)
            # 获取一条记录
            rs_time = self.cr.fetchone()

            if rs_time == None:
                rs_time = rs_time
            else:
                rs_time = rs_time[0]

            with open(save_address, "a+") as f:

                if rs_time == 60:
                    f.write("用户与角色管理课件题目二十:查询password_management  profile 文件口令重用时间正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十:查询password_management  profile 文件口令重用时间错误 , ---error" + '\n')

            # 查询用户examuser211是否具有password_management  profile 文件
            self.cr.execute(sql_file)
            # 获取一条记录
            rs_file = self.cr.fetchone()

            if rs_file == None:
                rs_file = rs_file
            else:
                rs_file = rs_file[0]

            with open(save_address, "a+") as f:

                if rs_file == 1:
                    f.write("用户与角色管理课件题目二十:查询用户examuser211是否具有password_management  profile 文件正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十:查询用户examuser211是否具有password_management  profile 文件错误 , ---error" + '\n')

        except:

            print('操作用户与角色管理课件题目二十:失败')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目二十:成功")


class Cat_score_21(object):
    """
    题目21
    询DEFAULT PROFILE的口令函数、口令有效期
    """

    def query_oracle_default_profile(self):

        filename_log = num_20_log
        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目二十一:文件/examdata/result/query_profile_value.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目二十一:文件/examdata/result/query_profile_value.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):
                f = open(num_20_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'dba_profiles|DEFAULT', line_str)

                if "dba_profiles" in str_1 and "DEFAULT" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write("用户与角色管理课件题目二十一:文件/examdata/result/query_profile_value.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目二十一:文件/examdata/result/query_profile_value.log不存在关键信息,---error" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目二十一:文件/examdata/result/query_profile_value.log不存在关键信息,---error" + '\n')

        except:
            print('操作用户与角色管理课件题目二十一:失败')

        else:
            f.close()
            print("操作用户与角色管理课件题目二十一:成功")


class Cat_score_22(object):
    """
    题目22
    使用PROFILE管理资源
    """

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
            print("用户与角色管理课件题目二十二:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_profile_manage(self):

        try:

            # 查询resourece_management profile并发数
            sql_num = "select limit from dba_profiles where resource_name='SESSIONS_PER_USER' and profile='RESOURECE_MANAGEMENT'"
            sql_jion_time = "select limit from dba_profiles where resource_name='CONNECT_TIME' and profile='RESOURECE_MANAGEMENT'"
            sql_free_time = "select limit from dba_profiles where resource_name='IDLE_TIME' and profile='RESOURECE_MANAGEMENT'"
            sql_file = "select profile from dba_users where username='EXAMUSER211'"

            self.cr.execute(sql_num)
            # 获取一条记录
            rs_num = self.cr.fetchone()
            if rs_num == None:
                rs_num = rs_num
            else:
                rs_num = rs_num[0]

            with open(save_address, "a+") as f:

                if rs_num == 2:
                    f.write("用户与角色管理课件题目二十二:查询resourece_management profile并发数正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十二:查询resourece_management profile并发数错误 , ---error" + '\n')

            # 查询resourece_management profile连接时长
            self.cr.execute(sql_jion_time)
            # 获取一条记录
            rs_jion_time = self.cr.fetchone()

            if rs_jion_time == None:
                rs_jion_time = rs_jion_time
            else:
                rs_jion_time = rs_jion_time[0]

            with open(save_address, "a+") as f:

                if rs_jion_time == 60:
                    f.write("用户与角色管理课件题目二十二:查询resourece_management profile连接时长正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十二:查询resourece_management profile连接时长错误 , ---error" + '\n')

            # 查询resourece_management profile空闲时间
            self.cr.execute(sql_free_time)
            # 获取一条记录
            rs_free_time = self.cr.fetchone()

            if rs_free_time == None:
                rs_free_time = rs_free_time
            else:
                rs_free_time = rs_free_time[0]

            with open(save_address, "a+") as f:

                if rs_free_time == 10:
                    f.write("用户与角色管理课件题目二十二:查询resourece_management profile空闲时间正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十二:查询resourece_management profile空闲时间错误 , ---error" + '\n')

            # 查询用户examuser211用户的profile文件
            self.cr.execute(sql_file)
            # 获取一条记录
            rs_file = self.cr.fetchone()

            if rs_file == None:
                rs_file = rs_file

            else:
                rs_file = rs_file[0]

            with open(save_address, "a+") as f:

                if rs_file == "RESOURECE_MANAGEMENT":
                    f.write("用户与角色管理课件题目二十二:查询用户examuser211用户的profile文件正确 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十二:查询用户examuser211用户的profile文件错误 , ---error" + '\n')

        except:

            print('操作用户与角色管理课件题目二十二:失败')

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目二十二:成功")


class Cat_score_23(object):
    """
    题目23
    删除exam_management PROFILE
    """

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
            print("用户与角色管理课件题目二十三:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_oracle_exam_management(self):

        filename_log = num_23_log
        try:
            # 判断文件是否存在
            if os.path.exists(filename_log):
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目二十三:文件/examdata/result/query_profile_user212.log存在,---ok" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目二十三:文件/examdata/result/query_profile_user212.log不存在,---error" + '\n')

            # 判断存在关键信息
            if os.path.exists(filename_log):
                f = open(num_23_log)
                lines = f.readlines()
                line_list = []
                a = 0

                for line in lines:
                    line = line.strip('\n')
                    line_list.append(line)

                # re匹配关键词
                line_str = " ".join(line_list)
                str_1 = re.findall(r'profile|dba_users|EXAMUSER212', line_str)

                if "profile" in str_1 and "dba_users" in str_1 and "EXAMUSER212" in str_1:
                    a += 1

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write("用户与角色管理课件题目二十三:文件/examdata/result/query_profile_user212.log存在关键信息,---ok" + '\n')

                    else:
                        f.write("用户与角色管理课件题目二十三:文件/examdata/result/query_profile_user212.log不存在关键信息,---error" + '\n')

            else:
                with open(save_address, "a+") as f:
                    f.write("用户与角色管理课件题目二十三:文件/examdata/result/query_profile_user212.log不存在关键信息,---error" + '\n')

            # 查询用户examuser208具有权限
            sql = "select count(*) from dba_profiles where profile='EXAM_MANAGEMENT'"

            self.cr.execute(sql)
            # 获取一条记录
            rs = self.cr.fetchone()

            if rs == None:
                rs = rs
            else:
                rs = rs[0]

            with open(save_address, "a+") as f:

                if rs == 0:
                    f.write("用户与角色管理课件题目二十三:确认exam_management PROFILE删除成功 ,---ok" + '\n')

                else:
                    f.write("用户与角色管理课件题目二十三:确认exam_management PROFILE删除错误 , ---error" + '\n')

        except:
            print('操作用户与角色管理课件题目二十三:失败')

        else:
            f.close()
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作用户与角色管理课件题目二十三:成功")


def run():
    Cat_score_1().query_status_instance()
    Cat_score_2().query_oracle_user7()
    Cat_score_3().query_oracle_user20()
    Cat_score_4().Search_file()
    Cat_score_5().Search_file()
    Cat_score_6().query_oracle_adams()
    Cat_score_7().query_oracle_james()
    Cat_score_8().Search_log()
    Cat_score_9().query_oracle_examuser202()
    Cat_score_10().query_oracle_examuser204()
    Cat_score_11().query_oracle_examuser205()
    Cat_score_12().query_oracle_examuser206()
    Cat_score_13().query_oracle_examuser217()
    Cat_score_14().query_oracle_examuser207()
    Cat_score_15().query_oracle_def_role()
    Cat_score_16().query_oracle_exam_role200()
    Cat_score_17().query_oracle_exam_role201()
    Cat_score_18().query_oracle_examuser207()
    Cat_score_19().query_oracle_examuser208_09_10()
    Cat_score_20().query_oracle_PROFILE()
    Cat_score_21().query_oracle_default_profile()
    Cat_score_22().query_oracle_profile_manage()
    Cat_score_23().query_oracle_exam_management()


run()
