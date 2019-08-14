#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands
import os
save_address = "/tmp/score.txt"
# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/date_ago.txt"


def run():
    try:
        if os.path.exists(linux_txt_1):
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

            cmd = "date +%F -d '-100 days'"
            com_ret = commands.getoutput(cmd)
            cmd = "cat /examdata/result/date_ago.txt"
            cmd_ret_txt = commands.getoutput(cmd)

            with open(save_address, "a+") as f:
                if com_ret in cmd_ret_txt:
                    f.write("Linux常用服务配置题目一：输出一致, ---ok\n")
                else:
                    f.write("Linux常用服务配置题目一：输出不一致, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目一：文件%s不存在, ---error\n" % linux_txt_1)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目一：文件%s不存在,无法进行对比输出, ---error\n" % linux_txt_1)
    except:
        raise

    else:
        print("Linux常用服务配置题目一:成功")



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
