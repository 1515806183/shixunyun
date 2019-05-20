# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re

save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_11 = "/examdata/result/file_use_as_disk"


def test_11():
    try:
        # 1
        cmd_ext4 = "df -hT|grep '/examdata/result/file_use_as_disk' | grep ext4"
        com_ret_ext4 = commands.getoutput(cmd_ext4).lower()

        with open(save_address, "w") as f:
            if "ext4" in com_ret_ext4:
                f.write("Linux磁盘存储管理题目十一：grep ext4成功, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十一：grep ext4错误, ---error\n")

        # 2
        cmd_file = "file 'df | grep '/examdata/result/file_use_as_disk' | awk '{print $1}'' | grep 'huge files'"
        com_ret_file = commands.getoutput(cmd_file).lower()

        with open(save_address, "a+") as f:
            if "huge files" in com_ret_file:
                f.write("Linux磁盘存储管理题目十一：grep huge files成功, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十一：grep huge files错误, ---error\n")

        # 3
        cmd_du = "df |grep /examdata/result/file_use_as_disk | awk '{print $1}'"
        com_ret_du = commands.getoutput(cmd_du)
        cmd_du = "du -sh %s |awk '{print $1}'|sed 's/[Mm]//g'" % com_ret_du
        com_ret_du = commands.getoutput(cmd_du)
        with open(save_address, "a+") as f:
            if "100" in com_ret_du or "101" in com_ret_du:
                f.write("Linux磁盘存储管理题目十一：输出结果为:%s, ---ok\n" % com_ret_du)
            else:
                f.write("Linux磁盘存储管理题目十一：输出结果为:%s, ---error\n" % com_ret_du)

    except:
        print("Linux磁盘存储管理题目十一:失败")

    else:
        print("Linux磁盘存储管理题目十一:成功")


if __name__ == '__main__':
    test_11()