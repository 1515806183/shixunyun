#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
save_address_test = './test.txt'

file_name01 = '/etc/inittab'
filename_2 = "/examdata/result/default_boot_mode"


def test_04():
    try:
        # 1
        cmd = 'echo $LANG'
        com_ret = commands.getoutput(cmd).lower()
        with open(save_address, 'w') as f:
            if "en_US.utf8".lower() in com_ret or 'en_US.utf-8'.lower() in com_ret:
                f.write("LINUX安装与配置题目四：echo $LANG,输出结果为 %s , ---ok" % com_ret + '\n')
            else:
                f.write("LINUX安装与配置题目四：echo $LANG,输出结果为 %s , ---error" % com_ret + '\n')
        # 2
        cmd = 'cat /etc/sysconfig/i18n'
        com_ret = commands.getoutput(cmd).lower()
        with open(save_address, 'a+') as f:
            if 'en_US.UTF-8'.lower() in com_ret or "en_US.UTF8".lower() in com_ret:
                f.write("LINUX安装与配置题目四：检查cat /etc/sysconfig/i18n,输出结果为 %s , ---ok" % com_ret + '\n')
            else:
                f.write("LINUX安装与配置题目四：检查cat /etc/sysconfig/i18n,输出结果为 %s , ---error" % com_ret + '\n')

    except:
        print("操作LINUX安装与配置题目四:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目四:成功")

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
    test_04()






