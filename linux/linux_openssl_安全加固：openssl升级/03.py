#!/usr/bin/python
# -*- coding: utf-8 -*-
    
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/check_file_modify"
    
    
    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("LINUX安全加固openssl升级题目三:文件%s存在 ---ok\n" % name)
    
                cmd_grep = "cat /examdata/result/check_file_modify | grep 'af_unix.conf: FAILED'"
                com_ret = commands.getoutput(cmd_grep).lower()
    
                if 'af_unix.conf' in com_ret and "failed" in com_ret:
                    f.write("LINUX安全加固openssl升级题目三:grep 'af_unix.conf FAILED'成功 ---ok\n")
                else:
                    f.write("LINUX安全加固openssl升级题目三:grep 'af_unix.conf FAILED'失败---error\n")
    
            else:
                f.write("LINUX安全加固openssl升级题目三:文件%s不存在 ---error\n" % name)
                f.write("LINUX安全加固openssl升级题目三:文件%s不存在,grep 'af_unix.conf FAILED'失败 ---error\n" % name)
    
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
    
