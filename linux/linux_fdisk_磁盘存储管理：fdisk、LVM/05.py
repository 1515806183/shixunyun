#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_5 = "/examdata/result/mountpoint_system_type"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_5):
                f.write("Linux磁盘存储管理题目五:文件%s存在 ---ok\n" % linux_txt_5)
                cmd_cat_ext4 = "cat /examdata/result/mountpoint_system_type|grep ext4"
                com_ret_cat_ext4 = commands.getoutput(cmd_cat_ext4).lower()

                cmd_cat_tmpfs = "cat /examdata/result/mountpoint_system_type|grep tmpfs"
                com_ret_cat_tmpfs = commands.getoutput(cmd_cat_tmpfs).lower()

                cmd_cat_iso = "cat /examdata/result/mountpoint_system_type|grep iso9660"
                com_ret_cat_iso = commands.getoutput(cmd_cat_iso).lower()

                if "ext4" in com_ret_cat_ext4 and "tmpfs" in com_ret_cat_tmpfs and "iso9660" in com_ret_cat_iso:
                    f.write("Linux磁盘存储管理题目五:过滤出ext4 tmpfs iso9660 ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目五:没有过滤出ext4 tmpfs iso9660 ---error\n")

            else:
                f.write("Linux磁盘存储管理题目五:文件%s不存在 ---error\n" % linux_txt_5)
                f.write("Linux磁盘存储管理题目五:文件%s不存在,无法过滤出ext4 tmpfs iso9660 ---error\n" % linux_txt_5)

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
