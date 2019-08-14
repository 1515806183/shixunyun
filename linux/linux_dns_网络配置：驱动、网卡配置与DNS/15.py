#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "/tmp/score.txt"
file_name = "/boot/grub/grub.conf"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(file_name):
            f.write("LINUX系统基本组成题目十五：文件: %s存在, ---ok\n" % file_name)
            cmd = "cat %s | grep timeout" % file_name
            ret = commands.getoutput(cmd)
            print ret
            ret = int(re.findall(r'\d+', ret)[0])

            if ret == 10:
                f.write("LINUX系统基本组成题目十五：系统在引导菜单停留的时间为: %s秒, ---ok\n" % ret)
            else:
                f.write("LINUX系统基本组成题目十五：系统在引导菜单停留的时间为: %s秒, ---error\n" % ret)

        else:
            f.write("LINUX系统基本组成题目十五：文件: %s不存在, ---error\n" % file_name)
            f.write("LINUX系统基本组成题目十五：文件: %s不存在,无法查看菜单停留的时间 ---error\n" % file_name)


    except:
        raise

    else:
        print("LINUX系统基本组成题目十五:成功")
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
