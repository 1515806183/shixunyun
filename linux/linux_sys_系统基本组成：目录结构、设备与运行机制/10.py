#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/opt/kong/sbin".lower()

def run():
    try:
        f = open(save_address, 'w')
        cmd = "echo $PATH"
        ret = commands.getoutput(cmd).lower()
        if name in ret:
            f.write(("LINUX系统基本组成题目十：检查出有%s这个路径, ---ok\n") % name)
        else:
            f.write(("LINUX系统基本组成题目十：检查出没有%s这个路径, ---error\n") % name)

    except:
        print("LINUX系统基本组成题目十:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目十:成功")
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
