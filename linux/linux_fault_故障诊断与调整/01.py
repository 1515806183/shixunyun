#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/resolve_ftp_login_error"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX故障诊断与调整题目一：文件%s存在, ---ok\n" % name)
            # 1
            cmd_grep = "cat %s|grep 'setsebool\s-P\sftp_home_dir\son'" % name
            com_ret = commands.getoutput(cmd_grep).lower().replace(" ", "")

            if 'setsebool-pftp_home_diron' in com_ret:
                f.write("LINUX故障诊断与调整题目一：grep setsebool -P ftp_home_dir on成功, ---ok\n")
            else:
                f.write("LINUX故障诊断与调整题目一：grep setsebool -P ftp_home_dir on失败, ---error\n")

        else:
            f.write("LINUX故障诊断与调整题目一：文件%s不存在, ---error\n" % name)
            f.write("LINUX故障诊断与调整题目一：文件%s不存在,grep setsebool -P ftp_home_dir on失败 ---error\n" % name)

    except:
        print("LINUX故障诊断与调整题目一:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX故障诊断与调整题目一:成功")
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
