#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/etc_size"


def test_01():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目一：文件%s存在, ---ok\n" % name)
            cmd = "du -sh /etc"
            ret = commands.getoutput(cmd)

            cmd_cat = "cat %s" % name
            ret_cat = commands.getoutput(cmd_cat)

            if ret in ret_cat:
                f.write("Linux文件系统结构与管理题目一:/etc/目录的总文件大小, ---ok\n'")
            else:
                f.write("Linux文件系统结构与管理题目一:/etc/目录的总文件大小, ---error\n'")

        else:
            f.write("Linux文件系统结构与管理题目一:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目一:文件%s不存在,无法进行过滤对比 ---error\n" % name)

    except:
        raise

    else:
        print("Linux文件系统结构与管理题目一:成功")
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
    test_01()
