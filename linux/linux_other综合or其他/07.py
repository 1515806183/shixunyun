#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目七'
save_address = "/tmp/score.txt"
test_vlu = "查询extundelete版本"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "extundelete -v"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'extundelete version 0.2.4'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

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
