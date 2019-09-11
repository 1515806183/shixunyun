#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_4 = "/examdata/result/httpd_deps"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_4):

                f.write("Linux软件安装与配置题目四:文件%s存在 ---ok\n" % linux_txt_4)

                cmd_cat = "cat %s|egrep '(chkconfig|apr|httpd-tools)'" % linux_txt_4
                com_ret_cat = commands.getoutput(cmd_cat).lower()

                if "chkconfig" in com_ret_cat or "apr" in com_ret_cat or "httpd-tools" in com_ret_cat:
                    f.write("Linux软件安装与配置题目四:输出正确 ---ok\n")
                else:
                    f.write("Linux软件安装与配置题目四:输出错误 ---error\n")

            else:
                f.write("LinuxLinux软件安装与配置题目四:文件%s不存在 ---error\n" % linux_txt_4)
                f.write("LinuxLinux软件安装与配置题目四:文件%s不存在,无法查询httpd依赖哪些包 ---error\n" % linux_txt_4)

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
