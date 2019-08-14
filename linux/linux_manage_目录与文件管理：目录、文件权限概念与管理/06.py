#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/user20_can_write"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目六：文件%s存在, ---ok\n" % name)
            # 1
            cmd_dir = "cat %s" % name
            com_ret = commands.getoutput(cmd_dir)

            if "drwxr--rwx" in com_ret and ".ssh" in com_ret:
                f.write("Linux目录与文件管理题目六：检查文件属性内容一致, ---ok\n")
            else:
                f.write("Linux目录与文件管理题目六：检查文件属性不一致, ---error\n")

        else:
            f.write("Linux目录与文件管理题目六:文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目六:文件%s不存在,无法检查文件属性 ---error\n" % name)

    except:
        raise

    else:
        print("Linux目录与文件管理题目六:成功")
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
