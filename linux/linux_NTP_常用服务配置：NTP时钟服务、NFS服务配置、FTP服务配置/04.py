#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands
    import os, re

    save_address = "/tmp/score.txt"
    # 测试文件
    save_address_test = './test.txt'
    linux_txt_4 = "/examdata/result/future_day"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_4):

                f.write("Linux常用服务配置题目四:文件%s存在 ---ok\n" % linux_txt_4)

                cmd_data = 'date +%F -d "+20 days" '
                com_ret_data_now = commands.getoutput(cmd_data)

                cmd_cat_txt = "cat %s" % linux_txt_4
                com_ret_cat = commands.getoutput(cmd_cat_txt)

                if com_ret_data_now in com_ret_cat:
                    f.write("Linux常用服务配置题目四:跟文件%s,输出一致 ---ok\n" % linux_txt_4)
                else:
                    f.write("Linux常用服务配置题目四:跟文件%s,输出不一致 ---error\n" % linux_txt_4)

            else:
                f.write("Linux常用服务配置题目四:文件%s不存在 ---error\n" % linux_txt_4)
                f.write("Linux常用服务配置题目四:文件%s不存在,无法进行输出比较 ---error\n" % linux_txt_4)

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
