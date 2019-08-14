#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_3 = '10.10.10.9'


def test_03():
    try:
        cmd_ip = 'route -n | egrep "10.10.10.9\s+.*\s+255.255.255.0\s+UH\s+0\s+0\s+0\s+eth0"'
        # cmd_ip = 'route -n | egrep "192.168.61.0\s+.*\s+255.255.255.0\s+U\s+0\s+0\s+0\s+eth0"'
        com_ret = commands.getoutput(cmd_ip)
        print com_ret
        with open(save_address, 'w') as f:
            if com_ret == "":
                f.write("LINUX系统基本组成题目三：查询路由过滤失败, ---error" + '\n')
            else:
                f.write("LINUX系统基本组成题目三：查询路由过滤成功, ---ok" + '\n')
    except:
        print("LINUX系统基本组成题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目三:成功")

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
    test_03()
