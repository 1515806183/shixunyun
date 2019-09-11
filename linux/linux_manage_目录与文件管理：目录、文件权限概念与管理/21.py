#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/fstab.bak"
    
    
    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("Linux目录与文件管理题目二十一:文件%s存在 ---ok\n" % name)
                # 1
                cmd_diff = "diff /etc/fstab %s" % name
                com_ret_grep = commands.getoutput(cmd_diff)
                if com_ret_grep == "":
                    f.write("Linux目录与文件管理题目二十一:文件%s内容和/etc/fstab一致 ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目二十一:文件%s内容和/etc/fstab不一致 ---error\n" % name)
    
                # 2
                cmd_ll = "ls -l /examdata/result/fstab.bak| awk '{print $4}'"
                com_ret_ll = commands.getoutput(cmd_ll).lower()
    
                if "manager" in com_ret_ll:
                    f.write("Linux目录与文件管理题目二十一:文件%s属组输出内容为manager ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目二十一:文件%s属组输出内容不为manager ---error\n" % name)
    
                # 3
                cmd_harry = "getfacl %s|egrep '(harry|natasha|other)'" % name
                com_ret_harry = commands.getoutput(cmd_harry).replace(' ','')
    
                if "other::r--" in com_ret_harry and "user:natasha:---" in com_ret_harry and "user:harry:rw-" in com_ret_harry:
                    f.write("Linux目录与文件管理题目二十一:检查harry natasha及其他用户的权限设置正确 ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目二十一:检查harry natasha及其他用户的权限设置错误 ---error\n")
    
            else:
                f.write("Linux目录与文件管理题目二十一:文件%s不存在 ---error\n" % name)
                f.write("Linux目录与文件管理题目二十一:文件%s不存在, 文件%s内容和/etc/fstab无法比较 ---error\n" % (name, name))
                f.write("Linux目录与文件管理题目二十一:文件%s不存在, 文件%s属组输出内容无法比较 ---error\n" % (name, name))
                f.write("Linux目录与文件管理题目二十一:文件%s不存在, harry natasha及其他用户的权限设置无法检查 ---error\n" % name)
    
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

