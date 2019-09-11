#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    import re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    file = '/examdata/result/hosts.bak'


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(file):
                f.write("LINUX系统基本组成题目十一:文件%s存在 ---ok\n" % file)
                cmd = "date"
                ret = commands.getoutput(cmd)
                ret_date = re.search(r'\d+年\s+\d+月', ret).group()
                cmd_host_name = "hostname"
                ret_host_name = commands.getoutput(cmd_host_name)
                cmd = "cat %s|egrep '(%s|%s)'" % (file, ret_date, ret_host_name)
                ret = commands.getoutput(cmd)
                if ret:
                    f.write("LINUX系统基本组成题目十一:文件%s里包含日期和主机名 ---ok\n" % file)
                else:
                    f.write("LINUX系统基本组成题目十一:文件%s里不包含日期和主机名 ---error\n" % file)
            else:
                f.write("LINUX系统基本组成题目十一:文件%s不存在, ---error\n" % file)
                f.write("LINUX系统基本组成题目十一:文件%s不存在,无法进行过滤主机名日期对比 ---error\n" % file)

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
