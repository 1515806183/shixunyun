#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_2 = '192.168.100.3'


    def run():
        try:
            f = open(save_address, 'w')

            cmd_cat = "ip addr"
            com_ret = commands.getoutput(cmd_cat)
            ip_list = re.findall(r'%s' % linux_txt_2, com_ret)
            if linux_txt_2 in ip_list:
                f.write("LINUX系统基本组成题目二:检查eth1的IP地址，正常输出为192.168.100.3, ---ok\n")
            else:
                f.write("LINUX系统基本组成题目二:检查eth1的IP地址，正常输出不为192.168.100.3, ---error\n")

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
                print i.strip('\n').split(':')[1]
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
