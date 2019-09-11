#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_7_1 = "/mnt/Packages/mysql-server-5.1.71-1.el6.x86_64.rpm"
    linux_txt_7_2 = "/examdata/result/mysql.txt"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            com_ret_rpm = None
            if os.path.exists(linux_txt_7_1):

                f.write("Linux软件安装与配置题目七:文件%s存在 ---ok\n" % linux_txt_7_1)
                cmd_rpm = "rpm -qpR %s" % linux_txt_7_1
                com_ret_rpm = commands.getoutput(cmd_rpm)
            else:
                f.write("LinuxLinux软件安装与配置题目七:文件%s不存在 ---error\n" % linux_txt_7_1)

            # 2
            if os.path.exists(linux_txt_7_2):

                f.write("Linux软件安装与配置题目七:文件%s存在 ---ok\n" % linux_txt_7_2)

                cmd_cat = "cat %s" % linux_txt_7_2
                com_ret_cat = commands.getoutput(cmd_cat)
                if com_ret_rpm is not None:
                    if com_ret_cat in com_ret_rpm and "error" not in com_ret_rpm:
                        f.write("Linux软件安装与配置题目七:对比文件输出正确 ---ok\n")
                    else:
                        f.write("Linux软件安装与配置题目七:对比文件输出错误 ---error\n")
                else:
                    f.write("Linux软件安装与配置题目七:没有查询到mysql-server ---error\n")

            else:
                f.write("LinuxLinux软件安装与配置题目七:文件%s不存在 ---error\n" % linux_txt_7_2)
                f.write("LinuxLinux软件安装与配置题目七:文件%s不存在,无法进行比较 ---error\n" % linux_txt_7_2)

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
