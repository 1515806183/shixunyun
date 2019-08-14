#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_2_1 = "/examdata/result/ping_01.sh"
linux_txt_2_2 = "/examdata/result/ping_log"


def run():
    try:
        # 1
        if os.path.exists(linux_txt_2_1):
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目二：文件%s存在, ---ok\n" % linux_txt_2_1)

            cmd_cat = "cat /examdata/result/ping_01.sh|grep '192.168.31.'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if "192.168.31." in com_ret_cat:
                    f.write("Linux命令与SHELL题目二：192.168.31.在文件中, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目二：192.168.31.不在文件中, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在, ---error\n" % linux_txt_2_1)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在,grep 192.168.31. 失败 ---error\n" % linux_txt_2_1)

        # 2
        if os.path.exists(linux_txt_2_2):
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s存在, ---ok\n" % linux_txt_2_2)

            cmd_cat = "head -n 5 /examdata/result/ping_log | grep '100%'"
            com_ret_cat = commands.getoutput(cmd_cat).replace(" ", "").lower()
            with open(save_address, "a+") as f:
                if "100%packetloss" in com_ret_cat:
                    f.write("Linux命令与SHELL题目二：100% packet loss过滤成功, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目二：100% packet loss过滤失败, ---error\n")
        else:
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在, ---error\n" % linux_txt_2_2)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在,100 packet loss过滤失败 ---error\n" % linux_txt_2_2)

    except:
        print("Linux命令与SHELL题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux命令与SHELL题目二:成功")



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
    run()
