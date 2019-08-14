#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_cat = "cat /etc/passwd|grep hill|grep nologin"
        com_ret_cat = commands.getoutput(cmd_cat)
        if com_ret_cat == '':
            f.write("Linux目录与文件管理题目十五：没有查询到用户hill, ---error\n")
        else:
            f.write("Linux目录与文件管理题目十五：查询到用户%s, ---ok\n" % com_ret_cat)

    except:
        print("Linux目录与文件管理题目十五\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十五:成功")
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
