#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'


    def run():
        try:
            f = open(save_address, 'w')
            cmd_swap = "swapon -s | awk 'NR>1 {print $3}'"
            com_ret_swap = commands.getoutput(cmd_swap)
            com_ret_swap = com_ret_swap.split('\n')
            num = 0
            for res in com_ret_swap:
                num += int(res)
            num = num/1024

            if 2020< num < 2060:
                f.write("LINUX安装与配置题目二:系统当前环境swap 大小为2G ---ok\n")
            else:
                f.write("LINUX安装与配置题目二:系统当前环境swap 大小不为2G ---error\n")

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
