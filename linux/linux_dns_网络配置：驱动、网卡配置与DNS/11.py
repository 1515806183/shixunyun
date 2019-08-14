#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_11_file = '/examdata/result/init_files'


def test_11():
    try:
        f = open(save_address, 'w')
        if os.path.exists(linux_11_file):
            f.write("LINUX系统基本组成题目十一：文件%s存在, ---ok\n" % linux_11_file)
            cmd = "ls /etc --file-type |grep -v /$|grep ^init"
            ret = commands.getoutput(cmd)

            cmd_cat = "cat %s" % linux_11_file
            ret_cat = commands.getoutput(cmd_cat)

            if ret in ret_cat:
                f.write("LINUX系统基本组成题目十一：检查对比输出正确, ---ok\n'")
            else:
                f.write("LINUX系统基本组成题目十一：检查对比输出不正确, ---error\n'")

        else:
            f.write("LINUX系统基本组成题目十一:文件%s不存在, ---error\n" % linux_11_file)
            f.write("LINUX系统基本组成题目十一:文件%s不存在,无法进行过滤对比 ---error\n" % linux_11_file)

    except:
        raise

    else:
        print("LINUX系统基本组成题目十一:成功")
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
    test_11()
