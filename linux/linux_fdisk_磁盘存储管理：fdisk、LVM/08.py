#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'


    def run():
        try:
            f = open(save_address, 'w')
            cmd_swapon = "swapon -s|grep file|awk '{print $1}'"
            com_ret_swapon = commands.getoutput(cmd_swapon)

            if "file" in com_ret_swapon.lower():
                f.write("Linux磁盘存储管理题目八:检查swap挂载过滤出信息file, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目八:检查swap挂载没有过滤出信息file ---error\n")

            cmd_awk = "swapon -s|grep file|awk '{print $1}'"
            com_ret_awk = commands.getoutput(cmd_awk)

            if com_ret_awk:
                cmd_du = "du -sh " + com_ret_awk + " | grep 200M"
                print cmd_du
                com_ret_du = commands.getoutput(cmd_du)
                com_ret_du = re.search(r'\d+', com_ret_du).group()

                if "200" in com_ret_du:
                    f.write("Linux磁盘存储管理题目八:检查swap的大小输出为200 ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目八:检查swap的大小输出不为200 ---error\n")
            else:
                f.write("Linux磁盘存储管理题目八:检查swap的大小输出不为200, ---error\n")

            cmd_cat = "cat /etc/fstab | egrep swap | grep -v '/dev/mapper'"
            com_ret_cat = commands.getoutput(cmd_cat)
            if com_ret_cat:
                f.write("Linux磁盘存储管理题目八:检查开机启动输出为/dev/mapper ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目八:检查开机启动输出不为/dev/mapper ---error\n")

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
                print i.strip('\n').split(':')[1]

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
