#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/training/wenjian.sh"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux性能诊断与调优题目一:文件%s存在 ---ok\n" % name)
                # 1
                cmd_ll = "ls -l /examdata/training/wenjian.sh |grep -E '(-rwxrwxr--)'"
                com_ret_ll = commands.getoutput(cmd_ll)
                if com_ret_ll:
                    f.write("Linux目录与文件管理题目一:文件%s其权限属性为-rwxrwxr-- ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目一:文件%s其权限属性不为-rwxrwxr-- ---error\n" % name)

            else:
                f.write("Linux目录与文件管理题目一:文件%s不存在 ---error\n" % name)
                f.write("Linux目录与文件管理题目一:文件%s不存在,无法查询文件属性 ---error\n" % name)

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

