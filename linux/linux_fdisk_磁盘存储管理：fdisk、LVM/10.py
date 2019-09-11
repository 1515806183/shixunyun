#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd_raid0 = "cat /proc/mdstat |grep md0|grep vdb1|grep vdb2"
            com_ret_raid0 = commands.getoutput(cmd_raid0)

            if "vdb2" in com_ret_raid0.lower():
                f.write("Linux磁盘存储管理题目十:检查raid0 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十:检查raid0 ---error\n")

            # 2
            cmd_raid1 = "cat /proc/mdstat |grep md1|grep vdb3|grep vdb4"
            com_ret_raid1 = commands.getoutput(cmd_raid1)

            if "vdb4" in com_ret_raid1.lower():
                f.write("Linux磁盘存储管理题目十:检查raid1 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十:检查raid1 ---error\n")

            # 3
            cmd_md0 = "df -T |grep /examdata/dir_raid0|grep '/dev/md0'|grep ext3"
            com_ret_md0 = commands.getoutput(cmd_md0)

            if "ext3" in com_ret_md0.lower():
                f.write("Linux磁盘存储管理题目十:检查dir_raid0,ext3 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十:检查dir_raid0, ext3 ---error\n")

            # 4
            cmd_md1 = "df -T |grep /examdata/dir_raid1|grep '/dev/md1'|grep ext3"
            com_ret_md1 = commands.getoutput(cmd_md1)

            if "ext3" in com_ret_md1.lower():
                f.write("Linux磁盘存储管理题目十:检查dir_raid1,ext3 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十:检查dir_raid1, ext3 ---error\n")

            # 5
            cmd_dir_raid0 = "cat /etc/fstab|egrep '/dev/md0[[:space:]]+/examdata/dir_raid0[[:space:]]+ext3'"
            com_ret_dir_raid0 = commands.getoutput(cmd_dir_raid0).lower()

            if "/dev/md0" in com_ret_dir_raid0 and "/examdata/dir_raid0" in com_ret_dir_raid0 and "ext3" in cmd_dir_raid0:
                f.write("Linux磁盘存储管理题目十:检查/dev/md0/examdata/dir_raid0/ext3 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十:检查/dev/md0/examdata/dir_raid0/ext3 ---error\n")

            # 6
            cmd_dir_raid1 = "cat /etc/fstab|egrep '/dev/md1[[:space:]]+/examdata/dir_raid1[[:space:]]+ext3'"
            com_ret_dir_raid1 = commands.getoutput(cmd_dir_raid1)

            if "/dev/md1" in com_ret_dir_raid1 and "/examdata/dir_raid1" in com_ret_dir_raid1 and "ext3" in com_ret_dir_raid1:
                f.write("Linux磁盘存储管理题目十:检查/dev/md1/examdata/dir_raid1/ext3 ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目十:检查/dev/md1/examdata/dir_raid1/ext3 ---error\n")

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
