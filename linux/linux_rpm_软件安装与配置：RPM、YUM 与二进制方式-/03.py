#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_3 = "/examdata/result/httpd_files"


def run():
    try:
        cmd_rpm = "rpm  -ql httpd"
        com_ret_egrep = commands.getoutput(cmd_rpm)

        if os.path.exists(linux_txt_3):
            with open(save_address, "w") as f:
                f.write("Linux软件安装与配置题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_cat = "cat %s" % linux_txt_3
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if com_ret_egrep in com_ret_cat:
                    f.write("Linux软件安装与配置题目三：对比输出正确, ---ok\n")

                else:
                    f.write("Linux软件安装与配置题目三：对比输出错误, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("LinuxLinux软件安装与配置题目三：文件%s不存在, ---error\n" % linux_txt_3)

            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目三：文件%s不存在,无法进行对比输出 ---error\n" % linux_txt_3)


    except:
        raise

    else:
        print("Linux软件安装与配置题目三:成功")



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
