#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    name = "/examdata/result/jichu06_conf"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("LINUX系统基本组成题目六:文件%s存在 ---ok\n" % name)
                # 1
                num = True
                cmd_find = "ls -l /etc/ssh/sshd_config %s | awk '{print $2}'" % name
                com_ret = commands.getoutput(cmd_find).split('\n')

                for ret in com_ret:
                    if ret == 2:
                        num = False
                        break

                if num:
                    f.write("LINUX系统基本组成题目六:检查%s, /etc/ssh/sshd_config存在硬链接 ---ok\n" % name)
                else:
                    f.write("LINUX系统基本组成题目六:检查%s, /etc/ssh/sshd_config不存在硬链接 ---error\n" % name)
                # 2
                cmd_diff = "diff /etc/ssh/sshd_config %s" % name
                ret = commands.getoutput(cmd_diff)
                if not ret:
                    f.write("LINUX系统基本组成题目六:检查%s, /etc/ssh/sshd_config内容一致 ---ok\n" % name)
                else:
                    f.write("LINUX系统基本组成题目六:检查%s, /etc/ssh/sshd_config内容不一致 ---error\n" % name)

            else:
                f.write("LINUX系统基本组成题目六:文件%s不存在 ---error\n" % name)
                f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行判断是否存在超链接 ---error\n" % name)
                f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行判断内容不一致 ---error\n" % name)

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
