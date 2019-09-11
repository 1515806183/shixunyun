#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands
    import os, re

    save_address = "/tmp/score.txt"
    # 测试文件
    save_address_test = './test.txt'
    linux_txt_2 = "/examdata/result/date.txt"


    def run():
        try:
            f = open(save_address, 'w')
            cmd_data = "date"
            com_ret_data_now = commands.getoutput(cmd_data)
            a_list = re.findall('\d+', com_ret_data_now)[:-1]

            cmd_hwclock = "hwclock"
            com_ret_hwclock_now = commands.getoutput(cmd_hwclock)
            b = "".join(com_ret_hwclock_now.split(' ')[:-3])
            b_list = re.findall('\d+', b)[:-1]

            if a_list == b_list:
                f.write("Linux常用服务配置题目二:时间是同步的 ---ok\n")
            else:
                f.write("Linux常用服务配置题目二:时间是不同步的 ---error\n")

            if os.path.exists(linux_txt_2):

                f.write("Linux常用服务配置题目二:文件%s存在 ---ok\n" % linux_txt_2)

                cmd_cat = "cat /examdata/result/date.txt"
                com_ret_cat = commands.getoutput(cmd_cat)

                if com_ret_data_now in com_ret_cat or com_ret_hwclock_now in com_ret_cat:
                    f.write("Linux常用服务配置题目二:输出一致 ---ok\n")
                else:
                    f.write("Linux常用服务配置题目二:输出不一致 ---error\n")

            else:
                f.write("Linux常用服务配置题目二:文件%s不存在 ---error\n" % linux_txt_2)
                f.write("Linux常用服务配置题目二:文件%s不存在,无法进行时间比较 ---error\n" % linux_txt_2)

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
