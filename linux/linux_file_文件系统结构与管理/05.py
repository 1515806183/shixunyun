#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_df = "df -hTP|grep '/dev/shm'|awk '{print $5}'"
        com_ret_df = commands.getoutput(cmd_df)
        ret_str = com_ret_df[-1:].lower()
        com_num = re.search(r'\d+', com_ret_df).group()
        if ret_str == 'm':
            if com_num == "4096":
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sM, 为4096M(4G) ---ok\n" % com_num)
            else:
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sM, 不为4096M(4G) ---ok\n" % com_num)
        else:
            if com_num == "4":
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sG, 为4G ---ok\n" % com_num)
            else:
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sG, 不为4G ---ok\n" % com_num)

    except:
        print("Linux文件系统结构与管理题目五:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目五:成功")
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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
