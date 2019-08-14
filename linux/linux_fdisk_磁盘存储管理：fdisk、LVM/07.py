#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'


def test_07():
    try:
        cmd_df = "df -T | grep ext3 | grep '/test'"
        com_ret_df = commands.getoutput(cmd_df)

        with open(save_address, "w") as f:
            if "test" in com_ret_df:
                f.write("Linux磁盘存储管理题目七：过滤出信息test, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目七：没有过滤出信息test, ---error\n")

    except:
        print("Linux磁盘存储管理题目七:失败")

    else:
        print("Linux磁盘存储管理题目七:成功")

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
    test_07()
