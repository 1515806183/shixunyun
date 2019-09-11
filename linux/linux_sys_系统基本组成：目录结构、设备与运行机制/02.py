#!/usr/bin/python
# -*- coding: utf-8 -*-
    
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    save_test = "/tmp/test.txt"
    
    name = "/examdata/result/mem0.txt"
    
    
    def run():
        try:
            cmd_1 = "free -m"
            com_ret_1 = commands.getoutput(cmd_1)
            with open(save_test, 'w') as f:
                f.write(com_ret_1 + '\n')
    
            cmd = "cat %s | awk '{ if (NR==2||NR==3) print$3,$4}'" % name
            com_ret = commands.getoutput(cmd)
            com_ret_list = re.findall(r'\d+', com_ret)
    
            cmd_test = "cat %s | awk '{ if (NR==2||NR==3) print$3,$4}'" % save_test
            com_ret_test = commands.getoutput(cmd_test)
            com_ret_test_list = re.findall(r'\d+', com_ret_test)
    
            diff_num = True
            for index, value in enumerate(com_ret_list):
                ret_num = abs(int(com_ret_test_list[index]) - int(value))
                if ret_num > 20:
                    diff_num = False
    
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("LINUX系统基本组成题目二:文件%s存在 ---ok\n" % name)
                if diff_num:
                    f.write("LINUX系统基本组成题目二:对比文件内容%s的输出一致 ---ok\n" % name)
    
                else:
                    f.write("LINUX系统基本组成题目二:对比文件内容%s的输出不一致 ---error\n" % name)
            else:
                f.write("LINUX系统基本组成题目二:文件%s不存在 ---error\n" % name)
                f.write("LINUX系统基本组成题目二:文件%s不存在,无法进行过滤对比 ---error\n" % name)
    
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
    
