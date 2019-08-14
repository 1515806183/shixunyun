#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_3 = "/examdata/result/mail.log"


def test_03():
    try:
        if os.path.exists(linux_txt_3):
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_egrep = "egrep '^mail.*[[:space:]]+-/examdata/result/mail.log' /examdata/result/mail.log"
            com_ret_egrep = commands.getoutput(cmd_egrep).lower().replace(" ", "")

            with open(save_address, "a+") as f:
                if com_ret_egrep:
                    f.write("Linux日志管理与配置题目三：查看  mail.*级别日志路径成功, ---ok\n")
                else:
                    f.write("Linux日志管理与配置题目三：查看 mail.*级别日志路径失败, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目三：文件%s不存在, ---error\n" % linux_txt_3)
                f.write("Linux日志管理与配置题目三：文件%s不存在,无法查询 mail.*级别日志路径 ---error\n" % linux_txt_3)

    except:
        print("Linux日志管理与配置题目三:\033[0;34m失败\033[0m")
        raise
    else:
        print("Linux日志管理与配置题目三:成功")

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
    test_03()
