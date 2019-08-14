#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/sshd_cconfig_location"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目十二:文件%s存在, ---ok\n" % name)
            cmd = "cat %s | grep /etc/ssh/sshd_config" % name
            ret = commands.getoutput(cmd)
            if ret:
                f.write("LINUX系统基本组成题目十二：文件%s,有过滤出/etc/ssh/sshd_config ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目十二：文件%s,没有过滤出/etc/ssh/sshd_config, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目十二:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目十二:文件%s不存在,无法检查输出情况, ---error\n" % name)

    except:
        raise

    else:
        print("LINUX系统基本组成题目十二:成功")
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
