#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands
    import os

    save_address = "/tmp/score.txt"
    # 测试文件
    save_address_test = './test.txt'

    linux_txt_1 = "/examdata/result/date_ago.txt"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_1):

                f.write("Linux常用服务配置题目一:文件%s存在 ---ok\n" % linux_txt_1)

                cmd = "date +%F -d '-100 days'"
                com_ret = commands.getoutput(cmd)
                cmd = "cat /examdata/result/date_ago.txt"
                cmd_ret_txt = commands.getoutput(cmd)

                if com_ret in cmd_ret_txt:
                    f.write("Linux常用服务配置题目一:输出一致 ---ok\n")
                else:
                    f.write("Linux常用服务配置题目一:输出不一致 ---error\n")
            else:
                f.write("Linux常用服务配置题目一:文件%s不存在 ---error\n" % linux_txt_1)
                f.write("Linux常用服务配置题目一:文件%s不存在,无法进行对比输出 ---error\n" % linux_txt_1)

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
