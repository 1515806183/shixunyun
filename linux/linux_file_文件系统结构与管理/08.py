#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    name = "/examdata/result/html"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux文件系统结构与管理题目八:文件%s存在 ---ok\n" % name)

                cmd_find = "ls -Zld %s|grep 'httpd_sys_content_t'" % name
                com_ret_find = commands.getoutput(cmd_find).lower()

                if "httpd_sys_content_t" in com_ret_find:
                    f.write("Linux文件系统结构与管理题目八:过滤出httpd_sys_content_t ---ok\n")
                else:
                    f.write("Linux文件系统结构与管理题目八:没有过滤出httpd_sys_content_t ---error\n")

            else:
                f.write("Linux文件系统结构与管理题目八:文件%s不存在 ---error\n" % name)
                f.write("Linux文件系统结构与管理题目八:文件%s不存在,无法过滤httpd_sys_content_t ---error\n" % name)

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
