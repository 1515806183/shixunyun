#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/dir_raid1"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_grep = "cat /etc/fstab |egrep '/examdata/dir_raid1\s+ext3\s+defaults,acl'"
        com_ret = commands.getoutput(cmd_grep).replace(" ", "")
        if "/examdata/dir_raid1ext3defaults,acl" in com_ret:
            f.write("LINUX内核用户限制参数题目一：grep /examdata/dir_raid1   ext3   defaults,acl成功, ---ok\n")
        else:
            f.write("LINUX内核用户限制参数题目一：grep /examdata/dir_raid1 ext3 defaults,acl失败, ---error\n")
        # 2
        if os.path.exists(name):
            f.write("LINUX内核用户限制参数题目一：文件%s存在, ---ok\n" % name)

            cmd_grep = "getfacl %s|grep 'user:user06:---'"
            com_ret = commands.getoutput(cmd_grep).replace(" ", "")
            if 'user:user06:---' in com_ret:
                f.write("LINUX内核用户限制参数题目一：grep user:user06:---成功, ---ok\n")
            else:
                f.write("LINUX内核用户限制参数题目一：grep user:user06:---失败, ---error\n")

        else:
            f.write("LINUX内核用户限制参数题目一：文件%s不存在, ---error\n" % name)
            f.write("LINUX内核用户限制参数题目一：文件%s不存在,grep user:user06:---失败 ---error\n" % name)

    except:
        raise

    else:
        print("LINUX内核用户限制参数题目一:成功")
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
