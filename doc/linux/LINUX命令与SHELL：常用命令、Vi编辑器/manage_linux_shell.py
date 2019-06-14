# coding=utf-8

import commands
import os


# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1_1 = "/examdata/result/file_check.sh"
linux_txt_1_2 = "/examdata/result/logical"
linux_txt_2_1 = "/examdata/result/ping_01.sh"
linux_txt_2_2 = "/examdata/result/ping_log"
linux_txt_3 = "/examdata/result/adduser_01.sh"
linux_txt_3_1 = "/examdata/result/adduser_01.sh"
linux_txt_4 = "/examdata/result/function.sh"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_1_1):
                with open(save_address, "w") as f:
                    f.write("Linux命令与SHELL题目一：文件%s存在, ---ok\n" % linux_txt_1_1)

                com_ret = os.popen("sh /examdata/result/file_check.sh")
                com_ret_readlines = com_ret.readlines()

                with open(save_address, "a+") as f:

                    if "logical" in com_ret_readlines[0]:
                        f.write("Linux命令与SHELL题目一：运行%s成功, ---ok\n" % linux_txt_1_1)
                    else:
                        f.write("Linux命令与SHELL题目一：运行%s失败, ---error\n" % linux_txt_1_1)

            else:
                with open(save_address, "w") as f:
                    f.write("Linux命令与SHELL题目一：文件%s不存在, ---error\n" % linux_txt_1_1)

            if os.path.exists(linux_txt_1_2):
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目一：文件%s存在, ---ok\n" % linux_txt_1_2)

                cmd_file = "file /examdata/result/logical | grep empty"
                com_ret_file = commands.getoutput(cmd_file)

                with open(save_address, "a+") as f:
                    if com_ret_file in "":
                        f.write("Linux命令与SHELL题目一： grep empty,不能过滤到, ---error\n")
                    else:
                        f.write("Linux命令与SHELL题目一： grep empty,能过滤到, ---ok\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目一：文件%s不存在, ---error\n" % linux_txt_1_2)

        except:
            print("Linux命令与SHELL题目一:失败")
            raise

        else:
            print("Linux命令与SHELL题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_2_1):
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目二：文件%s存在, ---ok\n" % linux_txt_2_1)

                cmd_cat = "cat /examdata/result/ping_01.sh|grep '192.168.31.'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:

                    if "192.168.31." in com_ret_cat:
                        f.write("Linux命令与SHELL题目二：192.168.31.在文件中, ---ok\n")

                    else:
                        f.write("Linux命令与SHELL题目二：192.168.31.不在文件中, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目二：文件%s不存在, ---error\n" % linux_txt_2_1)

            if os.path.exists(linux_txt_2_2):
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目二：文件%s存在, ---ok\n" % linux_txt_2_2)

                cmd_cat = "cat /examdata/result/ping_log | grep '100%\spacket\sloss' --color=auto"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "100% packet loss" in com_ret_cat:
                        f.write("Linux命令与SHELL题目二：100% packet loss过滤成功, ---ok\n")

                    else:
                        f.write("Linux命令与SHELL题目二：100% packet loss过滤失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目二：文件%s不存在, ---error\n" % linux_txt_2_2)

        except:
            print("Linux命令与SHELL题目二:失败")

        else:
            print("Linux命令与SHELL题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_3):
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目三：文件%s存在, ---ok\n" % linux_txt_3)

                cmd_for = "for i in user{09..16};do id $i;done"
                com_ret_for = commands.getoutput(cmd_for)

                with open(save_address, "a+") as f:

                    if "No such user" in com_ret_for:
                        f.write("Linux命令与SHELL题目三：创建用户失败, ---error\n")

                    else:
                        f.write("Linux命令与SHELL题目三：创建用户成功, ---ok\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目三：文件%s不存在, ---error\n" % linux_txt_3)

            if os.path.exists(linux_txt_3_1):
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目三：文件%s存在, ---ok\n" % linux_txt_3_1)

                cmd_for = "egrep 'passwd\s+--stdin' /examdata/result/adduser_01.sh"
                com_ret_for = commands.getoutput(cmd_for)

                with open(save_address, "a+") as f:

                    if "" not in com_ret_for:
                        f.write("Linux命令与SHELL题目三：过滤成功, ---ok\n")

                    else:
                        f.write("Linux命令与SHELL题目三：过滤失败, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目三：文件%s不存在, ---error\n" % linux_txt_3_1)

        except:
            print("Linux命令与SHELL题目三:失败")

        else:
            print("Linux命令与SHELL题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_4):
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目四：文件%s存在, ---ok\n" % linux_txt_4)

                cmd_egrep = "egrep .*\(\) /examdata/result/function.sh"
                com_ret_egrep = commands.getoutput(cmd_egrep)

                with open(save_address, "a+") as f:
                    if com_ret_egrep != '':
                        f.write("Linux命令与SHELL题目四：grep成功, ---ok\n")
                    else:
                        f.write("Linux命令与SHELL题目四：grep失败, ---error\n")

                cmd_cat = "cat  /examdata/result/function.sh|egrep '(\$1|\$2)'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "$1" in com_ret_cat and "$2" in com_ret_cat:
                        f.write("Linux命令与SHELL题目四：过滤$1,$2成功, ---ok\n")
                    else:
                        f.write("Linux命令与SHELL题目四：过滤$1,$2失败, ---error\n")

                cmd_cat = "cat  /examdata/result/function.sh|egrep  '(51|52)'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "51" in com_ret_cat and "52" in com_ret_cat:
                        f.write("Linux命令与SHELL题目四：过滤51,52成功, ---ok\n")
                    else:
                        f.write("Linux命令与SHELL题目四：过滤51,52失败, ---error\n")

                cmd_cat = "cat /examdta/result/file_check.sh|grep 'return'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if 'return' in com_ret_cat:
                        f.write("Linux命令与SHELL题目四：过滤return成功, ---ok\n")
                    else:
                        f.write("Linux命令与SHELL题目四：过滤return失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux命令与SHELL题目四：文件%s不存在, ---error\n" % linux_txt_4)


        except:
            print("Linux命令与SHELL题目四:失败")

        else:
            print("Linux命令与SHELL题目四:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()

run()





