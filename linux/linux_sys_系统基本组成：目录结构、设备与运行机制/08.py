#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/system_character"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目八:文件%s存在, ---ok\n" % name)
            cmd = "cat %s" % name
            ret = commands.getoutput(cmd).lower()
            if "en_US.UTF-8".lower() in ret or "en_US.UTF8".lower() in ret:
                f.write("LINUX系统基本组成题目八：检查%s,字符集, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目八：检查%s,字符集, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目八:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目八:文件%s不存在,无法检查字符集, ---error\n" % name)

    except:
        print("LINUX系统基本组成题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目八:成功")
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
