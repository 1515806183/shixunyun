#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    # 保存正式score文件
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_4 = "/examdata/result/find_var.txt"


    def run():
        try:
            f = open(save_address, 'w')

            if os.path.exists(linux_txt_4):

                f.write("LINUX系统基本组成题目四:文件%s存在, ---ok\n" % linux_txt_4)

                cmd_check = "find /var ! -atime -90 > ./check_atime.txt"
                commands.getoutput(cmd_check)

                # 比较两个文件内容
                cmd_num_file = "cat ./check_atime.txt|wc -l"
                cmd_num_server = "cat %s|wc -l" % linux_txt_4

                cmd_num_ret = int(commands.getoutput(cmd_num_file))
                cmd_server_ret = int(commands.getoutput(cmd_num_server))
                num = cmd_server_ret - cmd_num_ret

                if -10 < num < 10:
                    f.write("LINUX系统基本组成题目四:check_atime.txt  %s检查两个文件一致, ---ok\n" % linux_txt_4)

                else:
                    f.write("LINUX系统基本组成题目四:check_atime.txt  %s检查两个文件不一致, ---error\n" % linux_txt_4)

            else:
                f.write("LINUX系统基本组成题目四:文件%s不存在, ---error\n" % linux_txt_4)
                f.write("LINUX系统基本组成题目四:文件%s不存在,无法检查两个文件是否一致 ---error\n" % linux_txt_4)

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
