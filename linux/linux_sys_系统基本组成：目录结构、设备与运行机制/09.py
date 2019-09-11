#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    name = "/examdata/result/ls_man_location"
    file_name = "/usr/share/man/man1/ls.1.gz"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("LINUX系统基本组成题目九:文件%s存在 ---ok\n" % name)
                cmd = "cat %s" % name
                ret = commands.getoutput(cmd).lower()
                if file_name.lower() in ret:
                    f.write("LINUX系统基本组成题目九:输出正确 ---ok\n")
                else:
                    f.write("LINUX系统基本组成题目九:输出错误 ---error\n")

            else:
                f.write("LINUX系统基本组成题目九:文件%s不存在 ---error\n" % name)
                f.write("LINUX系统基本组成题目九:文件%s不存在,无法检查输出情况 ---error\n" % name)

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
