#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/new_messages/empty1"
    name1 = '/var/log/messages'
    
    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux目录与文件管理题目十一:文件%s存在 ---ok\n" % name)
                # 1
                cmd_messages = "ls -l /tmp/empty1 |  awk '{print $9 $10  $11}'"
                com_ret_messages = commands.getoutput(cmd_messages)
                if '/tmp/empty1->/examdata/result/new_messages/empty1' in com_ret_messages:
                    f.write("Linux目录与文件管理题目十一:软链接到/tmp目录下成功 ---ok\n")
    
                else:
                    f.write("Linux目录与文件管理题目十一:软链接到/tmp目录下失败 ---error\n")
    
                # 2
                cmd_empty = "ls -ld %s | awk '{print $3, $4}'" % name
                com_ret_empty = commands.getoutput(cmd_empty).lower().replace(" ", "")
    
                cmd_log = "ls -ld %s | awk '{print $3, $4}'" % name1
                com_ret_log = commands.getoutput(cmd_log).lower().replace(" ", "")
    
                if com_ret_log == com_ret_empty:
                    f.write("Linux目录与文件管理题目十一:文件%s组主和属组一致 ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目十一:文件%s组主和属组不一致 ---error\n" % name)
    
            else:
                f.write("Linux目录与文件管理题目十一:文件%s不存在 ---error\n" % name)
                f.write("Linux目录与文件管理题目十一:文件%s不存在,无法查看软连接 ---error\n" % name)
                f.write("Linux目录与文件管理题目十一:文件%s不存在,无法查看属组 ---error\n" % name)
    
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

