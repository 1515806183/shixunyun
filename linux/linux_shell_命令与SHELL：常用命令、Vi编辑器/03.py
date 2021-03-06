#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_3 = "/examdata/result/adduser_01.sh"


    def run():
        try:
            # 1
            f = open(save_address, 'w')
            cmd_for = "for i in user{09..16};do id $i;done"
            com_ret_for = commands.getoutput(cmd_for).lower()

            if "No such user".lower() in com_ret_for or "无此用户" in com_ret_for:
                f.write("Linux命令与SHELL题目三:检查用户是否创建,没有创建用户错误 ---error\n")
            else:
                f.write("Linux命令与SHELL题目三:检查用户是否创建,创建用户正确 ---ok\n")
            # 2
            if os.path.exists(linux_txt_3):

                f.write("Linux命令与SHELL题目三:文件%s存在 ---ok\n" % linux_txt_3)

                cmd_for = "egrep 'passwd\s+--stdin' %s" % linux_txt_3
                com_ret_for = commands.getoutput(cmd_for)

                if "passwd" in com_ret_for:
                    f.write("Linux命令与SHELL题目三:过滤passwd成功 ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目三:过滤passwd失败 ---error\n")
            else:
                f.write("Linux命令与SHELL题目三:文件%s不存在 ---error\n" % linux_txt_3)
                f.write("Linux命令与SHELL题目三:文件%s不存在,无法过滤passwd ---error\n" % linux_txt_3)

        except Exception as e:
            print str(e) + ' ---except'

        else:
            f.close()

        finally:
            with open(save_address) as f:
                num = f.readlines()

            # 总题目数
            sum = len(num)
            # 一题多少分
            average = 100 // sum

            # 正确的题目总数
            timu_all = 0
            for i in num:
                print i.strip("\n").split(":")[1]

                if '---ok' in i:
                    timu_all += 1

            if timu_all == sum:
                total_score = 100
            else:
                total_score = timu_all * average

            print str(total_score) + ' ---score'


except Exception as e:
    print str(e) + ' ---except'

else:
    if __name__ == '__main__':
        run()
