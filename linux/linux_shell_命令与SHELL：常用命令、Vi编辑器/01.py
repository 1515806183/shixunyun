#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_1_1 = "/examdata/result/file_check.sh"
    linux_txt_1_2 = "/examdata/result/logical"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_1_1):
                f.write("Linux命令与SHELL题目一:文件%s存在 ---ok\n" % linux_txt_1_1)
            else:
                f.write("Linux命令与SHELL题目一:文件%s不存在 ---error\n" % linux_txt_1_1)

            if os.path.exists(linux_txt_1_2):
                f.write("Linux命令与SHELL题目一:文件%s存在 ---ok\n" % linux_txt_1_2)

                cmd_file = "file %s | grep empty" % linux_txt_1_2
                com_ret_file = commands.getoutput(cmd_file).lower()

                if "empty" in com_ret_file:
                    f.write("Linux命令与SHELL题目一: grep empty ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目一: grep empty ---error\n")
            else:
                f.write("Linux命令与SHELL题目一:文件%s不存在 ---error\n" % linux_txt_1_2)
                f.write("Linux命令与SHELL题目一:文件%s不存在,无法进行grep empty ---error\n" % linux_txt_1_2)

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
