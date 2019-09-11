#!/usr/bin/python
# -*- coding: utf-8 -*-
    
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/version.txt"
    
    
    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("LINUX系统基本组成题目一:文件%s存在 ---ok\n" % name)
    
                cmd_1 = "cat /etc/redhat-release"
                com_ret_1 = commands.getoutput(cmd_1)
                cmd_2 = "uname -a"
                com_ret_2 = commands.getoutput(cmd_2)
                cmd_3 = 'cat %s' % name
                com_ret_3 = commands.getoutput(cmd_3)
                if com_ret_1 in com_ret_3 and com_ret_2 in com_ret_3:
                    f.write("LINUX系统基本组成题目一:对比文件内容%s的输出一致 ---ok\n" % name)
    
                else:
                    f.write("LINUX系统基本组成题目一:对比文件内容%s的输出不一致 ---error\n" % name)
    
            else:
                f.write("LINUX系统基本组成题目一:文件%s不存在 ---error\n" % name)
                f.write("LINUX系统基本组成题目一:文件%s不存在,无法进行过滤对比 ---error\n" % name)
    
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
    
