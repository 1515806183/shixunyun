# coding=utf-8
# 数据库得分保存地址

import commands
import psutil
import os
import re

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_1_root = 'lv_root:'
linux_1_swap = 'lv_swap:'
linux_3_find_1 = '/etc/inittab'
linux_3_find_2 = '/examdata/result/default_boot_mode'



class Cat_score_1(object):

    @staticmethod
    def run():
        try:
            cmd = "fdisk -l"
            com_ret = commands.getoutput(cmd)
            b = 0

            # 临时保存文件
            with open(save_address_test, 'w') as f:
                f.write(com_ret + '\n')

            f = open(save_address_test, 'r')
            line_list_find = []
            for line in f.readlines():
                line = line.strip('\n')
                line_list_find.append(line)
            f.close()

            for i in line_list_find:
                if linux_1_root in i or linux_1_swap in i:
                    b += 1

                else:
                    pass

            with open(save_address, 'w') as f:
                if b == 2:
                    f.write("LINUX安装与配置题目一：系统存在根分区和swap分区, ---ok" + '\n')
                else:
                    f.write("LINUX安装与配置题目一：系统不存在根分区和swap分区, ---ok" + '\n')

        except:
            print("操作LINUX安装与配置题目一:失败")

        else:
            print("操作LINUX安装与配置题目一:成功")


class Cat_score_2(object):
    """
    题目 2
    rhel65_training01系统当前环境swap 大小为1G，请调整swap大小为2G
    """

    @staticmethod
    def run():
        try:
            cmd_swap = "lsblk | grep lv_swap | awk '{print $5}'"
            com_ret_swap = commands.getoutput(cmd_swap)

            with open(save_address, 'a+') as f:
                if com_ret_swap == '2G':
                    f.write("LINUX安装与配置题目二：系统当前环境swap 大小为2G, ---ok" + '\n')
                else:
                    f.write("LINUX安装与配置题目二：系统当前环境swap 大小不为2G, ---error" + '\n')
        except:
            print("操作LINUX安装与配置题目二:失败")

        else:
            print("操作LINUX安装与配置题目二:成功")


class Cat_score_3(object):
    """
    题目 3
    3.将修改后的结果存放到/examdata/result/default_boot_mode,要求不要修改默认配置文件
    """

    @staticmethod
    def run():
        try:
            filename_1 = linux_3_find_1
            filename_2 = linux_3_find_2

            # 判断/etc/inittab文件是否存在
            if os.path.exists(filename_1):
                with open(save_address, 'a+') as f:
                    f.write("LINUX安装与配置题目二:%s文件存在, ---ok" % filename_1 + '\n')

                # 检查/etc/inittab文件是否有以id: 3:initdefault:
                f = open(filename_1)

                line_list_find = []
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_find.append(line)

                f.close()

                a_num = 0

                for i in line_list_find:
                    str_1_file = re.match(r'^id:3:initdefault:', str(i))

                    if str_1_file == None:
                        pass

                    else:
                        if "id:3:initdefault:" == str_1_file.group():
                            a_num = 1
                            break
                        else:
                            a_num = 0

                with open(save_address, 'a+') as f:
                    if a_num == 1:
                        f.write(
                            "LINUX安装与配置题目三：%s 文件是否有以id:3:initdefault: 存在开头的一行,修改了原文件, ---error" % filename_1 + '\n')

                    else:
                        f.write(
                            "LINUX安装与配置题目三：%s 文件是否有以id:3:initdefault: 不存在开头的一行,没有修改原文件, ---ok" % filename_1 + '\n')

            else:
                with open(save_address, 'a+') as f:
                    f.write("LINUX安装与配置题目三: %s 文件不存在, ---error" % filename_1 + '\n')

            if os.path.exists(filename_2):
                # 查询 /examdata/result/default_boot_mode
                cmd = "tail /examdata/result/default_boot_mode"

                com_ret = commands.getoutput(cmd)
                with open(save_address_test, "w") as f:
                    f.write(com_ret)

                f = open(save_address_test, 'r')
                line_list = []
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list.append(line)

                f.close()

                b_num = 0
                for i in line_list:
                    str_1 = re.match(r'^id:3:initdefault:', str(i))

                    if str_1 == None:
                        pass

                    else:
                        if "id:3:initdefault:" == str_1.group():
                            b_num = 1
                            break

                        else:
                            b_num = 0

                with open(save_address, 'a+') as f:
                    if b_num == 1:
                        f.write("LINUX安装与配置题目三：检查%s 文件有id:3:initdefault: 开头一行, ---ok" % filename_2 + '\n')
                    else:
                        f.write("LINUX安装与配置题目三：检查%s 文件没有id:3:initdefault: 开头一行, ---error" % filename_2 + '\n')

            else:
                with open(save_address, 'a+') as f:
                    f.write("LINUX安装与配置题目三: %s 文件不存在, ---error" % filename_2 + '\n')


        except:
            print("操作LINUX安装与配置题目三:失败")



        else:
            print("操作LINUX安装与配置题目三:成功")


class Cat_score_4(object):
    """
    题目 4
    请将系统的字符集改为英文（en_US.UTF-8）。
    """

    @staticmethod
    def run():
        try:

            # 检查当前系统的字符集设置
            cmd_1 = "echo $LANG"
            cmd_2 = "cat /etc/sysconfig/i18n"

            com_ret_1 = commands.getoutput(cmd_1)
            com_ret_2 = commands.getoutput(cmd_2)

            with open(save_address, 'a+') as f:

                if "en_US.utf8" in com_ret_1 or 'en_US.utf-8' in com_ret_1:
                    f.write("LINUX安装与配置题目四：echo $LANG,输出结果为 %s , ---ok" % com_ret_1 + '\n')

                else:
                    f.write("LINUX安装与配置题目四：echo $LANG,输出结果为 %s , ---error" % com_ret_1 + '\n')

            with open(save_address, 'a+') as f:

                if 'en_US.UTF-8' in com_ret_2 or "en_US.UTF8" in com_ret_2:
                    f.write("LINUX安装与配置题目四：检查cat /etc/sysconfig/i18n,输出结果为 %s , ---ok" % com_ret_2 + '\n')

                else:
                    f.write("LINUX安装与配置题目四：检查cat /etc/sysconfig/i18n,输出结果为 %s , ---error" % com_ret_2 + '\n')


        except:
            print("操作LINUX安装与配置题目四:失败")


        else:
            print("操作LINUX安装与配置题目四:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()


run()
