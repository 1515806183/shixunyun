# coding=utf-8

import commands
import os

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_129 = "/examdata/result/resolve_ftp_login_error"
linux_txt_130 = "/examdata/result/fix_login_prompt.txt"
linux_txt_131 = "/examdata/result/resolve_dmesg_error"


class Cat_score_129(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_129):
                with open(save_address, "w") as f:
                    f.write("LINUX故障诊断与调整题目一：文件%s存在, ---ok\n" % linux_txt_129)

                cmd_grep = "cat /examdata/result/resolve_ftp_login_error|grep 'setsebool\s-P\sftp_home_dir\son'"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if 'setsebool -P ftp_home_dir on' in com_ret:
                        f.write("LINUX故障诊断与调整题目一：grep setsebool -P ftp_home_dir on成功, ---ok\n")
                    else:
                        f.write("LINUX故障诊断与调整题目一：grep setsebool -P ftp_home_dir on失败, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("LINUX故障诊断与调整题目一：文件%s不存在, ---error\n" % linux_txt_129)

        except:
            print("LINUX故障诊断与调整题目一:失败")

        else:
            print("LINUX故障诊断与调整题目一:成功")


class Cat_score_130(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_130):
                with open(save_address, "a+") as f:
                    f.write("LINUX故障诊断与调整题目二：文件%s存在, ---ok\n" % linux_txt_130)

                cmd_grep = "cat /examdata/result/fix_login_prompt.txt|grep '/etc/skel/.bashrc'"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if '/etc/skel/.bashrc' in com_ret:
                        f.write("LINUX故障诊断与调整题目二：grep /etc/skel/.bashrc成功, ---ok\n")
                    else:
                        f.write("LINUX故障诊断与调整题目二：grep /etc/skel/.bashrc失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LINUX故障诊断与调整题目二：文件%s不存在, ---error\n" % linux_txt_130)

        except:
            print("LINUX故障诊断与调整题目二:失败")

        else:
            print("LINUX故障诊断与调整题目二:成功")


class Cat_score_131(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_131):
                with open(save_address, "a+") as f:
                    f.write("LINUX故障诊断与调整题目三：文件%s存在, ---ok\n" % linux_txt_131)

                cmd_grep = "cat /examdata/result/resolve_dmesg_error|grep 'service\siptables\sstop'"
                com_ret = commands.getoutput(cmd_grep)

                with open(save_address, 'a+') as f:
                    if 'service' in com_ret and 'iptables' in com_ret and 'stop' in com_ret:
                        f.write("LINUX故障诊断与调整题目三：grep service iptables stop成功, ---ok\n")
                    else:
                        f.write("LINUX故障诊断与调整题目三：grep service iptables stop失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LINUX故障诊断与调整题目三：文件%s不存在, ---error\n" % linux_txt_131)

        except:
            print("LINUX故障诊断与调整题目三:失败")

        else:
            print("LINUX故障诊断与调整题目三:成功")


def run():
    Cat_score_129().run()
    Cat_score_130().run()
    Cat_score_131().run()

run()

