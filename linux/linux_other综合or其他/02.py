#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目二'
save_address = "/tmp/score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "curl http://rhel65-training01.example.com"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "csg linux training".lower().replace(" ", "") in com_ret and "Couldn".lower().replace(" ", "") not in com_ret:
        f.write("%s:输出csg linux training正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出csg linux training错误 ---error\n" % test_name)

    # 2
    cmd = "curl http://www.example.com"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "example.com".lower().replace(" ", "") in com_ret and "Couldn".lower().replace(" ", "") not in com_ret:
        f.write("%s:输出http://www.example.com正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出http://www.example.com错误 ---error\n" % test_name)

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
