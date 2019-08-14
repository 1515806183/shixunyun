#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re

save_address = "/tmp/score.txt"
save_address_test = './test.txt'


def test_08():
    try:
        cmd_swapon = "swapon -s|grep -v dev|awk 'NR>1 {print $2}'"
        com_ret_swapon = commands.getoutput(cmd_swapon)

        with open(save_address, "w") as f:
            if "file" in com_ret_swapon.lower():
                f.write("Linux磁盘存储管理题目八：检查swap挂载过滤出信息file, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目八：检查swap挂载没有过滤出信息file, ---error\n")

        cmd_awk = "swapon -s|grep file|awk '{print $1}'"
        com_ret_awk = commands.getoutput(cmd_awk)

        cmd_du = "du -sh " + com_ret_awk
        com_ret_du = commands.getoutput(cmd_du)
        com_ret_du = re.search(r'\d+', com_ret_du).group()

        with open(save_address, "a+") as f:
            if "200" in com_ret_du or "201" in com_ret_du:
                f.write("Linux磁盘存储管理题目八：检查swap的大小输出为200或201, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目八：检查swap的大小输出不为200或201, ---error\n")

        cmd_cat = "cat /etc/fstab | egrep swap | grep -v '/dev/mapper'"
        com_ret_cat = commands.getoutput(cmd_cat)

        with open(save_address, "a+") as f:
            if com_ret_cat:
                f.write("Linux磁盘存储管理题目八：检查开机启动输出为/dev/mapper, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目八：检查开机启动输出不为/dev/mapper, ---error\n")

    except:
        print("Linux磁盘存储管理题目八:失败")

    else:
        print("Linux磁盘存储管理题目八:成功")

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
    test_08()
