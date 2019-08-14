#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/jichu05.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目五：文件%s存在, ---ok\n" % name)

            cmd_find = "find  /etc  -size +50k -a ! -user root -exec ls -ld {} \; "
            com_ret = commands.getoutput(cmd_find)

            cmd_cat = "cat %s" % name
            com_ret_cat = commands.getoutput(cmd_cat)

            if com_ret in com_ret_cat:
                f.write("LINUX系统基本组成题目五：%s文件内容输出一致, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目五：%s文件内容输出不一致, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目五:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目五:文件%s不存在,无法进行过滤对比 ---error\n" % name)

    except:
        print("LINUX系统基本组成题目五:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目五:成功")
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
