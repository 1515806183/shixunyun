#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_test = "./test.txt"

name = "/examdata/result/mem0.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目二：文件%s存在, ---ok\n" % name)

            cmd_1 = "free -m"
            com_ret_1 = commands.getoutput(cmd_1)

            cmd = 'cat %s' %  name
            com_ret = commands.getoutput(cmd)

            if com_ret_1 in com_ret :
                f.write("LINUX系统基本组成题目二：对比文件内容%s的输出一致, ---ok\n" % name)

            else:
                f.write("LINUX系统基本组成题目二：对比文件内容%s的输出不一致, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目二:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目二:文件%s不存在,无法进行过滤对比 ---error\n" % name)

    except:
        print("LINUX系统基本组成题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目二:成功")
        f.close()



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
