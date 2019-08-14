#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_1 = "/examdata/result/apache_install_log"


def run():
    try:
        cmd_chkconfig = "chkconfig --list httpd| grep '3:启用'"
        com_ret_chkconfig = commands.getoutput(cmd_chkconfig)

        with open(save_address, "w") as f:
            if "3:启用" in com_ret_chkconfig:
                f.write("Linux软件安装与配置题目二：设置httpd开机启动成功, ---ok\n")

            else:
                f.write("Linux软件安装与配置题目二：设置httpd开机启动失败, ---error\n")

    except:
        print("Linux软件安装与配置题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目二:成功")



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
