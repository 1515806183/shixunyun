#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/count_pwd"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目十三：文件%s存在, ---ok\n" % name)
            # 1
            cmd_cat = "cat /etc/passwd |wc -cl"
            com_ret_cat = commands.getoutput(cmd_cat)
            # 2
            cmd = "cat %s |wc -cl" %  name
            com_ret = commands.getoutput(cmd)

            if com_ret_cat == com_ret:
                f.write("Linux目录与文件管理题目十三：文件%s 字节数和行数一致, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目十三：文件%s 字节数和行数不一致, ---error\n" % name)
        else:
            f.write("Linux目录与文件管理题目十三：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目十三：文件%s不存在,无法比较字节数和行数 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目十三:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十三:成功")
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
