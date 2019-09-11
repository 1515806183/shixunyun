#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    name = "/examdata/result/inode.txt"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux性能诊断与调优题目二:文件%s存在 ---ok\n" % name)
                # 1
                cmd_txt = "df -i /|awk 'NR>1 {print $2}'"
                com_ret_txt = commands.getoutput(cmd_txt)
                # 2
                cmd_cat_txt = "cat /examdata/result/inode.txt"
                com_ret_cat = commands.getoutput(cmd_cat_txt)

                if com_ret_txt in com_ret_cat:
                    f.write("Linux目录与文件管理题目二:跟文件%s比较输出正常 ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目二:跟文件%s比较输出不正常 ---error\n" % name)

            else:
                f.write("Linux目录与文件管理题目二:文件%s不存在 ---error\n" % name)
                f.write("Linux目录与文件管理题目二:文件%s不存在,无法查询文件 ---error\n" % name)

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

