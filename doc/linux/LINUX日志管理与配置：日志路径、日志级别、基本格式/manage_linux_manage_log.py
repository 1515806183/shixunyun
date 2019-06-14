# coding=utf-8

import commands
import os

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/default_log_dir_and_filename"
linux_txt_2 = "/examdata/result/rsyslog_log_level"
linux_txt_4 = "/examdata/result/log_format"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux日志管理与配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_egrep = "cat /examdata/result/default_log_dir_and_filename | grep '/var/log/messages'"
                com_ret_egrep = commands.getoutput(cmd_egrep)

                with open(save_address, "a+") as f:
                    if com_ret_egrep == "":
                        f.write("Linux日志管理与配置题目一：没有查询到/var/log/messages, ---error\n")

                    else:
                        f.write("Linux日志管理与配置题目一：查询到/var/log/messages, ---ok\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux日志管理与配置题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux日志管理与配置题目一:失败")

        else:
            print("Linux日志管理与配置题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_2):
                with open(save_address, "a+") as f:
                    f.write("Linux日志管理与配置题目二：文件%s存在, ---ok\n" % linux_txt_2)

                cmd_egrep = "egrep '^*\.\*' /etc/rsyslog.conf|egrep -v '@|#'"
                com_ret_egrep = commands.getoutput(cmd_egrep)

                cmd_cat = "cat /examdata/result/rsyslog_log_level"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if com_ret_egrep in com_ret_cat:
                        f.write("Linux日志管理与配置题目二：输出一致, ---ok\n")
                    else:
                        with open(save_address, "a+") as f:
                            f.write("Linux日志管理与配置题目二：输出不一致, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux日志管理与配置题目二：文件%s不存在, ---error\n" % linux_txt_2)

        except:
            print("Linux日志管理与配置题目二:失败")

        else:
            print("Linux日志管理与配置题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:

            cmd_egrep = "egrep '^mail.*[[:space:]]+-/examdata/result/mail.log' /etc/rsyslog.conf"
            com_ret_egrep = commands.getoutput(cmd_egrep)

            with open(save_address, "a+") as f:
                if com_ret_egrep == "":
                    f.write("Linux日志管理与配置题目三：修改 mail.*级别日志失败, ---error\n")

                else:
                    f.write("Linux日志管理与配置题目三：修改 mail.*级别日志成功, ---ok\n")

        except:
            print("Linux日志管理与配置题目三:失败")

        else:
            print("Linux日志管理与配置题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_4):
                with open(save_address, "a+") as f:
                    f.write("Linux日志管理与配置题目四：文件%s存在, ---ok\n" % linux_txt_4)

                cmd_cat = "cat /examdata/result/log_format|wc -l"
                com_ret_cat = commands.getoutput(cmd_cat)

                cmd_head = "head -n 1 /examdata/result/log_format |grep '[0-9]\{4\}/[0-9]\{2\}/[0-9]\{2\}\s[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}'"
                com_ret_head = commands.getoutput(cmd_head)

                with open(save_address, "a+") as f:
                    if int(com_ret_cat) > 1:
                        f.write("Linux日志管理与配置题目四：查看大约一行, ---ok\n")

                    else:
                        f.write("Linux日志管理与配置题目四：查看小于一行, ---error\n")

                with open(save_address, "a+") as f:
                    if com_ret_head == "":
                        f.write("Linux日志管理与配置题目四：格式输出当前时间失败, ---error\n")

                    else:
                        f.write("Linux日志管理与配置题目四：格式输出当前时间成功, ---ok\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux日志管理与配置题目四：文件%s不存在, ---error\n" % linux_txt_4)

        except:
            print("Linux日志管理与配置题目四:失败")

        else:
            print("Linux日志管理与配置题目四:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()


run()