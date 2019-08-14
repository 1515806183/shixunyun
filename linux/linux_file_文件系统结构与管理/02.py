#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/boot_bak*"


def run():
    try:
        f = open(save_address, 'w')
        cmd = "ls %s" % name
        ret = commands.getoutput(cmd)

        if ret:
            f.write("Linux文件系统结构与管理题目二:备份文件%s存在, ---ok\n" % ret)
        else:
            f.write("Linux文件系统结构与管理题目二:备份文件%s不存在, ---error\n" % ret)

    except:
        raise

    else:
        print("Linux文件系统结构与管理题目二:成功")
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
