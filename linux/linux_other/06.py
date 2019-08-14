#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目六'
save_address = "/tmp/score.txt"

test_vlu = 'grep php-5.3'
test_vlu1 = 'grep compat-glibc'


def run():
    f = open(save_address, 'w')
    # 1
    cmd = 'rpm -qa | grep php-5.3'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'compat-glibc' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = 'rpm -qa |grep compat-glibc'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'compat-glibc' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

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
    run()
