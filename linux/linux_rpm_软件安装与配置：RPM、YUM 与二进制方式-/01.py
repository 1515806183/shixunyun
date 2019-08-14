#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_1 = "/examdata/result/apache_install_log"


def run():
    try:
        cmd_rpm = "rpm -qa httpd"
        com_ret_egrep = commands.getoutput(cmd_rpm)
        with open(save_address, "w") as f:
            if com_ret_egrep == "":
                f.write("Linux软件安装与配置题目一：设置httpd开机启动失败, ---error\n")
            else:
                f.write("Linux软件安装与配置题目一：设置httpd开机启动成功, ---ok\n")

        if os.path.exists(linux_txt_1):
            with open(save_address, "a+") as f:
                f.write("Linux软件安装与配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

            cmd_grep = "grep 'will be installed' %s" % linux_txt_1
            com_ret_grep = commands.getoutput(cmd_grep).lower()

            with open(save_address, "a+") as f:
                if "will be installed" in com_ret_grep:
                    f.write("Linux软件安装与配置题目一：有重定向日志, ---ok\n")
                else:
                    f.write("Linux软件安装与配置题目一：无重定向日志, ---error\n")
        else:
            with open(save_address, "a+") as f:
                f.write("Linux软件安装与配置题目一：文件%s不存在, ---error\n" % linux_txt_1)

            with open(save_address, "a+") as f:
                f.write("Linux软件安装与配置题目一：文件%s不存在,无法查询重定向 ---error\n" % linux_txt_1)

    except:
        raise

    else:
        print("Linux软件安装与配置题目一:成功")



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
