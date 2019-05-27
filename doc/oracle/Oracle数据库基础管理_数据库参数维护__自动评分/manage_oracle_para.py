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

oracle_6_file = '/examdata/result/pfile_tmp.ora'
oracle_7_file = '/examdata/result/query_default_undo.log'
oracle_8_file = '/examdata/result/query_undo_retention.log'
oracle_9_file = '/examdata/result/query_para_file.log'
oracle_10_file = '/examdata/result/query_para_block.log'
oracle_11_file = '/examdata/result/query_date_format.log'

import cx_Oracle
import os


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
            print("数据库参数维护课件题目一:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):
        """
        select status from v$instance;
        """
        try:
            with open(save_address, "w") as f:
                # 查看参数undo_retention值
                sql = "select value from v$parameter where name='undo_retention'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()
                # 文件判断保存
                if int(rs[0]) >= 5400:
                    f.write(("数据库参数维护课件题目一:查看参数undo_retention值:%s正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目一:查看参数undo_retention值:%s错误,---error" + '\n') % rs[0])

            # 查看查询参数processes值
            with open(save_address, "a+") as f:

                sql = "select value from v$parameter where upper(name)='PROCESSES'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                # 查询文件判断保存
                if int(rs[0]) >= 550:
                    f.write(("数据库参数维护课件题目一:查看参数processes值:%s正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目一:查看参数processes值:%s错误,---error" + '\n') % rs[0])

            # 查看查询参数job值
            with open(save_address, "a+") as f:

                sql = "select value from v$parameter where upper(name)='JOB_QUEUE_PROCESSES'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                # 查询文件判断保存
                if int(rs[0]) >= 15:
                    f.write(("数据库参数维护课件题目一:查看参数job值:%s正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目一:查看参数job值:%s错误,---error" + '\n') % rs[0])

        except:
            print("操作数据库参数维护课件题目一:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库参数维护课件题目一:成功")


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
            print("数据库参数维护课件题目二:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):
        """
        请配置oradb数据库支持300个会话，保留100个做专有连接；
        """
        try:
            with open(save_address, "a+") as f:
                # 查看参数sessions值
                sql = "select value from v$parameter where name='sessions'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()
                # 文件判断保存
                if int(rs[0]) >= 300:
                    f.write(("数据库参数维护课件题目二:查看参数sessions值:%s正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目二:查看参数sessions值:%s错误,---error" + '\n') % rs[0])

            # 查看参数shared_server_sessions
            with open(save_address, "a+") as f:

                sql = "select value from v$parameter where name='shared_server_sessions'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = (0,)
                else:
                    rs = rs

                # 查询文件判断保存
                if int(rs[0]) <= 200:
                    f.write(("数据库参数维护课件题目二:查看参数shared_server_sessions值:%s正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目二:查看参数shared_server_sessions值:%s错误,---error" + '\n') % rs[0])


        except:
            print("操作数据库参数维护课件题目二:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库参数维护课件题目二:成功")


class Cat_score_3(object):
    """题目 3"""

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
            print("数据库参数维护课件题目三:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):
        """
        请配置oradb数据库支持300个会话，保留100个做专有连接；
        """
        try:

            # 查看参数db_16k_cache_size值
            with open(save_address, "a+") as f:

                sql = "select value from v$parameter where name='db_16k_cache_size'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = (0,)
                else:
                    rs = rs

                # 查询文件判断保存
                if int(rs[0]) <= 200:
                    f.write(("数据库参数维护课件题目三:查看参数db_16k_cache_size值:%s正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目三:查看参数db_16k_cache_size值:%s错误,---error" + '\n') % rs[0])


        except:
            print("操作数据库参数维护课件题目三:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库参数维护课件题目三:成功")


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
            print("数据库参数维护课件题目四:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:

            # 查看参数db_16k_cache_size值
            with open(save_address, "a+") as f:

                sql = "Select status from v$instance"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = ('CLOSE',)
                else:
                    rs = rs

                # 查询文件判断保存
                if rs[0] == 'OPEN':
                    f.write(("数据库参数维护课件题目四:查看数据库状态:%s 正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目四:查看数据库状态:%s 错误,---error" + '\n') % rs[0])

        except:
            print("操作数据库参数维护课件题目四:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库参数维护课件题目四:成功")


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
            print("数据库参数维护课件题目五:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):

        try:
            # 查看参数sec_case_sensitive_logon值
            with open(save_address, "a+") as f:

                sql = "select value from v$parameter where name='sec_case_sensitive_logon'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = ('True',)
                else:
                    rs = rs

                # 查询文件判断保存
                if rs[0] == 'FALSE':
                    f.write(("数据库参数维护课件题目五:查看参数sec_case_sensitive_logon值:%s 正确,---ok" + '\n') % rs[0])

                else:
                    f.write(("数据库参数维护课件题目五:查看参数sec_case_sensitive_logon值:%s 错误,---error" + '\n') % rs[0])

        except:
            print("操作数据库参数维护课件题目五:失败")

        else:
            # 关闭数据库
            self.cr.close()
            self.db.close()
            print("操作数据库参数维护课件题目五:成功")


class Cat_score_6(object):

    def query_status_instance(self):

        try:
            filename = oracle_6_file

            with open(save_address, "a+") as f:
                if os.path.exists(filename):
                    f.write(("数据库参数维护课件题目六:查看文件:%s 存在,---ok" + '\n') % filename)

                else:
                    f.write(("数据库参数维护课件题目六:查看文件:%s 不存在,---error" + '\n') % filename)

        except:
            print("操作数据库参数维护课件题目六:失败")

        else:

            print("操作数据库参数维护课件题目六:成功")


class Cat_score_7(object):

    def query_status_instance(self):
        try:
            filename = oracle_7_file

            if os.path.exists(filename):

                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目七:查看文件:%s 存在,---ok" + '\n') % filename)

                f = open(filename, 'r')
                line_list_find = []
                a = 0
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_find.append(line)

                f.close()

                for line_str in line_list_find:
                    if 'undo_tablespace' in line_str:
                        a += 1
                    else:
                        pass

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write(("数据库参数维护课件题目七:文件:%s 存在关键信息,---ok" + '\n') % filename)
                    else:
                        f.write(("数据库参数维护课件题目七:文件:%s 不存在关键信息,---error" + '\n') % filename)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目七:查看文件:%s 不存在,---error" + '\n') % filename)
                    f.write(("数据库参数维护课件题目七:文件:%s 不存在关键信息,---error" + '\n') % filename)

        except:
            print("操作数据库参数维护课件题目七:失败")

        else:

            print("操作数据库参数维护课件题目七:成功")


class Cat_score_8(object):
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
            print("数据库参数维护课件题目四:数据库打开错误")

        else:
            self.cr = cr
            self.db = db

    def query_status_instance(self):
        try:
            filename = oracle_8_file

            if os.path.exists(filename):

                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目八:查看文件:%s 存在,---ok" + '\n') % filename)

                f = open(filename, 'r')
                line_list_find = []
                a = 0
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_find.append(line)

                f.close()

                for line_str in line_list_find:
                    if 'undo_retention' in line_str:
                        a += 1
                    else:
                        pass

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write(("数据库参数维护课件题目八:文件:%s 存在关键信息,---ok" + '\n') % filename)
                    else:
                        f.write(("数据库参数维护课件题目八:文件:%s 不存在关键信息,---error" + '\n') % filename)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目八:查看文件:%s 不存在,---error" + '\n') % filename)
                    f.write(("数据库参数维护课件题目八:文件:%s 不存在关键信息,---error" + '\n') % filename)

            # 查看参数undo_retention值
            with open(save_address, "a+") as f:

                sql = "select value from v$parameter where name='undo_retention'"
                self.cr.execute(sql)
                rs = self.cr.fetchone()

                if rs[0] == None:
                    rs = ('0',)
                else:
                    rs = rs

                # 查询文件判断保存
                if int(rs[0]) == 4800:
                    f.write(("数据库参数维护课件题目八:查询参数undo_retention值:%s 正确,---ok" + '\n') % rs[0])
                else:
                    f.write(("数据库参数维护课件题目八:查询参数undo_retention值:%s 错误,---error" + '\n') % rs[0])

        except:
            print("操作数据库参数维护课件题目八:失败")

        else:
            print("操作数据库参数维护课件题目八:成功")


class Cat_score_9(object):

    def query_status_instance(self):
        try:
            filename = oracle_9_file

            if os.path.exists(filename):

                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目九:查看文件:%s 存在,---ok" + '\n') % filename)

                f = open(filename, 'r')
                line_list_find = []
                a = 0
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_find.append(line)

                f.close()

                for line_str in line_list_find:
                    if 'pfile' in line_str or 'spfile' in line_str:
                        a += 1
                    else:
                        pass

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write(("数据库参数维护课件题目九:文件:%s 存在关键信息,---ok" + '\n') % filename)
                    else:
                        f.write(("数据库参数维护课件题目九:文件:%s 不存在关键信息,---error" + '\n') % filename)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目九:查看文件:%s 不存在,---error" + '\n') % filename)
                    f.write(("数据库参数维护课件题目九:文件:%s 不存在关键信息,---error" + '\n') % filename)

        except:
            print("操作数据库参数维护课件题目九:失败")

        else:
            print("操作数据库参数维护课件题目九:成功")



class Cat_score_10(object):

    def query_status_instance(self):
        try:
            filename = oracle_10_file

            if os.path.exists(filename):

                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目十:查看文件:%s 存在,---ok" + '\n') % filename)

                f = open(filename, 'r')
                line_list_find = []
                a = 0
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_find.append(line)
                f.close()

                for line_str in line_list_find:
                    if 'db_block_size' in line_str:
                        a += 1
                    else:
                        pass

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write(("数据库参数维护课件题目十:文件:%s 存在关键信息,---ok" + '\n') % filename)
                    else:
                        f.write(("数据库参数维护课件题目十:文件:%s 不存在关键信息,---error" + '\n') % filename)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目十:查看文件:%s 不存在,---error" + '\n') % filename)
                    f.write(("数据库参数维护课件题目十:文件:%s 不存在关键信息,---error" + '\n') % filename)

        except:
            print("操作数据库参数维护课件题目十:失败")

        else:
            print("操作数据库参数维护课件题目十:成功")


class Cat_score_11(object):

    def query_status_instance(self):
        try:
            filename = oracle_11_file

            if os.path.exists(filename):

                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目十一:查看文件:%s 存在,---ok" + '\n') % filename)

                f = open(filename, 'r')
                line_list_find = []
                a = 0
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_find.append(line)

                f.close()

                for line_str in line_list_find:
                    if "alter session set nls_date_format='YYYY-MM-DD'" in line_str:
                        a += 1
                    else:
                        pass

                with open(save_address, "a+") as f:
                    if a > 0:
                        f.write(("数据库参数维护课件题目十一:文件:%s 存在关键信息,---ok" + '\n') % filename)
                    else:
                        f.write(("数据库参数维护课件题目十一:文件:%s 不存在关键信息,---error" + '\n') % filename)

            else:
                with open(save_address, "a+") as f:
                    f.write(("数据库参数维护课件题目十一:查看文件:%s 不存在,---error" + '\n') % filename)
                    f.write(("数据库参数维护课件题目十一:文件:%s 不存在关键信息,---error" + '\n') % filename)

        except:
            print("操作数据库参数维护课件题目十一:失败")

        else:
            print("操作数据库参数维护课件题目十一:成功")


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


run()
