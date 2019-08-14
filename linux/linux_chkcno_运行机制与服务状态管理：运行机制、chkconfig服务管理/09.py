#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目九'
save_address = "/tmp/score.txt"
test_vlu = "过滤vsftpd"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "netstat -tulnp|grep vsftpd|grep '21'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    cmd_1 = "netstat -tulnp|grep vsftpd|grep '9999'"
    com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
    if com_ret and com_ret_1:
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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score


if __name__ == '__main__':
    run()
