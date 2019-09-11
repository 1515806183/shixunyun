#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    # 保存正式score文件
    import commands, os

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_9_file = '/examdata/result/xtgl_08.txt'


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_9_file):
                f.write("LINUX系统基本组成题目九：文件%s存在, ---ok\n" % linux_9_file)
                cmd_1 = "egrep -v '^(#|$|[0-9])' /examdata/training/new_sshd|wc -l"
                # cmd_2 = "egrep -v '^(#|$|[0-9])' /etc/ssh/sshd_config|wc -l"
                com_ret_1 = commands.getoutput(cmd_1)
                # com_ret_2 = commands.getoutput(cmd_2)

                cmd = "cat %s" % linux_9_file
                com_ret = commands.getoutput(cmd)

                if com_ret_1 in com_ret:
                    f.write("LINUX系统基本组成题目九：检查对比输出正确, ---ok\n'")

                else:
                    f.write("LINUX系统基本组成题目九：检查对比输出不正确, ---error\n'")

            else:
                f.write("LINUX系统基本组成题目九:文件%s不存在, ---error\n" % linux_9_file)
                f.write("LINUX系统基本组成题目九:文件%s不存在,无法进行过滤对比 ---error\n" % linux_9_file)

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
