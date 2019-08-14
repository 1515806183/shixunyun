#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_1 = '/examdata/result/auto_shutdown.txt'


def test_01():
    try:
        if os.path.exists(linux_txt_1):
            with open(save_address, "w") as f:
                f.write("LINUX系统基本组成题目一：文件%s存在, ---ok\n" % linux_txt_1)

            cmd_grep = "cat %s" % linux_txt_1
            com_ret_grep = commands.getoutput(cmd_grep).lower()

            with open(save_address, "a+") as f:
                if "1:30" in com_ret_grep and "/sbin/shutdown -h now" in com_ret_grep:
                    f.write("LINUX系统基本组成题目一：查看系统关机日志成功, ---ok\n")
                else:
                    f.write("LINUX系统基本组成题目一：查看系统关机日志失败, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("LINUX系统基本组成题目一：文件%s不存在, ---error\n" % linux_txt_1)

            with open(save_address, "a+") as f:
                f.write("LINUX系统基本组成题目一：文件%s不存在,无法查看系统关机日志 ---error\n" % linux_txt_1)

    except:
        print("LINUX系统基本组成题目一:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目一:成功")

    with open(save_address) as f :
        num = f.readlines()

    # 总题目数
    sum = len(num)
    # 一题多少分
    average = 100 // sum

    # 正确的题目总数
    timu_all = 0
    for i in num:
        if '---ok' in i:
                timu_all += 1
    total_score = timu_all * average

    print total_score


test_01()
