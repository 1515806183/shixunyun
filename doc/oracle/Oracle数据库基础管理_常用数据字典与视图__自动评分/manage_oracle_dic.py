# coding=utf-8

username = "system"
pwd = "oracle"
ip = "127.0.0.1"
tns = "oradb"

# 正式文件
save_address = "/etc/vsfox/score.txt"
# 测试文本
save_address_test = "./test.txt"

oracle_1_file = '/examdata/result/constraint_query.result'
oracle_2_file = '/examdata/result/query_segment_mb.result'
oracle_3_file = '/examdata/result/default_tbs_sys.result'
oracle_4_file = '/examdata/result/query_sum_mb.result'
oracle_5_file = '/examdata/result/query_user201.log'
oracle_6_file = '/examdata/result/system_default_tbs.log'
oracle_7_file = '/examdata/result/query_date.log'

import os


class Cat_score_1(object):
    """题目一"""

    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_1_file

            if os.path.exists(filename):
                with open(file_address, 'w') as f:
                    f.write("数据库数据字典与视图课件题目一:%s文件存在, ---ok\n" % filename)

                line_list_find = ""
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line
                f_read.close()

                with open(file_address, "a+") as f:

                    if "dba_constraints" in line_list_find and "CONSTRAINT_NAME" in line_list_find and "CONSTRAINT_TYPE" in line_list_find and "TABLE_NAME" in line_list_find and "OWNER" in line_list_find:
                        f.write(("数据库数据字典与视图课件题目一:%s文件中存在信息, ---ok" + '\n') % filename)

                    else:
                        f.write(("数据库数据字典与视图课件题目一:%s文件中不存在信息, ---error" + '\n') % filename)

            else:
                with open(file_address, 'w') as f:
                    f.write(("数据库数据字典与视图课件题目一:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目一:失败")

        else:

            print("数据库数据字典与视图课件题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_2_file

            if os.path.exists(filename):
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目二:%s文件存在, ---ok" + '\n') % filename)

                    # 查看文件，查看是否存在命令
                line_list_find = ''
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line
                f_read.close()

                with open(file_address, 'a+') as f:
                    if "dba_segments" in line_list_find and "owner" in line_list_find and "owner" in line_list_find and "segment_type" in line_list_find and "bytes" in line_list_find and "order by" in line_list_find:
                        f.write(("数据库数据字典与视图课件题目二:%s文件中存在信息, ---ok" + '\n') % filename)
                    else:
                        f.write(("数据库数据字典与视图课件题目二:%s文件中不存在信息, ---error" + '\n') % filename)

            else:
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目二:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目二:失败")

        else:

            print("数据库数据字典与视图课件题目二:成功")


class Cat_score_3(object):
    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_3_file
            if os.path.exists(filename):
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目三:%s文件存在, ---ok" + '\n') % filename)

                line_list_find = ""
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line

                f_read.close()
                with open(file_address, 'a+') as f:

                    if "dba_users" in line_list_find and "default_tablespace" in line_list_find:

                        f.write(("数据库数据字典与视图课件题目三:%s文件中存在信息, ---ok" + '\n') % filename)
                    else:
                        f.write(("数据库数据字典与视图课件题目三:%s文件中不存在信息, ---error" + '\n') % filename)

            else:
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目三:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目三:失败")

        else:

            print("数据库数据字典与视图课件题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_4_file

            if os.path.exists(filename):
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目四:%s文件存在, ---ok" + '\n') % filename)
                line_list_find = ""
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line

                f_read.close()
                with open(file_address, 'a+') as f:
                    if "dba_segments" in line_list_find and "sum" in line_list_find and "bytes" in line_list_find:

                        f.write(("数据库数据字典与视图课件题目四:%s文件中存在信息, ---ok" + '\n') % filename)
                    else:
                        f.write(("数据库数据字典与视图课件题目四:%s文件中不存在信息, ---error" + '\n') % filename)

            else:
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目四:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目四:失败")

        else:

            print("数据库数据字典与视图课件题目四:成功")


class Cat_score_5(object):

    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_5_file

            if os.path.exists(filename):
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目五:%s文件存在, ---ok" + '\n') % filename)

                line_list_find = ""
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line
                f_read.close()
                with open(file_address, 'a+') as f:

                    if "max_bytes" in line_list_find and "dba_ts_quotas" in line_list_find and "EXAMUSER201" in line_list_find:

                        f.write(("数据库数据字典与视图课件题目五:%s文件中存在信息, ---ok" + '\n') % filename)
                    else:
                        f.write(("数据库数据字典与视图课件题目五:%s文件中不存在信息, ---error" + '\n') % filename)



            else:
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目五:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目五:失败")

        else:

            print("数据库数据字典与视图课件题目五:成功")


class Cat_score_6(object):

    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_6_file

            if os.path.exists(filename):
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目六:%s文件存在, ---ok" + '\n') % filename)
                line_list_find = ""
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line
                f_read.close()

                with open(file_address, 'a+') as f:

                    if "dba_users" in line_list_find and "temporary_tablespace" in line_list_find and "SCOTT " in line_list_find and "SYSTEM" in line_list_find:

                        f.write(("数据库数据字典与视图课件题目六:%s文件中存在信息, ---ok" + '\n') % filename)
                    else:
                        f.write(("数据库数据字典与视图课件题目六:%s文件中不存在信息, ---error" + '\n') % filename)

            else:
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目六:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目六:失败")

        else:

            print("数据库数据字典与视图课件题目六:成功")


class Cat_score_7(object):

    @staticmethod
    def run():
        try:

            file_address = save_address
            filename = oracle_7_file

            if os.path.exists(filename):
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目七:%s文件存在, ---ok" + '\n') % filename)

                line_list_find = ""
                f_read = open(filename, 'r')

                for line in f_read.readlines():
                    line = line.strip('\n')
                    line_list_find += line

                f_read.close()

                with open(file_address, 'a+') as f:

                    if "sysdate" in line_list_find:
                        f.write(("数据库数据字典与视图课件题目七:%s文件中存在信息, ---ok" + '\n') % filename)
                    else:
                        f.write(("数据库数据字典与视图课件题目七:%s文件中不存在信息, ---error" + '\n') % filename)

            else:
                with open(file_address, 'a+') as f:
                    f.write(("数据库数据字典与视图课件题目七:%s文件不存在, ---error" + '\n') % filename)

        except:
            print("数据库数据字典与视图课件题目七:失败")

        else:

            print("数据库数据字典与视图课件题目七:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()
    Cat_score_5().run()
    Cat_score_6().run()
    Cat_score_7().run()


run()
