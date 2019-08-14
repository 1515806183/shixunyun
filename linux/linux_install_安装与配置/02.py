#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands
save_address = "/tmp/score.txt"
save_address_test = './test.txt'


def test_02():
    try:
        cmd_swap = "swapon -s | awk 'NR>1 {print $3}'"
        com_ret_swap = commands.getoutput(cmd_swap)
        com_ret_swap = com_ret_swap.split('\n')
        num = 0
        for res in com_ret_swap:
            num += int(res)
        num = num/1024
        with open(save_address, 'w') as f:
            if 2020< num < 2060:
                f.write("LINUX安装与配置题目二：系统当前环境swap 大小为2G, ---ok" + '\n')
            else:
                f.write("LINUX安装与配置题目二：系统当前环境swap 大小不为2G, ---error" + '\n')
    except:
        print("操作LINUX安装与配置题目二:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目二:成功")

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
    test_02()



