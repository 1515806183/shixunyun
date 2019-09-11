#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    name = "/examdata/result/vmstat.txt"

    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux性能诊断与调优题目一:文件%s存在 ---ok\n" % name)

                # 1
                cmd_1 = "cat %s|wc -l" % name
                com_ret_1 = commands.getoutput(cmd_1)
                if "12" in com_ret_1:
                    f.write("Linux性能诊断与调优题目一:输出结果为数字12 ---ok\n")

                else:
                    f.write("Linux性能诊断与调优题目一:输出结果不为数字12 ---error\n")

                # 2
                cmd_2 = "cat %s|grep free|awk ' {print $3,$NF}'" % name
                com_ret_2 = commands.getoutput(cmd_2).lower()

                if "swpd" in com_ret_2 and "st" in com_ret_2:
                    f.write("Linux性能诊断与调优题目一:输出为swpd st ---ok\n")

                else:
                    f.write("Linux性能诊断与调优题目一:输出不为swpd st ---error\n")

            else:
                f.write("Linux性能诊断与调优题目一:文件%s不存在 ---error\n" % name)
                f.write("Linux性能诊断与调优题目一:文件%s不存在,无法输出文件大小 ---error\n" % name)
                f.write("Linux性能诊断与调优题目一:文件%s不存在,无法输出swpd st ---error\n" % name)

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
                print i.strip('\n').split(':')[1]
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
