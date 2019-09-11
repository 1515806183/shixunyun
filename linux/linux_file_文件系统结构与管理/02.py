#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    name = "/examdata/result/boot_bak*"
    var = "/examdata/result/boot_bak"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(var):
                f.write("Linux文件系统结构与管理题目二:文件%s存在 ---ok\n" % var)
                cmd = "ls %s" % name
                ret = commands.getoutput(cmd)
                print ret

                if ret:
                    f.write("Linux文件系统结构与管理题目二:备份文件%s存在 ---ok\n" % ret)
                else:
                    f.write("Linux文件系统结构与管理题目二:备份文件%s不存在 ---error\n" % ret)
            else:
                f.write("Linux文件系统结构与管理题目二:文件%s不存在 ---error\n" % var)
                f.write("Linux文件系统结构与管理题目二:文件%s不存在,无法查看备份文件 ---error\n" % var)


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
