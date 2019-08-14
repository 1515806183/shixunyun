#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目一'
save_address = "/tmp/score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "ps -ef|grep rpcbind|grep -v grep"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if com_ret:
        f.write("%s:输出正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出错误 ---error\n" % test_name)

    # 2
    cmd = "ps -ef|grep nfs|grep -v grep | wc -l"
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret > 0:
        f.write("%s:ps输出正确 ---ok\n" % test_name)
    else:
        f.write("%s:ps输出错误 ---error\n" % test_name)

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
