#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_6 = "/examdata/result/rpmbuild_package_install.log"


def run():
    try:
        # 1
        cmd_rpm = "rpm -qa|grep e2fsprogs|wc -l"
        com_ret_rpm = int(commands.getoutput(cmd_rpm))
        with open(save_address, "w") as f:
            if com_ret_rpm == 3:
                f.write("Linux软件安装与配置题目八：结果输出为:%s 为3, ---ok\n" % com_ret_rpm)
            else:
                f.write("Linux软件安装与配置题目八：结果输出:%s 不为3, ---error\n"  % com_ret_rpm)

        # 2
        cmd_help = "extundelete --help"
        com_ret_help = commands.getoutput(cmd_help)
        with open(save_address, "a+") as f:
            if "command not found" in com_ret_help:
                f.write("Linux软件安装与配置题目八：extundelete 无帮助信息输出, ---error\n")
            else:
                f.write("Linux软件安装与配置题目八：extundelete 有帮助信息输出, ---ok\n")
    except:
        print("Linux软件安装与配置题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目八:成功")



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
