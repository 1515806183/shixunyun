#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"


    def run():
        try:
            f = open(save_address, 'w')

            cmd_dir = "ls -F /examdata/result/ | grep ^dir_level.*/$ | wc -l"
            com_ret = int(commands.getoutput(cmd_dir))
            if com_ret == 5:
                f.write("Linux目录与文件管理题目十:目录前缀为dir_level的数量为%s, ---ok\n" % com_ret)
            else:
                f.write("Linux目录与文件管理题目十:目录前缀为dir_level的数量为%s, ---error\n" % com_ret)


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

