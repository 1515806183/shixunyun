#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_11 = "/examdata/result/file_use_as_disk"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd_ext4 = "df -hT|grep '/examdata/result/file_use_as_disk' | grep ext4"
            com_ret_ext4 = commands.getoutput(cmd_ext4).lower()

            if "ext4" in com_ret_ext4:
                f.write("Linux磁盘存储管理题目十一:grep ext4成功 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十一:grep ext4错误 ---error\n")

            # 2
            cmd_file = "df | grep '/examdata/result/file_use_as_disk' | awk '{print $1}'"
            com_ret_file = commands.getoutput(cmd_file)
            cmd = "file %s | grep 'huge files'" % com_ret_file
            cmd_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "hugefiles" in cmd_ret:
                f.write("Linux磁盘存储管理题目十一:grep huge files成功 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十一:grep huge files错误 ---error\n")

            # 3
            cmd_du = "df |grep /examdata/result/file_use_as_disk | awk '{print $1}'"
            com_ret_du = commands.getoutput(cmd_du)
            cmd_du = "du -sh %s |awk '{print $1}'|sed 's/[Mm]//g'" % com_ret_du
            com_ret_du = commands.getoutput(cmd_du)

            if "100" in com_ret_du or "101" in com_ret_du:
                f.write("Linux磁盘存储管理题目十一:输出结果为%s ---ok\n" % com_ret_du)
            else:
                f.write("Linux磁盘存储管理题目十一:输出结果为%s ---error\n" % com_ret_du)

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
