#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目二'
save_address = "/tmp/score.txt"

test_vlu = 'grep cdrom'
test_vlu1 = '安装'


def run():
    f = open(save_address, 'w')

    # 1
    cmd = "yum repolist |grep cdrom"
    com_ret = commands.getoutput(cmd)
    if 'cdrom' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = 'yum --disablerepo=\* --enablerepo=cdrom install bind -y'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'error' in com_ret:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))

    f.close()
    print("%s:成功" % test_name)



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
