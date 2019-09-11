#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    # 保存正式score文件
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_3 = '10.10.10.9'


    def run():
        try:
            f = open(save_address, 'w')

            cmd_ip = 'route -n | egrep "10.10.10.9\s+.*\s+255.255.255.255\s+UH\s+0\s+0\s+0\s+eth0"'
            # cmd_ip = 'route -n | egrep "192.168.61.0\s+.*\s+255.255.255.0\s+U\s+0\s+0\s+0\s+eth0"'
            com_ret = commands.getoutput(cmd_ip)

            if com_ret == "":
                f.write("LINUX系统基本组成题目三:查询路由过滤失败, ---error" + '\n')
            else:
                f.write("LINUX系统基本组成题目三:查询路由过滤成功, ---ok" + '\n')

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
