# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name_1 = "/examdata/result/"
name_2 = "/etc/ssh/"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_1 = "ls %s | grep jichu06_conf.bak" % name_1
        com_1 = commands.getoutput(cmd_1)
        if com_1:
            f.write("LINUX系统基本组成题目七：存在备份文件%s%s, ---ok\n" % (name_1, com_1))
            # 1.1"
            cmd_1 = "diff %sjichu06_conf %s%s" % (name_1, name_1, com_1)
            com = commands.getoutput(cmd_1)
            if com == "":
                f.write("LINUX系统基本组成题目七：备份文件%s%s内容一致, ---ok\n" % (name_1, com_1))
            else:
                f.write("LINUX系统基本组成题目七：备份文件%s%s内容不一致, ---error\n" % (name_1, com_1))
        else:
            f.write("LINUX系统基本组成题目七：%s%s不存在备份文件, ---error\n" % (name_1, com_1))
            f.write("LINUX系统基本组成题目七：%s%s不存在备份文件,无法查看内容是否一致 ---error\n" % (name_1, com_1))

        # 2
        cmd_2 = "ls %s | grep sshd_config.bak" % name_2
        com_2 = commands.getoutput(cmd_2)
        if com_2:
            f.write("LINUX系统基本组成题目七：存在备份文件%s%s, ---ok\n" % (name_2, com_2))
            # 1.1"
            cmd_1 = "diff %ssshd_config %s%s" % (name_2, name_2, com_2)
            com = commands.getoutput(cmd_1)
            if com == "":
                f.write("LINUX系统基本组成题目七：备份文件%s%s内容一致, ---ok\n" % (name_2, com_2))
            else:
                f.write("LINUX系统基本组成题目七：备份文件%s%s内容不一致, ---error\n" % (name_2, com_2))
        else:
            f.write("LINUX系统基本组成题目七：%s%s不存在备份文件, ---error\n" % (name_2, com_2))
            f.write("LINUX系统基本组成题目七：%s%s不存在备份文件,无法查看内容是否一致 ---error\n" % (name_1, com_2))

    except:
        print("LINUX系统基本组成题目七:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目七:成功")
        f.close()


if __name__ == '__main__':
    run()