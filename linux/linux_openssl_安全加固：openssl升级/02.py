#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/ssh_version.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX安全加固openssl升级题目二：文件%s存在, ---ok\n" % name)

            cmd_grep = "cat /ssh_version.txt |grep OpenSSH_5.3p1"
            com_ret = commands.getoutput(cmd_grep).lower()
            if 'openssh_5.3p1' in com_ret:
                f.write("LINUX安全加固openssl升级题目二：grep OpenSSH_5.3p1成功, ---ok\n")
            else:
                f.write("LINUX安全加固openssl升级题目二：grep OpenSSH_5.3p1失败,---error\n")

        else:
            f.write("LINUX安全加固openssl升级题目二：文件%s不存在, ---error\n" % name)
            f.write("LINUX安全加固openssl升级题目二：文件%s不存在,grep OpenSSH_5.3p1失败 ---error\n" % name)

    except:
        print("LINUX安全加固openssl升级题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安全加固openssl升级题目二:成功")
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
