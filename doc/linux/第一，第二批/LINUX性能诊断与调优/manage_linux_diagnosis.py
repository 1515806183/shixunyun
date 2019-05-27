# coding=utf-8

import commands
import os


# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/vmstat.txt"
linux_txt_2 = "/examdata/result/top.txt"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux性能诊断与调优题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_num = "cat /examdata/result/vmstat.txt|wc -l"
                com_ret_num = commands.getoutput(cmd_num)

                cmd_NF = "cat /examdata/result/vmstat.txt|grep free|awk ' {print $3,$NF}'"
                com_ret_NF = commands.getoutput(cmd_NF)

                with open(save_address, "a+") as f:
                    if "12" in com_ret_num:
                        f.write("Linux性能诊断与调优题目一：输出结果为数字12, ---ok\n")
                    else:
                        f.write("Linux性能诊断与调优题目一：输出结果不为数字12, ---error\n")

                    if "swpd st" in com_ret_NF:
                        f.write("Linux性能诊断与调优题目一：输出为swpd st, ---ok\n")
                    else:
                        f.write("Linux性能诊断与调优题目一：输出不为swpd st, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux性能诊断与调优题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux性能诊断与调优题目一:失败")

        else:
            print("Linux性能诊断与调优题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_2):
                with open(save_address, "a+") as f:
                    f.write("Linux性能诊断与调优题目二：文件%s存在, ---ok\n" % linux_txt_2)

                cmd_cat_4 = "cat /examdata/result/top.txt| egrep '(20|new\spriority\s10)' --color=auto"
                com_ret_cat_4 = commands.getoutput(cmd_cat_4)

                with open(save_address, "a+") as f:
                    if "20: old priority 0, new priority 10" in com_ret_cat_4:
                        f.write("Linux性能诊断与调优题目二：查看pid为20的进程，将该进程的优先级调整为10成功, ---ok\n")
                    else:
                        f.write("Linux性能诊断与调优题目二：查看pid为20的进程，将该进程的优先级调整为10失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux性能诊断与调优题目二：文件%s不存在, ---error\n" % linux_txt_2)

        except:
            print("Linux性能诊断与调优题目二:失败")

        else:
            print("Linux性能诊断与调优题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:

            cmd_cat = "cat /etc/security/limits.conf|egrep '(\*\s+-\s+nofile\s+65535)'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if '65535' in com_ret_cat:
                    f.write("Linux性能诊断与调优题目三：描述符为65535正确, ---ok\n")
                else:
                    f.write("Linux性能诊断与调优题目三：描述符为65535不正确, ---error\n")


        except:
            print("Linux性能诊断与调优题目三:失败")

        else:
            print("Linux性能诊断与调优题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            cmd_num = "cat /proc/sys/net/core/somaxconn"
            com_ret_num = commands.getoutput(cmd_num)

            cmd_cat = "cat /etc/sysctl.conf|egrep '(net.core.somaxconn\s+=\s+1024)'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if "1024" in com_ret_num:
                    f.write("Linux性能诊断与调优题目四：输出为1024正确, ---ok\n")
                else:
                    f.write("Linux性能诊断与调优题目四：输出为1024不正确, ---error\n")

                if "1024" in com_ret_cat:
                    f.write("Linux性能诊断与调优题目四：过滤正确, ---ok\n")
                else:
                    f.write("Linux性能诊断与调优题目四：过滤不正确, ---error\n")

        except:
            print("Linux性能诊断与调优题目四:失败")

        else:
            print("Linux性能诊断与调优题目四:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()

run()

