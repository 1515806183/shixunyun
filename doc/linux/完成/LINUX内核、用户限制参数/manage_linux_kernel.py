# coding=utf-8

import commands
import os


# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_110 = "/examdata/dir_raid1"
linux_txt_111 = "/examdata/result/share_mem_size"


class Cat_score_110(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_110):
                with open(save_address, "w") as f:
                    f.write("LINUX内核、用户限制参数题目一：文件%s存在, ---ok\n" % linux_txt_110)

                cmd_grep = "cat /etc/fstab |egrep '/examdata/dir_raid1\s+ext3\s+defaults,acl'"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if '/examdata/dir_raid1' in com_ret and 'ext3' in com_ret and 'defaults,acl' in com_ret:
                        f.write("LINUX内核、用户限制参数题目一：grep /examdata/dir_raid1   ext3   defaults,acl成功, ---ok\n")
                    else:
                        f.write("LINUX内核、用户限制参数题目一：grep /examdata/dir_raid1   ext3   defaults,acl失败, ---error\n")

                cmd_grep = "getfacl /examdata/dir_raid1|grep 'user:user06:---'"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if 'user:user06:---' in com_ret:
                        f.write("LINUX内核、用户限制参数题目一：grep user:user06:---成功, ---ok\n")
                    else:
                        f.write("LINUX内核、用户限制参数题目一：grep user:user06:---失败, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("LINUX内核、用户限制参数题目一：文件%s不存在, ---error\n" % linux_txt_110)

        except:
            print("LINUX内核、用户限制参数题目一:失败")

        else:
            print("LINUX内核、用户限制参数题目一:成功")


class Cat_score_111(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_111):
                with open(save_address, "a+") as f:
                    f.write("LINUX内核、用户限制参数题目二：文件%s存在, ---ok\n" % linux_txt_111)
            else:
                with open(save_address, "a+") as f:
                    f.write("LINUX内核、用户限制参数题目二：文件%s不存在, ---error\n" % linux_txt_111)

            cmd_grep = "sysctl -p 2>/dev/null|grep 'kernel.shmmax\s=\s2147483648'"
            com_ret = commands.getoutput(cmd_grep)

            with open(save_address, 'a+') as f:
                if 'kernel.shmmax' in com_ret and '2147483648' in com_ret:
                    f.write("LINUX内核、用户限制参数题目二：grep kernel.shmmax = 2147483648成功, ---ok\n")
                else:
                    f.write("LINUX内核、用户限制参数题目二：grep kernel.shmmax = 2147483648失败, ---error\n")

        except:
            print("LINUX内核、用户限制参数题目二:失败")

        else:
            print("LINUX内核、用户限制参数题目二:成功")


class Cat_score_112(object):

    @staticmethod
    def run():
        try:
            cmd_grep = "sysctl -p 2>/dev/null|grep 'net.ipv4.tcp_tw_reuse\s=\s1'"
            com_ret = commands.getoutput(cmd_grep)

            with open(save_address, 'a+') as f:
                if 'net.ipv4.tcp_tw_reuse' in com_ret and '1' in com_ret:
                    f.write("LINUX内核、用户限制参数题目三：grep net.ipv4.tcp_tw_reuse = 1成功, ---ok\n")
                else:
                    f.write("LINUX内核、用户限制参数题目三：grep net.ipv4.tcp_tw_reuse = 1失败, ---error\n")

        except:
            print("LINUX内核、用户限制参数题目三:失败")

        else:
            print("LINUX内核、用户限制参数题目三:成功")


class Cat_score_113(object):

    @staticmethod
    def run():
        try:
            cmd_grep = "sysctl -p 2>/dev/null |egrep 'net.ipv4.ip_local_port_range'"
            com_ret = commands.getoutput(cmd_grep)

            with open(save_address, 'a+') as f:
                if 'net.ipv4.ip_local_port_range' in com_ret and '1024' in com_ret:
                    f.write("LINUX内核、用户限制参数题目四：grep net.ipv4.ip_local_port_range = 1024 +65000成功, ---ok\n")
                else:
                    f.write("LINUX内核、用户限制参数题目四：grep net.ipv4.ip_local_port_range = 1024 +6500失败, ---error\n")

        except:
            print("LINUX内核、用户限制参数题目四:失败")

        else:
            print("LINUX内核、用户限制参数题目四:成功")


def run():
    Cat_score_110().run()
    Cat_score_111().run()
    Cat_score_112().run()
    Cat_score_113().run()


run()

