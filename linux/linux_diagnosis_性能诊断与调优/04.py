#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
try:
    import commands

    save_address = "/tmp/score.txt"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd_1 = "cat /proc/sys/net/core/somaxconn"
            com_ret_1 = commands.getoutput(cmd_1)
            if "1024" in com_ret_1:
                f.write("Linux性能诊断与调优题目四:过滤输出为%s 成功,为1024 ---ok\n" % com_ret_1)

            else:
                f.write("Linux性能诊断与调优题目四:过滤输出为%s 失败,不为1024 ---error\n" % com_ret_1)

            # 2
            cmd_cat = "cat /etc/sysctl.conf|egrep '(net.core.somaxconn\s+=\s+1024)'"
            com_ret_cat = commands.getoutput(cmd_cat)
            if com_ret_cat:
                f.write("Linux性能诊断与调优题目四:过滤输出net.core.somaxconn = 1024成功 ---ok\n")

            else:
                f.write("Linux性能诊断与调优题目四:滤输出net.core.somaxconn = 1024失败 ---error\n")

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
