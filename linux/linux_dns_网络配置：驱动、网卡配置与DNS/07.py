#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    # 保存正式score文件
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_7 = "/examdata/result/process_running"


    def run():
        try:
            f = open(save_address, 'w')

            if os.path.exists(linux_txt_7):
                f.write("LINUX系统基本组成题目七:文件%s存在, ---ok\n" % linux_txt_7)

                # 1
                cmd_cat_1 = "sed -n 1p %s" % linux_txt_7
                com_ret_1 = commands.getoutput(cmd_cat_1)
                com_ret_1 = re.findall(r'\d+年\s+\d+月\s+\d+日', com_ret_1)
                if com_ret_1:
                    f.write("LINUX系统基本组成题目七:日期输出在第一行, ---ok\n")

                else:
                    f.write("LINUX系统基本组成题目七:日期输出不在第一行, ---error\n")

                # 2
                cmd_cat_2 = "sed -n 2p %s" % linux_txt_7
                com_ret_2 = commands.getoutput(cmd_cat_2)
                if com_ret_2.isdigit():
                    f.write("LINUX系统基本组成题目七:第二行为进程数量, ---ok\n")

                else:
                    f.write("LINUX系统基本组成题目七:第二行不为进程数量, ---error\n")

            else:
                f.write("LINUX系统基本组成题目七:文件%s不存在, ---error\n" % linux_txt_7)
                f.write("LINUX系统基本组成题目七:文件%s不存在,无法进行过滤查询 ---error\n" % linux_txt_7)

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
