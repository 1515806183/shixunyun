#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re
    save_address = "/tmp/score.txt"

    def run():
        try:
            f = open(save_address, 'w')
            cmd_grep = "openssl version | grep 1.0.2k"
            com_ret = commands.getoutput(cmd_grep)
            if '1.0.2k' in com_ret:
                f.write("LINUX安全加固openssl升级题目一:grep 1.0.2k成功 ---ok\n")
            else:
                f.write("LINUX安全加固openssl升级题目一:grep 1.0.2k失败 ---error\n")

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
