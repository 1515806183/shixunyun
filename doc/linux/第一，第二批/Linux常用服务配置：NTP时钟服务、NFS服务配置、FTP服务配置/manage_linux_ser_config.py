# coding=utf-8

import commands
import os

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/date_ago.txt"
linux_txt_2 = "/examdata/result/date.txt"
linux_txt_3 = "/etc/ntp.conf"
linux_txt_4 = "/examdata/result/future_day"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux常用服务配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_txt = "date +%F -d '-100 days'"
                com_ret_txt = commands.getoutput(cmd_txt)
                cmd_cat_txt = "cat /examdata/result/date_ago.txt"
                com_ret_cat = commands.getoutput(cmd_cat_txt)

                with open(save_address, "a+") as f:
                    if com_ret_txt in com_ret_cat:
                        f.write("Linux常用服务配置题目一：输出一致, ---ok\n")

                    else:
                        f.write("Linux常用服务配置题目一：输出不一致, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux常用服务配置题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux常用服务配置题目一:失败")

        else:
            print("Linux常用服务配置题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:
            cmd_data = "date | awk '{print $4}'"
            com_ret_data = commands.getoutput(cmd_data)

            cmd_hwclock = "hwclock | awk '{print $5}'"
            com_ret_hwclock = commands.getoutput(cmd_hwclock)

            with open(save_address, "a+") as f:
                if com_ret_data == com_ret_data or (int(str(com_ret_hwclock).split(":")[2]) - int(str(com_ret_data).split(":")[2]) > 0):
                    f.write("Linux常用服务配置题目二：时间是同步的, ---ok\n")

                else:
                    f.write("Linux常用服务配置题目二：时间是不同步的, ---error\n")

            if os.path.exists(linux_txt_2):
                with open(save_address, "a+") as f:
                    f.write("Linux常用服务配置题目二：文件%s存在, ---ok\n" % linux_txt_2)

                cmd_cat = "cat /examdata/result/date.txt"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if com_ret_data in com_ret_cat and com_ret_hwclock in com_ret_cat:
                        f.write("Linux常用服务配置题目二：输出一致, ---ok\n")

                    else:
                        f.write("Linux常用服务配置题目二：输出不一致, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux常用服务配置题目二：文件%s不存在, ---error\n" % linux_txt_2)


        except:
            print("Linux常用服务配置题目二:失败")

        else:
            print("Linux常用服务配置题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_3):

                cmd_data = "egrep 'server[[:space:]]+10.10.10.12' /etc/ntp.conf"
                com_ret_data = commands.getoutput(cmd_data)

                with open(save_address, "a+") as f:
                    if com_ret_data == "":
                        f.write("Linux常用服务配置题目二：无配置, ---error\n")

                    else:
                        f.write("Linux常用服务配置题目二：有配置, ---ok\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux常用服务配置题目二：文件%s不存在, ---error\n" % linux_txt_3)

        except:
            print("Linux常用服务配置题目二:失败")

        else:
            print("Linux常用服务配置题目二:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_4):
                with open(save_address, "a+") as f:
                    f.write("Linux常用服务配置题目一：文件%s存在, ---ok\n" % linux_txt_4)

                cmd_txt = "date +%F -d '+20 days'"
                com_ret_txt = commands.getoutput(cmd_txt)
                cmd_cat_txt = "cat /examdata/result/future_day"
                com_ret_cat = commands.getoutput(cmd_cat_txt)

                with open(save_address, "a+") as f:
                    if com_ret_txt in com_ret_cat:
                        f.write("Linux常用服务配置题目一：输出一致, ---ok\n")

                    else:
                        f.write("Linux常用服务配置题目一：输出不一致, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux常用服务配置题目一：文件%s不存在, ---error\n" % linux_txt_4)


        except:
            print("Linux常用服务配置题目一:失败")

        else:
            print("Linux常用服务配置题目一:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()


run()
