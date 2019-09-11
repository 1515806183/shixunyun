#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    name = "/examdata/result/"
    name1 = "/examdata/result/file_right"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd_dir = "ls -l %s | grep rwxrwxrwt --color=auto " % name
            com_ret = commands.getoutput(cmd_dir)

            if "rwxrwxrwt" in com_ret:
                f.write("Linux目录与文件管理题目七:/examdata/result目录的权限为1777, ---ok\n")

                if os.path.exists(name1):
                    f.write("Linux目录与文件管理题目七:文件%s存在, ---ok\n" % name1)

                else:
                    f.write("Linux目录与文件管理题目七:文件%s不存在, ---error\n" % name1)

            else:
                f.write("Linux目录与文件管理题目七:/examdata/result目录的权限不为1777, ---error\n")
                f.write("Linux目录与文件管理题目七:文件%s不存在 ---error\n" % name1)

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
