#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "/tmp/score.txt"
file = "/examdata/result/fetch_ip"


def test_13():
    try:
        f = open(save_address, 'w')
        if os.path.exists(file):
            f.write("LINUX系统基本组成题目十三：文件%s存在, ---ok\n" % file)

            cmd = "ifconfig eth0 |awk -F '[ :]+' 'NR==2 {print $4}'"
            ret = commands.getoutput(cmd)
            cmd_cat = "ifconfig eth0 |awk -F '[ :]+' 'NR==2 {print $4}'"
            ret_cat = commands.getoutput(cmd_cat)

            if ret in ret_cat:
                f.write("LINUX系统基本组成题目十三：检查显示几项为开启的, ---ok\n'")
            else:
                f.write("LINUX系统基本组成题目十三：检查显示几项有不开启的, ---error\n'")

        else:
            f.write("LINUX系统基本组成题目十三:文件%s不存在, ---error\n" % file)
            f.write("LINUX系统基本组成题目十三:文件%s不存在,无法进行过滤对比 ---error\n" % file)

    except:
        raise

    else:
        print("LINUX系统基本组成题目十三:成功")
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
    test_13()
