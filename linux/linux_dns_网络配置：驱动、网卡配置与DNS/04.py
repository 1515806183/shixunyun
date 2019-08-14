#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_4 = "/examdata/result/find_var.txt"


def test_04():
    try:
        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("LINUX系统基本组成题目四：文件%s存在, ---ok\n" % linux_txt_4)

            cmd_check = "find /var ! -atime -90 > ./check_atime.txt"
            commands.getoutput(cmd_check)

            # 比较两个文件内容
            cmd_num_file = "cat ./check_atime.txt|wc -l"
            cmd_num_server = "cat %s|wc -l" % linux_txt_4

            cmd_num_ret = int(commands.getoutput(cmd_num_file))
            cmd_server_ret = int(commands.getoutput(cmd_num_server))
            num = cmd_server_ret - cmd_num_ret

            with open(save_address, "a+") as f:
                if -10 < num < 10:
                    f.write("LINUX系统基本组成题目四：check_atime.txt  %s检查两个文件一致, ---ok\n" % linux_txt_4)
                else:
                    f.write("LINUX系统基本组成题目四：check_atime.txt  %s检查两个文件不一致, ---error\n" % linux_txt_4)
        else:
            with open(save_address, "w") as f:
                f.write("LINUX系统基本组成题目四：文件%s不存在, ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("LINUX系统基本组成题目四：文件%s不存在,无法检查两个文件是否一致 ---error\n" % linux_txt_4)
    except:
        raise

    else:
        print("LINUX系统基本组成题目:成功")

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
    test_04()
