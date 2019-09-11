#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_1 = "/examdata/result/lvm_info"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_1):
                f.write("Linux磁盘存储管理题目一:文件%s存在 ---ok\n" % linux_txt_1)

                # 1
                cmd_PV_1 = "cat %s|egrep '(vda2|vdc)' --color=auto" % linux_txt_1
                com_ret_PV_1 = commands.getoutput(cmd_PV_1)
                if "vda2" in com_ret_PV_1 or "vdc" in com_ret_PV_1:
                    f.write("Linux磁盘存储管理题目一:文件%s包含vda2或vdc ---ok\n" % linux_txt_1)
                else:
                    f.write("Linux磁盘存储管理题目一:文件%s不包含vda2或vdc ---error\n" % linux_txt_1)

                # 2
                cmd_LV_1 = "cat %s| egrep 'lv_root|lv_swap'--color=auto" % linux_txt_1
                com_ret_LV_1 = commands.getoutput(cmd_LV_1)

                if "lv_root" in com_ret_LV_1 or "lv_swap" in com_ret_LV_1:
                    f.write("Linux磁盘存储管理题目一:文件%s包含lv_root或lv_swap ---ok\n" % linux_txt_1)
                else:
                    f.write("Linux磁盘存储管理题目一:文件%s不包含lv_root或lv_swap ---error\n" % linux_txt_1)

                # 3
                cmd_VG_1 = "cat %s| grep rhel65trainin" % linux_txt_1
                com_ret_VG_1 = commands.getoutput(cmd_VG_1).lower().replace(" ", "")
                if "rhel65trainin" in com_ret_VG_1:
                    f.write("Linux磁盘存储管理题目一:文件%s包含vg_rhe或65trainin ---ok\n" % linux_txt_1)
                else:
                    f.write("Linux磁盘存储管理题目一:文件%s不包含vg_rhe或65trainin ---error\n" % linux_txt_1)

            else:

                f.write("Linux磁盘存储管理题目一:文件%s不存在 ---error\n" % linux_txt_1)
                f.write("Linux磁盘存储管理题目一:文件%s不存在,无法查询vda2或vdc ---error\n" % linux_txt_1)
                f.write("Linux磁盘存储管理题目一:文件%s不存在,无法查询lv_root或lv_swap ---error\n" % linux_txt_1)
                f.write("Linux磁盘存储管理题目一:文件%s不存在,无法查询vg_rhe或65trainin ---error\n" % linux_txt_1)

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
