#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import os
    save_address = "/tmp/score.txt"
    name = "/examdata/training/sam.txt"
    name_1 = "/examdata/result/jack.txt"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux性能诊断与调优题目三:文件%s存在 ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目三:文件%s不存在 ---error\n" % name)

            if os.path.exists(name_1):
                f.write("Linux性能诊断与调优题目三:文件%s存在 ---ok\n" % name_1)
            else:
                f.write("Linux目录与文件管理题目三:文件%s不存在 ---error\n" % name_1)

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

