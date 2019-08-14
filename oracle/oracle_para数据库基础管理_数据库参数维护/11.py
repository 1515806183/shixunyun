#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, cx_Oracle
test_name = '数据库参数维护课件题目十一'
save_address = "/tmp/score.txt"
name = "/examdata/result/query_date_format.log"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "127.0.0.1"
tns = "oradb"
port = 1521


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if "alter session set nls_date_format='YYYY-MM-DD'".lower().replace(" ", "") in com_ret:
            f.write("%s:查看文件%s 存在以下关键信息正确 ---ok\n" % (test_name, name))
        else:
            f.write("%s:查看文件%s 存在以下关键信息错误 ---error\n" % (test_name, name))
    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s 无法查看关键信息 ---error\n" % (test_name, name))

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
