#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/inode.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目二：文件%s存在, ---ok\n" % name)
            # 1
            cmd_txt = "df -i /|awk 'NR>1 {print $2}'"
            com_ret_txt = commands.getoutput(cmd_txt)
            # 2
            cmd_cat_txt = "cat /examdata/result/inode.txt"
            com_ret_cat = commands.getoutput(cmd_cat_txt)

            if com_ret_txt in com_ret_cat:
                f.write("Linux目录与文件管理题目二：跟文件%s比较输出正常, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目二：跟文件%s比较输出不正常, ---error\n" % name)

        else:
            f.write("Linux目录与文件管理题目二:文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目二:文件%s不存在,无法查询文件 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目二:成功")
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
