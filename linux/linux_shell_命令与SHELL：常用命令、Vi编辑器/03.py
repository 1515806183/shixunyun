#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_3 = "/examdata/result/adduser_01.sh"


def run():
    try:
        # 1
        cmd_for = "for i in user{09..16};do id $i;done"
        com_ret_for = commands.getoutput(cmd_for).lower()
        with open(save_address, "w") as f:
            if "No such user".lower() in com_ret_for or "无此用户" in com_ret_for:
                f.write("Linux命令与SHELL题目三：检查用户是否创建了,没有创建用户, ---error\n")
            else:
                f.write("Linux命令与SHELL题目三：检查用户是否创建了,创建用户, ---ok\n")
        # 2
        if os.path.exists(linux_txt_3):
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_for = "egrep 'passwd\s+--stdin' %s" % linux_txt_3
            com_ret_for = commands.getoutput(cmd_for)

            with open(save_address, "a+") as f:
                if "passwd" in com_ret_for:
                    f.write("Linux命令与SHELL题目三：过滤passwd成功, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目三：过滤passwd失败, ---error\n")
        else:
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目三：文件%s不存在, ---error\n" % linux_txt_3)
                f.write("Linux命令与SHELL题目三：文件%s不存在,无法过滤passwd ---error\n" % linux_txt_3)

    except:
        print("Linux命令与SHELL题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux命令与SHELL题目三:成功")



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
