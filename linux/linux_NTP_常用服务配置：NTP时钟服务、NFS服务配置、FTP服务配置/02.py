#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands
import os, re
save_address = "/tmp/score.txt"
# 测试文件
save_address_test = './test.txt'
linux_txt_2 = "/examdata/result/date.txt"


def run():
    try:
        cmd_data = "date"
        com_ret_data_now = commands.getoutput(cmd_data)
        com_ret_data = re.findall(r'\d+', com_ret_data_now)[:-1]

        cmd_hwclock = "hwclock"
        com_ret_hwclock_now = commands.getoutput(cmd_hwclock)
        com_ret_hwclock = re.findall(r'\d+', com_ret_hwclock_now)[:-3]

        with open(save_address, "w") as f:
            if com_ret_data == com_ret_hwclock:
                f.write("Linux常用服务配置题目二：时间是同步的, ---ok\n")
            else:
                f.write("Linux常用服务配置题目二：时间是不同步的, ---error\n")

        if os.path.exists(linux_txt_2):
            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目二：文件%s存在, ---ok\n" % linux_txt_2)

            cmd_cat = "cat /examdata/result/date.txt"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if com_ret_data_now in com_ret_cat or com_ret_hwclock_now in com_ret_cat:
                    f.write("Linux常用服务配置题目二：输出一致, ---ok\n")
                else:
                    f.write("Linux常用服务配置题目二：输出不一致, ---error\n")

        else:
            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目二：文件%s不存在, ---error\n" % linux_txt_2)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目二：文件%s不存在,无法进行时间比较 ---error\n" % linux_txt_2)

    except:
        print("Linux常用服务配置题目二:\033[0;34m失败\033[0m")

    else:
        print("Linux常用服务配置题目二:成功")



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
