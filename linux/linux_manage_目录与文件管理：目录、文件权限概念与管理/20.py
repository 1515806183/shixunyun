#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/num_users"
    
    
    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux目录与文件管理题目二十:文件%s存在 ---ok\n" % name)
                cmd_grep = "grep -v 'nologin' /etc/passwd|awk -F ':' '{print $1}' | wc -l"
                com_ret_grep = int(commands.getoutput(cmd_grep))
                cmd_cat = "cat %s | wc -l" % name
                com_ret_cat = int(commands.getoutput(cmd_cat))
    
                if com_ret_grep == com_ret_cat:
                    f.write("Linux目录与文件管理题目二十:系统上允许登陆的用户有 %s个,与输出文件%s内容一致 ---ok\n" % (com_ret_grep, name))
                else:
                    f.write("Linux目录与文件管理题目二十:系统上允许登陆的用户有 %s个,与输出文件%s内容不一致 ---error\n" % (com_ret_grep, name))
    
    
            else:
                f.write("Linux目录与文件管理题目二十:文件%s不存在 ---error\n" % name)
                f.write("Linux目录与文件管理题目二十:文件%s不存在, 无法对比查询内容 ---error\n" % name)
    
    
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

