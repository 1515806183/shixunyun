# coding=utf-8

import commands
import os
import re


# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/lvm_info"
linux_txt_3_1 = "/examdata/result/lvm_config_file"
linux_txt_3_2 = "/etc/lvm/lvm.conf"
linux_txt_4_1 = "/examdata/result/mountpoint_size"
linux_txt_4_2 = "/examdata/result/exam_lvm"
linux_txt_5 = "/examdata/result/mountpoint_system_type"
linux_txt_6 = "/examdata/result/extend.log"
linux_txt_9 = "/dev/raw/raw1"
linux_txt_11 = "/examdata/result/file_use_as_disk"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux磁盘存储管理题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_PV_1 = "cat |egrep '(vda2|vdc)'--color=auto"
                com_ret_PV_1 = commands.getoutput(cmd_PV_1)

                cmd_PV_2 = "cat /examdata/result/lvm_info|egrep '(vda2 | vdc)' --color=auto"
                com_ret_PV_2 = commands.getoutput(cmd_PV_2)

                with open(save_address, "a+") as f:
                    if "vda2--color=auto" in com_ret_PV_1 or "vdc--color=auto" in com_ret_PV_1 or "vda2 --color=auto" in com_ret_PV_2 or "vdc --color=auto" in com_ret_PV_2:
                        f.write("Linux磁盘存储管理题目一：包含'(vda2|vdc)'--color=auto, ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目一：不包含'(vda2|vdc)'--color=auto, ---error\n")

                cmd_LV_1 = "cat /examdata/result/lvm_info| egrep 'lv_root | lv_swap'--color=auto"
                com_ret_LV_1 = commands.getoutput(cmd_LV_1)

                cmd_LV_2 = "cat /examdata/result/lvm_info| egrep 'lv_root | lv_swap' --color=auto"
                com_ret_LV_2 = commands.getoutput(cmd_LV_2)

                with open(save_address, "a+") as f:
                    if "lv_root--color=auto" in com_ret_LV_1 or "lv_swap--color=auto" in com_ret_LV_1 or "lv_root --color=auto" in com_ret_LV_2 or "lv_swap --color=auto" in com_ret_LV_2:
                        f.write("Linux磁盘存储管理题目一：包含'lv_root|lv_swap'--color=auto, ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目一：不包含'lv_root|lv_swap'--color=auto, ---error\n")

                cmd_VG_1 = "cat /examdata/result/lvm_info| grep 'vg_rhe | 65trainin' --color=auto"
                com_ret_VG_1 = commands.getoutput(cmd_VG_1)

                cmd_VG_2 = "cat /examdata/result/lvm_info| grep 'vg_rhe | 65trainin' --color=auto"
                com_ret_VG_2 = commands.getoutput(cmd_VG_2)

                with open(save_address, "a+") as f:
                    if "vg_rhe--color=auto" in com_ret_VG_1 or "65trainin--color=auto" in com_ret_VG_1 or "vg_rhe --color=auto" in com_ret_VG_2 or "65trainin --color=auto" in com_ret_VG_2:
                        f.write("Linux磁盘存储管理题目一：包含'lv_root|lv_swap'--color=auto, ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目一：不包含'lv_root|lv_swap'--color=auto, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux磁盘存储管理题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux磁盘存储管理题目一:失败")

        else:
            print("Linux磁盘存储管理题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            cmd_lv = "df -hTP|grep '/examdata/result/exam_lvm'"
            com_ret_lv = commands.getoutput(cmd_lv)

            with open(save_address, "a+") as f:
                if "/examdata/result/exam_lvm" in com_ret_lv:
                    f.write("Linux磁盘存储管理题目二：检查lv被挂载, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目二：检查lv没有被挂载, ---error\n")

            cmd_lv = "df -hTP /|awk 'NR>1 {print $3}'|sed 's/[M|m]//g'"
            com_ret_lv = commands.getoutput(cmd_lv)

            com_ret_num = int(com_ret_lv[:-1])

            with open(save_address, "a+") as f:
                if 100 < com_ret_num < 150:
                    f.write("Linux磁盘存储管理题目二：检查LV的大小正确, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目二：检查LV的大小错误, ---error\n")

        except:
            print("Linux磁盘存储管理题目二:失败")

        else:
            print("Linux磁盘存储管理题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_3_1):
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目三：文件%s存在, ---ok\n" % linux_txt_3_1)

                if os.path.exists(linux_txt_3_2):
                    with open(save_address, "a+") as f:
                        f.write("Linux磁盘存储管理题目三：文件%s存在, ---ok\n" % linux_txt_3_2)

                    cmd_diff = "diff /examdata/result/lvm_config_file  /etc/lvm/lvm.conf"
                    com_ret_diff = commands.getoutput(cmd_diff)

                    with open(save_address, "a+") as f:
                        if com_ret_diff == "":
                            f.write("Linux磁盘存储管理题目三：备份lvm配置文件内容一致, ---ok\n")
                        else:
                            f.write("Linux磁盘存储管理题目三：备份lvm配置文件内容不一致, ---error\n")

                else:
                    with open(save_address, "a+") as f:
                        f.write("Linux磁盘存储管理题目三：文件%s不存在, ---error\n" % linux_txt_3_2)

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目三：文件%s不存在, ---error\n" % linux_txt_3_1)

        except:
            print("Linux磁盘存储管理题目三:失败")

        else:
            print("Linux磁盘存储管理题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_4_1):
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目四：文件%s存在, ---ok\n" % linux_txt_3_1)

                if os.path.exists(linux_txt_4_2):

                    cmd_hTP = "diff /examdata/result/lvm_config_file  /etc/lvm/lvm.conf"
                    com_ret_hTP = commands.getoutput(cmd_hTP)
                    htp_list = str(com_ret_hTP).split()
                    htp_1 = htp_list[0]
                    htp_2 = htp_list[1]

                    cmd_dev = "diff /examdata/result/lvm_config_file  /etc/lvm/lvm.conf"
                    com_ret_dev = commands.getoutput(cmd_dev)
                    dev_list = str(com_ret_dev).split()
                    dev_1 = dev_list[0]
                    dev_2 = dev_list[1]

                    cmd_boot = "diff /examdata/result/lvm_config_file  /etc/lvm/lvm.conf"
                    com_ret_boot = commands.getoutput(cmd_boot)
                    boot_list = str(com_ret_boot).split()
                    boot_1 = boot_list[0]
                    boot_2 = boot_list[1]

                    cmd_exam_lvm = "diff /examdata/result/lvm_config_file  /etc/lvm/lvm.conf"
                    com_ret_exam_lvm = commands.getoutput(cmd_exam_lvm)
                    exam_lvm_list = str(com_ret_exam_lvm).split()
                    exam_lvm_1 = exam_lvm_list[0]
                    exam_lvm_2 = exam_lvm_list[1]

                    cmd_cat = "cat /examdata/result/mountpoint_size"
                    com_ret_cat = commands.getoutput(cmd_cat)

                    with open(save_address, "a+") as f:
                        if htp_1 in com_ret_cat and htp_2 in com_ret_cat and dev_1 in com_ret_cat and dev_2 in com_ret_cat and boot_1 in com_ret_cat and boot_2 in com_ret_cat and exam_lvm_1 in com_ret_cat and exam_lvm_2 in com_ret_cat:
                            f.write("Linux磁盘存储管理题目四：系统各挂载点的容量内容一致, ---ok\n")
                        else:
                            f.write("Linux磁盘存储管理题目四：系统各挂载点的容量内容不一致, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目四：文件%s不存在, ---error\n" % linux_txt_3_1)

        except:
            print("Linux磁盘存储管理题目四:失败")

        else:
            print("Linux磁盘存储管理题目四:成功")


class Cat_score_5(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_5):
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目五：文件%s存在, ---ok\n" % linux_txt_5)

                cmd_cat_ext4 = "cat /examdata/result/mountpoint_system_type|grep ext4"
                com_ret_cat_ext4 = commands.getoutput(cmd_cat_ext4)

                cmd_cat_tmpfs = "cat /examdata/result/mountpoint_system_type|grep tmpfs"
                com_ret_cat_tmpfs = commands.getoutput(cmd_cat_tmpfs)

                cmd_cat_iso = "cat /examdata/result/mountpoint_system_type|grep iso9660"
                com_ret_cat_iso = commands.getoutput(cmd_cat_iso)

                with open(save_address, "a+") as f:
                    if "ext4" in com_ret_cat_ext4 and "tmpfs" in com_ret_cat_tmpfs and "iso9660" in com_ret_cat_iso:
                        f.write("Linux磁盘存储管理题目五：过滤出ext4 tmpfs iso9660 , ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目五：没有过滤出ext4 tmpfs iso9660, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目五：文件%s不存在, ---error\n" % linux_txt_5)

        except:
            print("Linux磁盘存储管理题目五:失败")

        else:
            print("Linux磁盘存储管理题目五:成功")


class Cat_score_6(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_6):
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目六：文件%s存在, ---ok\n" % linux_txt_6)

                cmd_df = "df -hT /|sed 's/[GgMm]//g'"
                com_ret_df = commands.getoutput(cmd_df)

                int_cat = int(str(com_ret_df).strip())

                cmd_cat = "cat /examdata/result/extend.log"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if 37.9 < int_cat < 38.1:
                        f.write("Linux磁盘存储管理题目六：检查根目录的空间大小为%s, ---ok\n" % int_cat)
                    else:
                        f.write("Linux磁盘存储管理题目六：检查根目录的空间大小为%s, ---error\n" % int_cat)

                with open(save_address, "a+") as f:
                    if str(int_cat) in com_ret_cat:
                        f.write("Linux磁盘存储管理题目六：对比输出的结果正确, ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目六：对比输出的结果错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目六：文件%s不存在, ---error\n" % linux_txt_6)

        except:
            print("Linux磁盘存储管理题目六:失败")

        else:
            print("Linux磁盘存储管理题目六:成功")


class Cat_score_7(object):

    @staticmethod
    def run():
        try:
            cmd_df = "df|grep ext3|grep '/test'"
            com_ret_df = commands.getoutput(cmd_df)

            with open(save_address, "a+") as f:
                if "/test" in com_ret_df or "test" in com_ret_df:
                    f.write("Linux磁盘存储管理题目七：过滤出信息/test, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目七：没有过滤出信息/test, ---error\n")

        except:
            print("Linux磁盘存储管理题目七:失败")

        else:
            print("Linux磁盘存储管理题目七:成功")


class Cat_score_8(object):

    @staticmethod
    def run():
        try:
            cmd_swapon = "swapon -s|grep -v dev|awk 'NR>1 {print $2}'"
            com_ret_swapon = commands.getoutput(cmd_swapon)

            with open(save_address, "a+") as f:
                if "file" in com_ret_swapon:
                    f.write("Linux磁盘存储管理题目八：检查swap挂载过滤出信息file, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目八：检查swap挂载没有过滤出信息file, ---error\n")

            cmd_awk = "swapon -s|grep file|awk '{print $1}'"
            com_ret_awk = commands.getoutput(cmd_awk)

            cmd_du = "du -sh " + com_ret_awk
            com_ret_du = commands.getoutput(cmd_du)

            with open(save_address, "a+") as f:
                if "200" in com_ret_du or "201" in com_ret_du:
                    f.write("Linux磁盘存储管理题目八：检查swap的大小输出为200或201, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目八：检查swap的大小输出不为200或201, ---error\n")

            cmd_cat = "cat /etc/fstab | egrep swap | grep -v '/dev/mapper'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if "/dev/mapper" in com_ret_cat:
                    f.write("Linux磁盘存储管理题目八：检查开机启动输出为/dev/mapper, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目八：检查开机启动输出不为/dev/mapper, ---error\n")

        except:
            print("Linux磁盘存储管理题目八:失败")

        else:
            print("Linux磁盘存储管理题目八:成功")


class Cat_score_9(object):

    @staticmethod
    def run():
        try:
            cmd_ls = "ls /dev/raw/raw｛1..4}"
            com_ret_ls = commands.getoutput(cmd_ls)

            with open(save_address, "a+") as f:
                if "ls:" in com_ret_ls and "on" in com_ret_ls:
                    f.write("Linux磁盘存储管理题目九：查看raw[1-4]错误, ---error\n")
                else:
                    f.write("Linux磁盘存储管理题目九：查看raw[1-4]正确, ---ok\n")

            if os.path.exists(linux_txt_9):
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目九：文件%s存在, ---ok\n" % linux_txt_9)

                cmd_ll = "ll /dev/raw/raw1|grep oracle|grep oinstall"
                com_ret_ll = commands.getoutput(cmd_ll)

                with open(save_address, "a+") as f:
                    if "oinstall" in com_ret_ll:
                        f.write("Linux磁盘存储管理题目九：grep 到oinstall正确, ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目九：没有grep 到oinstall错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux磁盘存储管理题目九文件%s不存在, ---error\n" % linux_txt_9)


        except:
            print("Linux磁盘存储管理题目九:失败")

        else:
            print("Linux磁盘存储管理题目九:成功")


class Cat_score_10(object):

    @staticmethod
    def run():
        try:
            cmd_raid0 = "cat /proc/mdstat |grep md0|grep vdb1|grep vdb2"
            com_ret_raid0 = commands.getoutput(cmd_raid0)

            cmd_raid1 = "cat /proc/mdstat |grep md1|grep vdb3|grep vdb4"
            com_ret_raid1 = commands.getoutput(cmd_raid1)

            cmd_md0 = "df -T |grep /examdata/dir_raid0|grep '/dev/md0'|grep ext3"
            com_ret_md0 = commands.getoutput(cmd_md0)

            cmd_md1 = "df -T |grep /examdata/dir_raid1|grep '/dev/md1'|grep ext3"
            com_ret_md1 = commands.getoutput(cmd_md1)

            cmd_dir_raid0 = "cat /etc/fstab|egrep '/dev/md0[[:space:]]+/examdata/dir_raid0[[:space:]]+ext3'"
            com_ret_dir_raid0 = commands.getoutput(cmd_dir_raid0)

            cmd_dir_raid1 = "cat /etc/fstab|egrep '/dev/md1[[:space:]]+/examdata/dir_raid1[[:space:]]+ext3'"
            com_ret_dir_raid1 = commands.getoutput(cmd_dir_raid1)

            with open(save_address, "a+") as f:
                if "vdb2" in com_ret_raid0 and "vdb4" in com_ret_raid1 and "ext3" in com_ret_md0 and "ext3" in com_ret_md1:
                    if "/dev/md0" in com_ret_dir_raid0 and "/examdata/dir_raid0" in com_ret_dir_raid0 and "ext3" in com_ret_dir_raid0:
                        if "/dev/md1" in com_ret_dir_raid1 and "/examdata/dir_raid1" in com_ret_dir_raid1 and "ext3" in com_ret_dir_raid1:
                            f.write("Linux磁盘存储管理题目十：6步都能grep过滤到正确, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目十：6步不能grep过滤到, ---error\n")

        except:
            print("Linux磁盘存储管理题目十:失败")

        else:
            print("Linux磁盘存储管理题目十:成功")


class Cat_score_11(object):

    @staticmethod
    def run():
        try:
            cmd_ext4 = "df -hT|grep '/examdata/result/file_use_as_disk' | grep ext4"
            com_ret_ext4 = commands.getoutput(cmd_ext4)

            cmd_file = "file 'df | grep '/examdata/result/file_use_as_disk' | awk '{print $1}'' | grep 'huge files'"
            com_ret_file = commands.getoutput(cmd_file)

            cmd_du = "du -sh 'df |grep '/examdata/result/file_use_as_disk' | awk '{print $1}'' | awk '{print $1}'|sed 's/[Mm]//g'"
            com_ret_du = commands.getoutput(cmd_du)

            with open(save_address, "a+") as f:
                if "" not in com_ret_ext4:
                    f.write("Linux磁盘存储管理题目十一：grep ext4正确, ---ok\n" )

                else:
                    f.write("Linux磁盘存储管理题目十一：grep ext4错误, ---error\n")

                if os.path.exists(linux_txt_11):
                    with open(save_address, "a+") as f:
                        f.write("Linux磁盘存储管理题目十一：文件%s存在, ---ok\n" % linux_txt_11)

                    with open(save_address, "a+") as f:
                        if "" not in com_ret_file:
                            f.write("Linux磁盘存储管理题目十一：%s目录是一个文档, ---ok\n" % linux_txt_11)
                        else:
                            f.write("Linux磁盘存储管理题目十一：%s目录不是一个文档, ---error\n" % linux_txt_11)

                    with open(save_address, "a+") as f:
                        if "100" in com_ret_du or "101" in com_ret_du:
                            f.write("Linux磁盘存储管理题目十一：结果为100或101正确, ---ok\n")
                        else:
                            f.write("Linux磁盘存储管理题目十一：结果为100或101错误, ---error\n")
                else:
                    f.write("Linux磁盘存储管理题目十一：文件%s不存在, ---error\n" % linux_txt_11)


        except:
            print("Linux磁盘存储管理题目十一:失败")

        else:
            print("Linux磁盘存储管理题目十一:成功")



def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()
    Cat_score_5().run()
    Cat_score_6().run()
    Cat_score_7().run()
    Cat_score_8().run()
    Cat_score_9().run()
    Cat_score_10().run()
    Cat_score_11().run()

run()


