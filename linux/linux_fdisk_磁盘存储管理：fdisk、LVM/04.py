# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re

save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_4_1 = "/examdata/result/mountpoint_size"
linux_txt_4 = "/examdata/result/exam_lvm"


def test_04():
    try:
        ret_size = None

        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目四：文件%s存在, ---ok\n" % linux_txt_4)

            cmd_size = "df -h %s |awk 'NR >1 {print $1,$2}'" % linux_txt_4
            ret_size = commands.getoutput(cmd_size)
        else:
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目四：文件%s存在, ---error\n" % linux_txt_4)

        if os.path.exists(linux_txt_4_1):
            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目四：文件%s存在, ---ok\n" % linux_txt_4_1)

            cmd_htp = "df -hTP /|awk 'NR >1 {print $1,$2}'"
            ret_htp = commands.getoutput(cmd_htp)

            cmd_dev = "df -h /dev/shm|awk 'NR >1 {print $1,$2}'"
            ret_dev = commands.getoutput(cmd_dev)

            cmd_boot = "df -h /boot|awk 'NR >1 {print $1,$2}'"
            ret_boot = commands.getoutput(cmd_boot)

            cmd_cat = "cat %s" % linux_txt_4_1
            ret_cat = commands.getoutput(cmd_cat)
            # 1
            with open(save_address, "a+") as f:
                if ret_htp in ret_cat:
                    f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s一致, ---ok\n" % (linux_txt_4_1, ret_htp))
                else:
                    f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s不一致, ---error\n" % (linux_txt_4_1, ret_htp))
            # 2
            with open(save_address, "a+") as f:
                if ret_dev in ret_cat:
                    f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s一致, ---ok\n" % (linux_txt_4_1, ret_dev))
                else:
                    f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s不一致, ---error\n" % (linux_txt_4_1, ret_dev))
            # 3
            with open(save_address, "a+") as f:
                if ret_boot in ret_cat:
                    f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s一致, ---ok\n" % (linux_txt_4_1, ret_boot))
                else:
                    f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s不一致, ---error\n" % (linux_txt_4_1, ret_boot))
            # 4
            with open(save_address, "a+") as f:
                if ret_size:
                    if ret_size in ret_cat:
                        f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s一致, ---ok\n" % (linux_txt_4_1, ret_size))
                    else:
                        f.write("Linux磁盘存储管理题目四：查看文件%s和内容%s不一致, ---error\n" % (linux_txt_4_1, ret_size))
                else:
                    f.write("Linux磁盘存储管理题目四：文件%s不存在，无法跟文件%s比较, ---error\n" % (linux_txt_4, linux_txt_4_1))

        else:
            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目四：文件%s不存在, ---error\n" % linux_txt_4_1)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目四：文件%s不存在,df -hTP无法进行比较 ---error\n" % linux_txt_4_1)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目四：文件%s不存在,/dev/shm无法进行比较 ---error\n" % linux_txt_4_1)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目四：文件%s不存在,/boot|awk无法进行比较 ---error\n" % linux_txt_4_1)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目四：文件%s不存在，无法跟文件%s比较, ---error\n" % (linux_txt_4, linux_txt_4_1))

    except:
        print("操作LINUX安装与配置题目四:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目四:成功")


if __name__ == '__main__':
    test_04()
