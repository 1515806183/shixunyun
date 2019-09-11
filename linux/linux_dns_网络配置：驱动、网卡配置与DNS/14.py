#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands

    save_address = "/tmp/score.txt"
    file_name = "/etc/motd"


    def run():
        try:
            f = open(save_address, 'w')
            cmd = "cat %s" % file_name
            ret = commands.getoutput(cmd).lower().replace(' ', '')

            str_name = "hello, welcome to login linux trainning system"
            str_name = str_name.replace(' ', '')

            if str_name in ret:
                f.write("LINUX系统基本组成题目十四:文件%s存在提示信息hello, welcome to login linux  trainning system ---ok\n" % file_name)
            else:
                f.write(
                    "LINUX系统基本组成题目十四:文件%s不存在提示信息hello, welcome to login linux  trainning system ---error\n" % file_name)

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
