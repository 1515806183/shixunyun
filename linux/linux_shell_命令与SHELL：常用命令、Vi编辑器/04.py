#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_4 = "/examdata/result/function.sh"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_4):

                f.write("Linux命令与SHELL题目四:文件%s存在 ---ok\n" % linux_txt_4)

                # 1
                cmd_egrep = "egrep .*\(\) %s" % linux_txt_4
                com_ret_egrep = commands.getoutput(cmd_egrep)

                if com_ret_egrep == '':
                    f.write("Linux命令与SHELL题目四:egrep .*\(\)失败 ---error\n")
                else:
                    f.write("Linux命令与SHELL题目四:egrep .*\(\)成功 ---ok\n")

                # 2
                cmd_cat = "cat  /examdata/result/function.sh|egrep '(\$1|\$2)'"
                com_ret_cat = commands.getoutput(cmd_cat).lower()

                if "$1" in com_ret_cat and "$2" in com_ret_cat:
                    f.write("Linux命令与SHELL题目四:过滤$1,$2成功 ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目四:过滤$1,$2失败 ---error\n")

                # 3
                cmd_cat = "cat  /examdata/result/function.sh|egrep  '(51|52)'"
                com_ret_cat = commands.getoutput(cmd_cat).lower()

                if 'return' in com_ret_cat:
                    f.write("Linux命令与SHELL题目四:过滤return成功 ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目四:过滤return失败 ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux命令与SHELL题目四:文件%s不存在 ---error\n" % linux_txt_4)
                    f.write("Linux命令与SHELL题目四:文件%s不存在,egrep .*\(\)失败 ---error\n" % linux_txt_4)
                    f.write("Linux命令与SHELL题目四:文件%s不存在,过滤$1,$2失败 ---error\n" % linux_txt_4)
                    f.write("Linux命令与SHELL题目四:文件%s不存在,过滤return失败 ---error\n" % linux_txt_4)

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
