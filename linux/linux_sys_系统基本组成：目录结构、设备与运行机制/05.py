#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    name = "/examdata/result/jichu05.txt"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("LINUX系统基本组成题目五:文件%s存在 ---ok\n" % name)

                cmd_find = "find  /etc  -size +50k -a ! -user root -exec ls -ld {} \; "
                com_ret = commands.getoutput(cmd_find)

                cmd_cat = "cat %s" % name
                com_ret_cat = commands.getoutput(cmd_cat)

                if com_ret in com_ret_cat:
                    f.write("LINUX系统基本组成题目五:%s文件内容输出一致 ---ok\n" % name)
                else:
                    f.write("LINUX系统基本组成题目五:%s文件内容输出不一致 ---error\n" % name)

            else:
                f.write("LINUX系统基本组成题目五:文件%s不存在 ---error\n" % name)
                f.write("LINUX系统基本组成题目五:文件%s不存在,无法进行过滤对比 ---error\n" % name)

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
