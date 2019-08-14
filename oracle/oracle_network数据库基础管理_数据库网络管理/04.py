#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = '数据库网络管理课件题目四'
test_vlu = '服务名为tns_exam'
save_address = "/tmp/score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % 'tnsping tns_exam'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ok' in com_ret:
        f.write("%s:查看%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:查看%s错误 ---error\n" % (test_name, test_vlu))
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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
