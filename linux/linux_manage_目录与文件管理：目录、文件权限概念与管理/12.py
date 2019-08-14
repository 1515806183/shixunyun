#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/new_passwd"
etc_name = "/etc/passwd"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目十二：文件%s存在, ---ok\n" % name)
            cmd_diff = "diff /etc/passwd %s" % name
            com_ret_diff = commands.getoutput(cmd_diff)

            if com_ret_diff == "":
                f.write("Linux目录与文件管理题目十二：文件%s和文件%s内容一致, ---ok\n" % (name, etc_name))
            else:
                f.write("Linux目录与文件管理题目十二：文件%s和文件%s内容不一致, ---error\n" % (name, etc_name))
        else:
            f.write("Linux目录与文件管理题目十二：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目十二：文件%s不存在,无法比较文件%s和文件%s ---error\n" % (name, name, etc_name))

    except:
        raise

    else:
        print("Linux目录与文件管理题目十二:成功")
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
