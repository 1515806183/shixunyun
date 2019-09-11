#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    name = "/testdata1/result/newhelloworld.txt"
    name_2 = "/examdata/result/helloworld.backup"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux文件系统结构与管理题目四:文件%s存在 ---ok\n" % name)

                # 1
                cmd_VM = "grep VMware %s" % name
                com_ret_VM = commands.getoutput(cmd_VM).lower()
                if "VMware".lower() in com_ret_VM:
                    f.write("Linux文件系统结构与管理题目四:grep到VMware ---error\n")
                else:
                    f.write("Linux文件系统结构与管理题目四:没有grep到VMware ---ok\n")

                # 2
                cmd_xing = "grep '\*\*\*' %s" % name
                com_ret_xing = commands.getoutput(cmd_xing)
                if "***" in com_ret_xing:
                    f.write("Linux文件系统结构与管理题目四:grep到*** ---ok\n")
                else:
                    f.write("Linux文件系统结构与管理题目四:没有grep到*** ---error\n")

                # 3
                cmd_tools = "grep -i 'Tools' %s" % name
                com_ret_tools = commands.getoutput(cmd_tools).lower()
                if "tools" in com_ret_tools:
                    f.write("Linux文件系统结构与管理题目四:grep到 tools ---error\n")
                else:
                    f.write("Linux文件系统结构与管理题目四:没有grep到 tools ---ok\n")

                # 4
                cmd_head = "head -n 30 %s|grep '[[:upper:]]'" % name
                com_ret_head = commands.getoutput(cmd_head)
                if com_ret_head == "":
                    f.write("Linux文件系统结构与管理题目四:前30行没有大写 ---ok\n")
                else:
                    f.write("Linux文件系统结构与管理题目四:前30行有大写 ---error\n")

                # 5
                if os.path.exists(name_2):
                    f.write("Linux文件系统结构与管理题目四:文件%s存在 ---ok\n" % name_2)
                else:
                    f.write("Linux文件系统结构与管理题目四:文件%s不存在 ---error\n" % name_2)

            else:
                f.write("Linux文件系统结构与管理题目四:文件%s不存在 ---error\n" % name)
                f.write("Linux文件系统结构与管理题目四:文件%s不存在,根据题意取错误答案,grep到VMware ---error\n" % name)
                f.write("Linux文件系统结构与管理题目四:文件%s不存在,根据题意取错误答案,没有grep到*** ---error\n" % name)
                f.write("Linux文件系统结构与管理题目四:文件%s不存在,根据题意取错误答案,grep到 tools ---error\n" % name)
                f.write("Linux文件系统结构与管理题目四:文件%s不存在,根据题意取错误答案,前30行有大写 ---error\n" % name)
                f.write("Linux文件系统结构与管理题目四:文件%s不存在,根据题意取错误答案,没有文件%s, ---error\n" % (name, name_2))

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

