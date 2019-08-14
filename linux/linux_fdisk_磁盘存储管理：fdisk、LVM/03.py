#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'

linux_txt_3_1 = "/examdata/result/lvm_config_file"
linux_txt_3_2 = "/etc/lvm/lvm.conf"


def test_03():
    try:
        if os.path.exists(linux_txt_3_1):
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目三：文件%s存在, ---ok\n" % linux_txt_3_1)

            if os.path.exists(linux_txt_3_2):
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目三：文件%s存在, ---ok\n" % linux_txt_3_2)

                cmd_diff = "diff %s %s" % (linux_txt_3_1, linux_txt_3_2)
                com_ret_diff = commands.getoutput(cmd_diff)

                with open(save_address, "a+") as f:
                    if com_ret_diff == "":
                        f.write("Linux磁盘存储管理题目三：备份lvm配置文件内容一致, ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目三：备份lvm配置文件内容不一致, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目三：文件%s不存在, ---error\n" % linux_txt_3_2)

        else:
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目三：文件%s不存在, ---error\n" % linux_txt_3_1)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目三：文件%s不存在, 无法进行备份lvm配置文件内容进行比较 ---error\n" % linux_txt_3_1)

    except:
        print("操作LINUX安装与配置题目三:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目三:成功")

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
    test_03()
