#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_4 = "/examdata/result/log_format"


def test_04():
    try:
        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目四：文件%s存在, ---ok\n" % linux_txt_4)
            # 1
            cmd_cat = "cat %s|wc -l" % linux_txt_4
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if int(com_ret_cat) > 0:
                    f.write("Linux日志管理与配置题目四：查看大于一行, ---ok\n")
                else:
                    f.write("Linux日志管理与配置题目四：查看小于一行, ---error\n")

            # 2
            cmd_head = "head -n 1 %s |grep '[0-9]\{4\}/[0-9]\{2\}/[0-9]\{2\}\s[0-9]\{2\}:[0-9]\{2\}:[0-9]\{2\}'" % linux_txt_4
            com_ret_head = commands.getoutput(cmd_head)
            com_ret_head = re.findall(r'(\d{4}/\d{1,2}/\d{1,2}\s\d{1,2}:\d{1,2}:\d{1,2})', com_ret_head)

            with open(save_address, "a+") as f:
                if len(com_ret_head) == 0:
                    f.write("Linux日志管理与配置题目四：格式输出当前时间失败, ---error\n")
                else:
                    f.write("Linux日志管理与配置题目四：格式输出当前时间成功, ---ok\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目四：文件%s不存在, ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux日志管理与配置题目四：文件%s不存在,无法进行查看行数 ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux日志管理与配置题目四：文件%s不存在,无法格式输出当前时间 ---error\n" % linux_txt_4)

    except:
        raise
    else:
        print("Linux日志管理与配置题目四:成功")

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
    test_04()
