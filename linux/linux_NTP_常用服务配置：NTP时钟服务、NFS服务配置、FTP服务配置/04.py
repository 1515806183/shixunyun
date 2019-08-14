#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands
import os, re
save_address = "/tmp/score.txt"
# 测试文件
save_address_test = './test.txt'
linux_txt_4 = "/examdata/result/future_day"


def run():
    try:
        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目四：文件%s存在, ---ok\n" % linux_txt_4)

            cmd_data = 'date +%F -d "+20 days" '
            com_ret_data_now = commands.getoutput(cmd_data)

            cmd_cat_txt = "cat %s" % linux_txt_4
            com_ret_cat = commands.getoutput(cmd_cat_txt)

            with open(save_address, "a+") as f:
                if com_ret_data_now in com_ret_cat:
                    f.write("Linux常用服务配置题目四：跟文件%s,输出一致, ---ok\n" % linux_txt_4)
                else:
                    f.write("Linux常用服务配置题目四：跟文件%s,输出不一致, ---error\n" % linux_txt_4)

        else:
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目四：文件%s不存在, ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目四：文件%s不存在,无法进行输出比较 ---error\n" % linux_txt_4)

    except:
        raise

    else:
        print("Linux常用服务配置题目四:成功")



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
