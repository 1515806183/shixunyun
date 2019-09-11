#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_1 = "/examdata/result/apache_install_log"


    def run():
        try:
            f = open(save_address, 'w')
            cmd_chkconfig = "chkconfig --list httpd| grep '3:启用'"
            com_ret_chkconfig = commands.getoutput(cmd_chkconfig)

            if "3:启用" in com_ret_chkconfig:
                f.write("Linux软件安装与配置题目二:设置httpd开机启动成功 ---ok\n")
            else:
                f.write("Linux软件安装与配置题目二:设置httpd开机启动失败 ---error\n")

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
