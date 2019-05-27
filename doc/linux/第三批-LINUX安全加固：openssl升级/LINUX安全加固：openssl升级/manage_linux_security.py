# coding=utf-8

import commands
import os


# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/soft.iso/openssl-1.0.2k.tar.gz"
linux_txt_2 = "/ssh_version.txt"
linux_txt_3 = "/examdata/result/check_file_modify"
linux_txt_102 = "/home/test2/fstab"
linux_txt_102_1 = "/examdata/result/get_ftp_file.log"


class Cat_score_97(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux安全加固题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_grep = "openssl version | grep 1.0.2k"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if '1.0.2k' in com_ret:
                        f.write("Linux安全加固题目一：grep 1.0.2k成功, ---ok\n")
                    else:
                        f.write("Linux安全加固题目一：grep 1.0.2k失败, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux安全加固题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux安全加固题目一:失败")

        else:
            print("Linux安全加固题目一:成功")


class Cat_score_98(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_2):
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目二：文件%s存在, ---ok\n" % linux_txt_2)

                cmd_grep = "cat /ssh_version.txt |grep OpenSSH_5.3p1"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if 'OpenSSH_5.3p1' in com_ret:
                        f.write("Linux安全加固题目二：grep OpenSSH_5.3p1成功, ---ok\n")
                    else:
                        f.write("Linux安全加固题目二：grep OpenSSH_5.3p1失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目二：文件%s不存在, ---error\n" % linux_txt_2)

        except:
            print("Linux安全加固题目二:失败")

        else:
            print("Linux安全加固题目二:成功")


class Cat_score_99(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_3):
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目三：文件%s存在, ---ok\n" % linux_txt_3)

                cmd_grep = "cat /examdata/result/check_file_modify | grep 'af_unix.conf: FAILED'"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if 'af_unix.conf: FAILED' in com_ret:
                        f.write("Linux安全加固题目三：grep af_unix.conf: FAILED成功, ---ok\n")
                    else:
                        f.write("Linux安全加固题目三：grep af_unix.conf: FAILED失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目三：文件%s不存在, ---error\n" % linux_txt_3)

        except:
            print("Linux安全加固题目三:失败")

        else:
            print("Linux安全加固题目三:成功")


class Cat_score_100(object):

    @staticmethod
    def run():
        try:

            cmd_grep = "sysctl -p|grep 'net.ipv4.tcp_syncookies = 1'"
            com_ret = commands.getoutput(cmd_grep)
            with open(save_address, "a+") as f:
                if 'error' not in com_ret and 'net.ipv4.tcp_syncookies = 1' in com_ret:
                    f.write("Linux安全加固题目四：grep net.ipv4.tcp_syncookies = 1成功, ---ok\n")
                else:
                    f.write("Linux安全加固题目四：grep net.ipv4.tcp_syncookies = 1失败, ---error\n")

        except:
            print("Linux安全加固题目四:失败")

        else:
            print("Linux安全加固题目四:成功")


class Cat_score_101(object):

    @staticmethod
    def run():
        try:

            cmd_grep = "cat /etc/pam.d/login|egrep '(deny=5|unlock_time=600)'"
            com_ret = commands.getoutput(cmd_grep)
            with open(save_address, "a+") as f:
                if 'deny=5' in com_ret and 'unlock_time=600' in com_ret:
                    f.write("Linux安全加固题目五：grep deny=5和unlock_time=600成功, ---ok\n")
                else:
                    f.write("Linux安全加固题目五：grep deny=5和unlock_time=600失败, ---error\n")

        except:
            print("Linux安全加固题目五:失败")

        else:
            print("Linux安全加固题目五:成功")


class Cat_score_102(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_102):
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目六：文件%s存在, ---ok\n" % linux_txt_102)

                cmd_diff = "diff /etc/fstab /home/test2/fstab"
                com_ret_diff = commands.getoutput(cmd_diff)

                with open(save_address, 'a+') as f:
                    if com_ret_diff == '':
                        f.write("Linux安全加固题目六：/etc/fstab /home/test2/fstab比较两文件是一致, ---ok\n")
                    else:
                        f.write("Linux安全加固题目六：/etc/fstab /home/test2/fstab比较两文件不是一致, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目六：文件%s不存在, ---error\n" % linux_txt_102)

            if os.path.exists(linux_txt_102_1):
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目六：文件%s存在, ---ok\n" % linux_txt_102_1)

                cmd_cat = "cat /examdata/result/get_ftp_file.log|grep 'remote:\s/etc/fstab'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, 'a+') as f:
                    if 'remote:' in com_ret_cat and 'com_ret_cat' in com_ret_cat:
                        f.write("Linux安全加固题目六：grep remote: /etc/fstab成功, ---ok\n")
                    else:
                        f.write("Linux安全加固题目六：grep remote: /etc/fstab失败, ---error\n")

                cmd_cat = "cat /examdata/result/get_ftp_file.log |grep 'received\sin' --color=auto"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, 'a+') as f:
                    if 'received' in com_ret_cat and 'in' in com_ret_cat:
                        f.write("Linux安全加固题目六：grep received in成功, ---ok\n")
                    else:
                        f.write("Linux安全加固题目六：grep received in失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux安全加固题目六：文件%s不存在, ---error\n" % linux_txt_102_1)

        except:
            print("Linux安全加固题目六:失败")

        else:
            print("Linux安全加固题目六:成功")


def run():
    Cat_score_97().run()
    Cat_score_98().run()
    Cat_score_99().run()
    Cat_score_100().run()
    Cat_score_101().run()
    Cat_score_102().run()


run()

