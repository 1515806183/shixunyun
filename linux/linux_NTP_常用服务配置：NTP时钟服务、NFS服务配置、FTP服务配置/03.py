#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands
import os, re
save_address = "/tmp/score.txt"
# 测试文件
save_address_test = './test.txt'
linux_txt_3 = "/etc/ntp.conf"


def run():
    try:
        if os.path.exists(linux_txt_3):
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_data = "egrep 'server[[:space:]]+10.10.10.12' /etc/ntp.conf"
            com_ret_data = commands.getoutput(cmd_data)

            with open(save_address, "a+") as f:
                if com_ret_data == "":
                    f.write("Linux常用服务配置题目三：不存在配置server 10.10.10.12, ---error\n")
                else:
                    f.write("Linux常用服务配置题目三：存在配置server 10.10.10.12, ---ok\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目三：文件%s不存在, ---error\n" % linux_txt_3)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目三：文件%s不存在, 无法查询配置server 10.10.10.12, ---error\n" % linux_txt_3)

    except:
        print("Linux常用服务配置题目三:\033[0;34m失败\033[0m")

    else:
        print("Linux常用服务配置题目三:成功")



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
