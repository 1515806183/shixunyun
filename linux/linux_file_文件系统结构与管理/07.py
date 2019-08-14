#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
name = "/examdata/result/partation_table"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目七：文件%s存在, ---ok\n" % name)

            cmd_find = "file /examdata/result/partation_table |grep startsector"
            com_ret_find = commands.getoutput(cmd_find).lower()

            if "startsector" in com_ret_find:
                f.write("Linux文件系统结构与管理题目七：过滤出startsector, ---ok\n")
            else:
                f.write("Linux文件系统结构与管理题目七：没有过滤出startsector, ---error\n")


        else:
            f.write("Linux文件系统结构与管理题目七:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目七:文件%s不存在,无法过滤对比 ---error\n" % name)

    except:
        raise

    else:
        print("Linux文件系统结构与管理题目七:成功")
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
