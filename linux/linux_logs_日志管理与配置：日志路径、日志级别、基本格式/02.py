#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_2 = "/examdata/result/rsyslog_log_level"


def test_02():
    try:
        if os.path.exists(linux_txt_2):
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目二：文件%s存在, ---ok\n" % linux_txt_2)

            cmd_egrep = "egrep '^*\.\*' /etc/rsyslog.conf | egrep -v '@|#'"
            com_ret_egrep = commands.getoutput(cmd_egrep)

            cmd_cat = "cat %s" % linux_txt_2
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if com_ret_egrep in com_ret_cat:
                    f.write("Linux日志管理与配置题目二：输出一致, ---ok\n")
                else:
                    f.write("Linux日志管理与配置题目二：输出不一致, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目二：文件%s不存在, ---error\n" % linux_txt_2)
                f.write("Linux日志管理与配置题目二：文件%s不存在,无法进行输出比较 ---error\n" % linux_txt_2)

    except:
        print("Linux日志管理与配置题目二:\033[0;34m失败\033[0m")
        raise
    else:
        print("Linux日志管理与配置题目二:成功")

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
    test_02()
