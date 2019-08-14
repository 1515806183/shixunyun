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
        print("Linux文件系统结构与管理题目二:\033[0;34m失败\033[0m")
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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score


if __name__ == '__main__':
    run()
