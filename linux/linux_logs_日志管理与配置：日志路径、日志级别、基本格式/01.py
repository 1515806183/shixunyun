# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_1 = "/examdata/result/default_log_dir_and_filename"


def test_01():
    try:
        if os.path.exists(linux_txt_1):
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

            cmd_egrep = "cat %s | grep '/var/log/messages'" % linux_txt_1
            com_ret_egrep = commands.getoutput(cmd_egrep)
            with open(save_address, "a+") as f:
                if com_ret_egrep == "":
                    f.write("Linux日志管理与配置题目一：没有查询到/var/log/messages, ---error\n")
                else:
                    f.write("Linux日志管理与配置题目一：查询到/var/log/messages, ---ok\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目一：文件%s不存在, ---error\n" % linux_txt_1)
            with open(save_address, "a+") as f:
                f.write("Linux日志管理与配置题目一：文件%s不存在, 无法查询到/var/log/messages---error\n" % linux_txt_1)
    except:
        print("Linux日志管理与配置题目一:\033[0;34m失败\033[0m")
        raise
    else:
        print("Linux日志管理与配置题目一:成功")


if __name__ == '__main__':
    test_01()