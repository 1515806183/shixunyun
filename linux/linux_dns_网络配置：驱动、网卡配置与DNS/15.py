#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    file_name = "/boot/grub/grub.conf"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(file_name):
                f.write("LINUX系统基本组成题目十五:文件 %s存在 ---ok\n" % file_name)
                cmd = "cat %s | grep timeout" % file_name
                ret = commands.getoutput(cmd)
                ret = int(re.findall(r'\d+', ret)[0])

                if ret == 10:
                    f.write("LINUX系统基本组成题目十五:系统在引导菜单停留的时间为: %s秒 ---ok\n" % ret)
                else:
                    f.write("LINUX系统基本组成题目十五:系统在引导菜单停留的时间为: %s秒 ---error\n" % ret)

            else:
                f.write("LINUX系统基本组成题目十五:文件 %s不存在, ---error\n" % file_name)
                f.write("LINUX系统基本组成题目十五:文件 %s不存在,无法查看菜单停留的时间 ---error\n" % file_name)

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
