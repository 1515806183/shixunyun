#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/jichu06_conf"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目六：文件%s存在, ---ok\n" % name)
            # 1
            num = True
            cmd_find = "ls -l /etc/ssh/sshd_config %s | awk '{print $2}'" % name
            com_ret = commands.getoutput(cmd_find).split('\n')

            for ret in com_ret:
                if ret == 2:
                    num = False
                    break

            if num:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config存在硬链接, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config不存在硬链接, ---error\n" % name)
            # 2
            cmd_diff = "diff /etc/ssh/sshd_config %s" % name
            ret = commands.getoutput(cmd_diff)
            if not ret:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config内容一致, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config内容不一致, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目六:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行判断是否存在超链接, ---error\n" % name)
            f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行判断内容不一致, ---error\n" % name)

    except:
        print("LINUX系统基本组成题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目六:成功")
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
