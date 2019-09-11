#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_6 = "/examdata/result/rpmbuild_package_install.log"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd_rpm = "rpm -qa|grep e2fsprogs|wc -l"
            com_ret_rpm = int(commands.getoutput(cmd_rpm))

            if com_ret_rpm == 3:
                f.write("Linux软件安装与配置题目八:结果输出为%s 为3 ---ok\n" % com_ret_rpm)
            else:
                f.write("Linux软件安装与配置题目八:结果输出%s 不为3 ---error\n" % com_ret_rpm)

            # 2
            cmd_help = "extundelete --help"
            com_ret_help = commands.getoutput(cmd_help)

            if "command not found" in com_ret_help:
                f.write("Linux软件安装与配置题目八:extundelete --help 无帮助信息输出 ---error\n")
            else:
                f.write("Linux软件安装与配置题目八:extundelete --help 有帮助信息输出 ---ok\n")

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
