#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "/tmp/score.txt"
file_name = "/etc/motd"


def test_14():
    try:
        f = open(save_address, 'w')
        cmd = "cat %s" % file_name
        ret = commands.getoutput(cmd).lower().replace(' ', '')

        str_name = "hello, welcome to login linux trainning system"
        str_name = str_name.replace(' ', '')

        if str_name in ret:
            f.write("LINUX系统基本组成题目十四：文件%s存在提示信息hello, welcome to login linux  trainning system, ---ok\n" % file_name)
        else:
            f.write("LINUX系统基本组成题目十四：文件%s不存在提示信息hello, welcome to login linux  trainning system, ---error\n" % file_name)

    except:
        raise

    else:
        print("LINUX系统基本组成题目十四:成功")
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
    test_14()
