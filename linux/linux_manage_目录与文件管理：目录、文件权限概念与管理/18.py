#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/user08.sh"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目十八：文件%s存在, ---ok\n" % name)
            cmd_cat = "cat %s" % name
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            if "/user08/bin/cat" in com_ret_cat and "/user08/bin/lsblk" in com_ret_cat and "/user08/bin/ping" in com_ret_cat:
                f.write("Linux目录与文件管理题目十八：文件%s,存在限制 user08用户命令, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目十八：文件%s,不存在限制 user08用户命令, ---error\n" % name)

        else:
            f.write("Linux目录与文件管理题目十八：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目十八：文件%s不存在,无法查看限制 user08用户命令 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目十八:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十八:成功")
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
