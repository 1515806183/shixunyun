# coding=utf-8

username = "system"
pwd = "oracle"
ip = "127.0.0.1"
tns = "oradb"

# 正式文件
save_address = "./score.txt"
# 测试文本
save_address_test = "./test.txt"

oracle_1_file = "/u01/app/oracle/product/11.2.0/dbhome_1/network/admin/listener.ora"
oracle_3_file = "/examdata/result/clear_listener_log.txt"


import os
import re
import commands


class Cat_score_1(object):
    """题目一"""

    @staticmethod
    def run():
        try:
            def isIP(str):
                p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
                if p.match(str):
                    return True
                else:
                    return False

            if os.path.exists(oracle_1_file):

                f_file_1 = open(oracle_1_file, "r")

                with open(save_address, 'w') as f:
                    if "PROTOCOL = TCP" in f_file_1.read() or "protocol = tcp" in f_file_1.read():
                        f.write("数据库网络管理课件题目一:查看监听的连接协议为TCP, ---ok\n")
                    else:
                        f.write("数据库网络管理课件题目一:查看监听的连接协议不为TCP, ---error\n")

                str_i = ""
                for i in f_file_1.readlines():
                    str_i += i.strip("\n")

                ip_str = re.search("HOST = .*\d", str_i)

                f_file_1.close()

                myStr = ip_str.group()[7:]

                if myStr == None:
                    with open(save_address, 'a+') as f:
                        f.write("数据库网络管理课件题目一:查看监听配置没有使用IP地址, ---error\n")

                else:
                    with open(save_address, 'a+') as f:
                        if isIP(myStr):
                            f.write("数据库网络管理课件题目一:查看监听配置使用IP地址为%s, ---ok\n" % myStr)
                        else:
                            f.write("数据库网络管理课件题目一:查看监听配置使用IP地址不正确为%s, ---error\n" % myStr)

            else:
                with open(save_address, 'w') as f:
                    f.write("数据库网络管理课件题目一:%s文件不存在, ---error\n" % oracle_1_file)

        except:
            print("数据库网络管理课件题目一:失败")

        else:

            print("数据库网络管理课件题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:
            cmd_1526 = "netstat -an|grep 1526|grep ESTABLISHED|wc -l"
            cmd_lsnr2 = "lsnrctl status lsnr2|grep READY|wc -l"
            com_1526 = commands.getoutput(cmd_1526)
            com_lsnr2 = commands.getoutput(cmd_lsnr2)

            with open(save_address, 'a+') as f:
                if int(com_1526) > 1:
                    f.write("数据库网络管理课件题目二:查看监听端口1526正确, ---ok\n")
                else:
                    f.write("数据库网络管理课件题目二:查看监听端口1526错误, ---error\n")

            with open(save_address, 'a+') as f:
                if com_lsnr2 > 1:
                    f.write("数据库网络管理课件题目二:查看监听lsnr2是否存在正确, ---ok\n")
                else:
                    f.write("数据库网络管理课件题目二:查看监听lsnr2是否存在错误, ---error\n")

        except:
            print("数据库网络管理课件题目二:失败")
            raise

        else:
            print("数据库网络管理课件题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:

            with open(save_address, 'a+') as f:
                if os.path.exists(oracle_3_file):
                    f.write("数据库网络管理课件题目三:文件%s存在, ---ok\n" % oracle_3_file)
                else:
                    f.write("数据库网络管理课件题目三:%s文件不存在, ---error\n" % oracle_3_file)

            cmd_host_name = "hostname"
            com_host_name = commands.getoutput(cmd_host_name)

            log_str = "/u01/app/oracle/diag/tnslsnr/" + str(com_host_name) + "/listener/trace/listener.log"

            if os.path.exists(log_str):
                com_log = commands.getoutput("du -h" + " " + log_str)

                int_str = com_log[0:4]  #  1.0K
                str_letter = int_str[-1]  #K or M

                with open(save_address, 'a+') as f:
                    if str_letter == "K":
                        if int_str.strip("K") < "1":
                            f.write("数据库网络管理课件题目三:文件大小正确，文件为：%s, ---ok\n" % int_str)
                        else:
                            f.write("数据库网络管理课件题目三:文件大小错误，文件为：%s, ---error\n" % int_str)

                    else:
                        f.write("数据库网络管理课件题目三:文件大小错误，文件为：%s, ---error\n" % int_str)
            else:
                with open(save_address, 'a+') as f:
                    f.write("数据库网络管理课件题目三:文件%s不存在, ---error\n" % log_str)

        except:
            print("数据库网络管理课件题目三:失败")

        else:
            print("数据库网络管理课件题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:
            cmd_tns = "tnsping tns_exam"

            com_tns = commands.getoutput(cmd_tns)

            with open(save_address, 'a+') as f:
                if "OK" in com_tns:
                    f.write("数据库网络管理课件题目四:tnsping tns_exam正确, ---ok\n")

                else:
                    f.write("数据库网络管理课件题目四:tnsping tns_exam错误, ---error\n")

        except:
            print("数据库网络管理课件题目四:失败")

        else:
            print("数据库网络管理课件题目四:成功")


def run():
    Cat_score_1.run()
    Cat_score_2.run()
    Cat_score_3.run()
    Cat_score_4.run()

run()



