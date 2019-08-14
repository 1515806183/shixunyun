#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re

save_address = "/tmp/score.txt"
save_address_test = './test.txt'


def test_10():
    try:
        # 1
        cmd_raid0 = "cat /proc/mdstat |grep md0|grep vdb1|grep vdb2"
        com_ret_raid0 = commands.getoutput(cmd_raid0)

        with open(save_address, "w") as f:
            if "vdb2" in com_ret_raid0.lower():
                f.write("Linux磁盘存储管理题目十: 检查raid0, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十: 检查raid0, ---error\n")

        # 2
        cmd_raid1 = "cat /proc/mdstat |grep md1|grep vdb3|grep vdb4"
        com_ret_raid1 = commands.getoutput(cmd_raid1)

        with open(save_address, "a+") as f:
            if "vdb4" in com_ret_raid1.lower():
                f.write("Linux磁盘存储管理题目十: 检查raid1, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十: 检查raid1, ---error\n")

        # 3
        cmd_md0 = "df -T |grep /examdata/dir_raid0|grep '/dev/md0'|grep ext3"
        com_ret_md0 = commands.getoutput(cmd_md0)

        with open(save_address, "a+") as f:
            if "ext3" in com_ret_md0.lower():
                f.write("Linux磁盘存储管理题目十: 检查dir_raid0,ext3, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十: 检查dir_raid0, ext3, ---error\n")

        # 4
        cmd_md1 = "df -T |grep /examdata/dir_raid1|grep '/dev/md1'|grep ext3"
        com_ret_md1 = commands.getoutput(cmd_md1)

        with open(save_address, "a+") as f:
            if "ext3" in com_ret_md1.lower():
                f.write("Linux磁盘存储管理题目十: 检查dir_raid1,ext3, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十: 检查dir_raid1, ext3, ---error\n")

        # 5
        cmd_dir_raid0 = "cat /etc/fstab|egrep '/dev/md0[[:space:]]+/examdata/dir_raid0[[:space:]]+ext3'"
        com_ret_dir_raid0 = commands.getoutput(cmd_dir_raid0).lower()
        with open(save_address, "a+") as f:
            if "/dev/md0" in com_ret_dir_raid0 and "/examdata/dir_raid0" in com_ret_dir_raid0 and "ext3" in cmd_dir_raid0:
                f.write("Linux磁盘存储管理题目十: 检查/dev/md0/examdata/dir_raid0/ext3, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十: 检查/dev/md0/examdata/dir_raid0/ext3, ---error\n")

        # 6
        cmd_dir_raid1 = "cat /etc/fstab|egrep '/dev/md1[[:space:]]+/examdata/dir_raid1[[:space:]]+ext3'"
        com_ret_dir_raid1 = commands.getoutput(cmd_dir_raid1)

        with open(save_address, "a+") as f:
            if "/dev/md1" in com_ret_dir_raid1 and "/examdata/dir_raid1" in com_ret_dir_raid1 and "ext3" in com_ret_dir_raid1:
                f.write("Linux磁盘存储管理题目十: 检查/dev/md1/examdata/dir_raid1/ext3, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十: 检查/dev/md1/examdata/dir_raid1/ext3, ---error\n")

    except:
        print("Linux磁盘存储管理题目十:失败")

    else:
        print("Linux磁盘存储管理题目十:成功")

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
    test_10()
