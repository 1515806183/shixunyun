#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands
    import os, re

    save_address = "/tmp/score.txt"
    # 测试文件
    save_address_test = './test.txt'
    linux_txt_3 = "/etc/ntp.conf"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_3):
                f.write("Linux常用服务配置题目三:文件%s存在 ---ok\n" % linux_txt_3)

                cmd_data = "egrep 'server[[:space:]]+10.10.10.12' /etc/ntp.conf"
                com_ret_data = commands.getoutput(cmd_data)

                if com_ret_data == "":
                    f.write("Linux常用服务配置题目三:不存在配置server 10.10.10.12 ---error\n")
                else:
                    f.write("Linux常用服务配置题目三:存在配置server 10.10.10.12 ---ok\n")
            else:
                f.write("Linux常用服务配置题目三:文件%s不存在 ---error\n" % linux_txt_3)
                f.write("Linux常用服务配置题目三:文件%s不存在, 无法查询配置server 10.10.10.12 ---error\n" % linux_txt_3)

        except Exception as e:
            print str(e) + '---except'

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
    print str(e) + '---except'

else:
    if __name__ == '__main__':
        run()
