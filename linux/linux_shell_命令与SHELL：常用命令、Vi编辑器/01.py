#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_1_1 = "/examdata/result/file_check.sh"
linux_txt_1_2 = "/examdata/result/logical"


def run():
    try:
        if os.path.exists(linux_txt_1_1):
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目一：文件%s存在, ---ok\n" % linux_txt_1_1)
        else:
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目一：文件%s不存在, ---error\n" % linux_txt_1_1)

        if os.path.exists(linux_txt_1_2):
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目一：文件%s存在, ---ok\n" % linux_txt_1_2)

            cmd_file = "file %s | grep empty" % linux_txt_1_2
            com_ret_file = commands.getoutput(cmd_file).lower()

            with open(save_address, "a+") as f:
                if "empty" in com_ret_file:
                    f.write("Linux命令与SHELL题目一： grep empty, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目一： grep empty, ---error\n")
        else:
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目一：文件%s不存在, ---error\n" % linux_txt_1_2)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目一：文件%s不存在,无法进行grep empty ---error\n" % linux_txt_1_2)
    except:
        print("Linux命令与SHELL题目一:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux命令与SHELL题目一:成功")



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
