#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_2_1 = "/examdata/result/ping_01.sh"
    linux_txt_2_2 = "/examdata/result/ping_log"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            if os.path.exists(linux_txt_2_1):

                f.write("Linux命令与SHELL题目二:文件%s存在 ---ok\n" % linux_txt_2_1)

                cmd_cat = "cat /examdata/result/ping_01.sh|grep '192.168.31.'"
                com_ret_cat = commands.getoutput(cmd_cat)

                if "192.168.31." in com_ret_cat:
                    f.write("Linux命令与SHELL题目二:192.168.31.在文件中 ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目二:192.168.31.不在文件中 ---error\n")
            else:
                f.write("Linux命令与SHELL题目二:文件%s不存在 ---error\n" % linux_txt_2_1)
                f.write("Linux命令与SHELL题目二:文件%s不存在,grep 192.168.31. 失败 ---error\n" % linux_txt_2_1)

            # 2
            if os.path.exists(linux_txt_2_2):

                f.write("Linux命令与SHELL题目二:文件%s存在 ---ok\n" % linux_txt_2_2)

                cmd_cat = "head -n 5 /examdata/result/ping_log | grep '100%'"
                com_ret_cat = commands.getoutput(cmd_cat).replace(" ", "").lower()

                if "100%packetloss" in com_ret_cat:
                    f.write("Linux命令与SHELL题目二:100% packet loss过滤成功 ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目二:100% packet loss过滤失败 ---error\n")
            else:
                f.write("Linux命令与SHELL题目二:文件%s不存在 ---error\n" % linux_txt_2_2)
                f.write("Linux命令与SHELL题目二:文件%s不存在,100 packet loss过滤失败 ---error\n" % linux_txt_2_2)

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
