#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux磁盘存储管理题目六'
save_address = "/tmp/score.txt"

test_vlu = "执行命令，结果"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "df -hT /|sed 's/[GgMm]//g' | awk 'NR>1{print $3}'"
    com_ret = int(commands.getoutput(cmd).lower().replace(" ", ""))

    if com_ret == 16:
        f.write("%s:%s %s 正确 ---ok\n" % (test_name, test_vlu, com_ret))
    else:
        f.write("%s:%s %s 错误 ---error\n" % (test_name, test_vlu, com_ret))

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
