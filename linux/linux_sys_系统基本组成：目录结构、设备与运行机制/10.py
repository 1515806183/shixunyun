#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    name = "/opt/kong/sbin".lower()


    def run():
        try:
            f = open(save_address, 'w')
            cmd = "echo $PATH"
            ret = commands.getoutput(cmd).lower()
            if name in ret:
                f.write(("LINUX系统基本组成题目十:检查出有%s这个路径 ---ok\n") % name)
            else:
                f.write(("LINUX系统基本组成题目十:检查出没有%s这个路径 ---error\n") % name)

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
