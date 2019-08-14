#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "/tmp/score.txt"


def test_12():
    try:
        f = open(save_address, 'w')
        # rsyslog、crond、network、sshd、sysstat、autofs、auditd、haldaemon、messagebus、
        cmd = "chkconfig --list | grep 3:启用 | awk '{print $1}'"
        ret = commands.getoutput(cmd).lower()
        ret_list = ret.split('\n')
        res_on = ['rsyslog', 'crond', 'network', 'sshd', 'sysstat', 'autofs', 'auditd', 'haldaemon', 'messagebus']

        set_ret_list = set(ret_list).intersection(res_on)

        if set(res_on) == set_ret_list:
            f.write("LINUX系统基本组成题目十二：检查显示几项为开启的, ---ok\n'")
        else:
            f.write("LINUX系统基本组成题目十二：检查显示几项有不开启的, ---error\n'")

    except:
        raise

    else:
        print("LINUX系统基本组成题目十二:成功")
        f.close()

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


if __name__ == '__main__':
    test_12()
