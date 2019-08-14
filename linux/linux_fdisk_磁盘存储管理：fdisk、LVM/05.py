#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_5 = "/examdata/result/mountpoint_system_type"


def test_05():
    try:
        if os.path.exists(linux_txt_5):
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目五：文件%s存在, ---ok\n" % linux_txt_5)

            cmd_cat_ext4 = "cat /examdata/result/mountpoint_system_type|grep ext4"
            com_ret_cat_ext4 = commands.getoutput(cmd_cat_ext4).lower()

            cmd_cat_tmpfs = "cat /examdata/result/mountpoint_system_type|grep tmpfs"
            com_ret_cat_tmpfs = commands.getoutput(cmd_cat_tmpfs).lower()

            cmd_cat_iso = "cat /examdata/result/mountpoint_system_type|grep iso9660"
            com_ret_cat_iso = commands.getoutput(cmd_cat_iso).lower()

            with open(save_address, "a+") as f:
                if "ext4" in com_ret_cat_ext4 and "tmpfs" in com_ret_cat_tmpfs and "iso9660" in com_ret_cat_iso:
                    f.write("Linux磁盘存储管理题目五：过滤出ext4 tmpfs iso9660 , ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目五：没有过滤出ext4 tmpfs iso9660, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目五：文件%s不存在, ---error\n" % linux_txt_5)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目五：文件%s不存在,无法过滤出ext4 tmpfs iso9660 ---error\n" % linux_txt_5)

    except:
        raise

    else:
        print("操作LINUX安装与配置题目五:成功")

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
    test_05()
