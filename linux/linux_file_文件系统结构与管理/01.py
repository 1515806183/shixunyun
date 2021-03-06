#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    name = "/examdata/result/etc_size"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux文件系统结构与管理题目一:文件%s存在 ---ok\n" % name)
                cmd = "du -sh /etc"
                ret = commands.getoutput(cmd)

                cmd_cat = "cat %s" % name
                ret_cat = commands.getoutput(cmd_cat)

                if ret in ret_cat:
                    f.write("Linux文件系统结构与管理题目一:/etc/目录的总文件大小 ---ok\n")
                else:
                    f.write("Linux文件系统结构与管理题目一:/etc/目录的总文件大小 ---error\n")

            else:
                f.write("Linux文件系统结构与管理题目一:文件%s不存在 ---error\n" % name)
                f.write("Linux文件系统结构与管理题目一:文件%s不存在,无法进行过滤对比 ---error\n" % name)

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
