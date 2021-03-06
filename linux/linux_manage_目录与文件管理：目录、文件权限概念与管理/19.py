#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/user08.sh"
    
    
    def run():
        try:
            f = open(save_address, 'w')
    
            cmd_cat = "cat /etc/passwd | grep '^stu' | awk -F ':' '{print $1}'"
            com_ret_cat = commands.getoutput(cmd_cat)
            if com_ret_cat:
                com_ret_cat = com_ret_cat.split('\n')
                if len(com_ret_cat) == 10:
                    f.write("Linux目录与文件管理题目十九:文件%s,用户stu01-stu10存在 ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目十九:文件%s,用户stu01-stu10不存在 ---error\n" % name)
            else:
                f.write("Linux目录与文件管理题目十九:文件%s,用户stu01-stu10不存在 ---error\n" % name)
    
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

