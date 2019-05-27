# coding=utf-8
# 数据库得分保存地址

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_5_find = '/examdata/result/version.txt'
linux_6_find = '/examdata/result/mem0.txt'
linux_7_find = '/examdata/result/df.txt'
linux_8_find = '/examdata/result/jichu04.txt'
linux_9_find = '/examdata/result/jichu05.txt'
linux_10_find_1 = '/etc/ssh/sshd_config'
linux_10_find_2 = '/examdata/result/jichu06_conf'
linux_11_find = '/examdata/result/system_character'
linux_12_find = '/examdata/result/ls_man_location'
linux_13_path = '/opt/kong/sbin'
linux_14_find = '/examdata/result/system_arch_dirs'
linux_15_find = '/examdata/result/sshd_cconfig_location'


import commands
import os
import re
import psutil


class Cat_score_5(object):
    """
    题目 5
    查看系统当前版本及内核信息，信息输出到/examdata/result/version.txt
    """
    @staticmethod
    def run():
        try:

            # 检查系统版本和内核信息,并保存
            cmd_1 = "cat /etc/redhat-release"
            cmd_2 = "uname -a"

            com_ret_1 = commands.getoutput(cmd_1)
            com_ret_2 = commands.getoutput(cmd_2)

            with open(save_address_test, 'w') as f:
                f.write(com_ret_1)

            with open(save_address_test, "a+") as f:
                f.write(com_ret_2)

            # 比较是否存在
            if os.path.exists(linux_5_find):
                cmd_3 = 'cat /examdata/result/version.txt'
                com_ret_3 = commands.getoutput(cmd_3)

                with open(save_address, 'a+') as f:
                    if com_ret_1 in com_ret_3 and com_ret_2 in com_ret_3:
                        f.write("LINUX系统基本组成题目五：文件内容与1）和2）的输出一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目五：文件内容与1）和2）的输出不一致, ---error" + '\n')
            else:
                with open(save_address, 'w') as f:
                    f.write(("LINUX系统基本组成题目五：文件%s 不存在, ---error" + '\n') % linux_5_find)


        except:
            print("操作LINUX系统基本组成题目五:失败")

        else:
            print("操作LINUX系统基本组成题目五:成功")


class Cat_score_6(object):
    """
    题目 6
    查看当前系统分配内存大小, 将查询结果输出到/examdata/result/mem0.txt。
    """

    @staticmethod
    def run():
        try:
            # 查看当前系统分配内存大小
            mem = psutil.virtual_memory()

            with open(save_address_test, 'w') as f:
                f.write(str(mem))

            # 比较是否存在
            if os.path.exists(linux_6_find):
                cmd = 'cat /examdata/result/mem0.txt'
                com_ret = commands.getoutput(cmd)

                f = open(linux_6_find)
                line_str = ""
                for line in f.readlines():
                    line_str += line

                f.close()

                with open(save_address, 'a+') as f:

                    if com_ret in line_str:
                        f.write("LINUX系统基本组成题目六：文件内容与1的输出一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目五：文件内容与1的输出不一致, ---error" + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目五：文件%s 不存在, ---error" + '\n') % linux_6_find)

        except:
            print("操作LINUX系统基本组成题目六:失败")

        else:
            print("操作LINUX系统基本组成题目六:成功")


class Cat_score_7(object):
    """
    题目 7
    7.查看当前文件系统使用率情况，并将查询结果输出到/examdata/result/df.txt并核对是否有超过90%现象。
    """

    @staticmethod
    def run():
        try:

            cmd_df_1 = "df -h"
            cmd_df = "df -h | awk '{print $5}'"

            com_ret_df_1 = commands.getoutput(cmd_df_1)
            com_ret_df = commands.getoutput(cmd_df)

            # 临时保存过滤的信息
            with open(save_address_test, 'w') as f:
                f.write(str(com_ret_df))

            # 打开临时保存的信息
            f = open(save_address_test)

            # 数据进行处理
            line_list = []
            for line in f.readlines():
                line = line.strip('\n')
                line_list.append(line)
            f.close()

            # 正则取出数据进行判断是否超过90%
            list_num = []
            test = 0

            for i in line_list:
                a = re.match(r'\d*', i)
                if len(a.group()) > 0:
                    list_num.append(a.group())

            for i in list_num:

                if int(i) < 90:
                    test += 1

                else:
                    pass

            with open(save_address, 'a+') as f:
                if test > 0:
                    f.write("LINUX系统基本组成题目七：当前文件系统使用率小于90%, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目七：当前文件系统使用率大于90%, ---error" + '\n')

            if os.path.exists(linux_7_find):

                cmd_cat = "cat /examdata/result/df.txt"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, 'a+') as f:
                    if com_ret_df_1 in com_ret_cat:
                        f.write("LINUX系统基本组成题目七：cat /examdata/result/df.txt文件内容与1的输出一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目七：cat /examdata/result/df.txt文件内容与1的输出不一致, ---error" + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目七：文件%s不存在, ---error" + '\n') % linux_7_find)

        except:
            print("操作LINUX系统基本组成题目七:失败")

        else:
            print("操作LINUX系统基本组成题目七:成功")


class Cat_score_8(object):
    """
    题目 8
    找出 /etc 底下，文档大小介于80K 到 130K 之间的文档，并且将权限完整的列出 (ls -l)
    并将列出输出到/examdata/result/jichu04.txt
    """

    @staticmethod
    def run():
        try:

            cmd_df = "find /etc -size +80k -a -size -130k -exec ls -l {} \;"
            # cmd_df_test = "find /etc -size +80k -a -size -130k -exec ls -l {} \; | awk '{print $9}'"

            com_ret = commands.getoutput(cmd_df)
            # com_ret_test = commands.getoutput(cmd_df_test)

            # 保存相应大小的文档到临时文件里面
            with open(save_address_test, 'w') as f:
                f.write(str(com_ret))

            # 打开临时文件
            f_test = open(save_address_test, "r")
            line_test = ""

            for line in f_test.readlines():
                line = line.strip('\n')
                line_test += line

            f.close()

            if os.path.exists(linux_8_find):
                # 打开正式文件
                f_file = open(linux_8_find)
                line_file = ""

                for line in f_file.readlines():
                    line = line.strip('\n')
                    line_file += line

                f.close()

                with open(save_address, 'a+') as f:

                    if line_test in line_file:
                        f.write("LINUX系统基本组成题目八：文件内容与1的输出一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目八：文件内容与1的输出不一致, ---error" + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目八：文件 %s 不存在, ---error" + '\n') % linux_8_find)

        except:
            print("操作LINUX系统基本组成题目八:失败")


        else:
            print("操作LINUX系统基本组成题目八:成功")


class Cat_score_9(object):
    """
    题目 9
    9.找出 /etc 底下，文档天小大于 50K 且文档所有人不是 root 的文档，并将权限完整的列出，
    列出输出到/examdata/result/jichu05.txt。
    """

    @staticmethod
    def run():
        try:

            cmd_df = "find  /etc  -size +50k -a ! -user root -exec ls -ld {} \; "
            # cmd_df_test = "find  /etc  -size +50k -a ! -user root -exec ls -ld {} \;  | awk '{print $9}'"

            com_ret = commands.getoutput(cmd_df)
            # com_ret_test = commands.getoutput(cmd_df_test)

            if os.path.exists(linux_9_find):

                # # 判断保存文件是否与输出的一致
                f = open(linux_9_find)
                line = f.readlines()
                # 因为取出来的是列表，需要遍历，拼接字符串，python和shell交互得到的是字符串
                line_i = ""

                for i_line in line:
                    line_i += i_line

                f.close()

                with open(save_address, 'a+') as f:
                    if com_ret in line_i:
                        f.write("LINUX系统基本组成题目九：文件内容与1的输出一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目九：文件内容与1的输出不一致, ---error" + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目九：文件%s 不存在, ---error" + '\n') % linux_9_find)


        except:
            print("操作LINUX系统基本组成题目九:失败")

        else:
            print("操作LINUX系统基本组成题目九:成功")


class Cat_score_10(object):
    """
    题目 10
    10.为/etc/ssh/sshd_config建为硬链接，并把硬链接放到/examdata/result/jichu06_conf
    """

    @staticmethod
    def run():
        try:
            filename_1 = linux_10_find_1
            filename_2 = linux_10_find_2

            if os.path.exists(filename_1):

                # 创建硬链接
                cmd_ln = "ln /etc/ssh/sshd_config /examdata/result/jichu06_conf"

                # 判断硬链接创建是否成功
                cmd_status_ln, cmd_ret_ln = commands.getstatusoutput(cmd_ln)
                if os.path.exists(filename_2):

                    # 查看硬链接创建成功条件
                    cmd_ln_grep_cat = "ls /etc/ssh/sshd_config /examdata/result/jichu06_conf -l | awk '{print $2}'"

                    # 执行命令判断是否有没有输出，没有输出就是正确的
                    cmd_if_cat = 'diff /etc/ssh/sshd_config /examdata/result/jichu06_conf'

                    if cmd_status_ln == 0 or cmd_ret_ln == "ln: creating hard link `/examdata/result/jichu06_conf': File exists":

                        # 判断硬链接创建成功条件是否成功，并过滤数据
                        com_ret_ln_grep_cat = commands.getoutput(cmd_ln_grep_cat)

                        line_list = []
                        for line in com_ret_ln_grep_cat:
                            if line == '\n':
                                pass

                            else:
                                line_list.append(line)

                        num_a = len(line_list)

                        for num in line_list:
                            if '2' == num:
                                num_a -= 1
                            else:
                                pass

                        if num_a == 0:

                            # 最后判断硬链接条件
                            com_status_if_cat, com_ret_if_cat = commands.getstatusoutput(cmd_if_cat)
                            if com_status_if_cat == 0:

                                with open(save_address, 'a+') as f:
                                    f.write("LINUX系统基本组成题目十：创建硬链接成功，且两文件内容为一致, ---ok" + '\n')


                                # 题目二
                                # 备份文件
                                cmd_cp_1 = "cp /etc/ssh/{sshd_config,sshd_config.bak}"
                                cmd_cp_2 = "cp /examdata/result/{jichu06_conf,jichu06.conf.bak}"

                                # 执行
                                cmd_status_cp_1, cmd_ret_cp_1 = commands.getstatusoutput(cmd_cp_1)
                                cmd_status_cp_2, cmd_ret_cp_2 = commands.getstatusoutput(cmd_cp_2)

                                if cmd_status_cp_1 == 0 and cmd_status_cp_2 == 0:

                                    # 查看原文件的行数
                                    cmd_rm_cat_1 = "cat /etc/ssh/sshd_config|wc -l"
                                    cmd_ret_rm_cat_1 = commands.getoutput(cmd_rm_cat_1)

                                    # 删除非备份文件, 判断硬链接是否有效
                                    cmd_rm_1 = "rm /etc/ssh/sshd_config"
                                    commands.getstatusoutput(cmd_rm_1)

                                    # 查看备份文件的行数
                                    cmd_cat_1 = "cat /etc/ssh/sshd_config.bak|wc -l"
                                    cmd_ret_cat_1 = commands.getoutput(cmd_cat_1)

                                    # 判断备份文件与原的行数是否一致
                                    if int(cmd_ret_rm_cat_1) == int(cmd_ret_cat_1):
                                        with open(save_address, 'a+') as f:
                                            f.write(
                                                "LINUX系统基本组成题目十：sshd_config.bak备份文件可打开，内容没丢失, ---ok" + '\n')
                                    else:

                                        with open(save_address, 'a+') as f:
                                            f.write("LINUX系统基本组成题目十：sshd_config.bak备份文件不可打开，内容丢失, ---error" + '\n')

                                    # 恢复删除的文件
                                    cmd_hf_1 = "ln /examdata/result/jichu06_conf /etc/ssh/sshd_config"

                                    # 执行
                                    commands.getstatusoutput(cmd_hf_1)


                                else:
                                    with open(save_address, 'a+') as f:
                                        f.write("LINUX系统基本组成题目十：备份/etc/ssh/sshd_config和/examdata/result/jichu06.conf文件失败, ---error" + '\n')


                            else:

                                with open(save_address, 'a+') as f:
                                    f.write("LINUX系统基本组成题目十：创建硬链接失败，且两文件内容为不一致, ---error" + '\n')

                        else:

                            with open(save_address, 'a+') as f:
                                f.write("LINUX系统基本组成题目十：文件没有硬链接, ---error" + '\n')

                    else:

                        with open(save_address, 'a+') as f:
                            f.write("LINUX系统基本组成题目十：' /etc/ssh/sshd_config与 /examdata/result/jichu06_conf不是硬链接', ---error" + '\n')

                else:

                    with open(save_address, 'a+') as f:
                        f.write("LINUX系统基本组成题目十：备份文件sshd_config到/examdata/result/jichu06_conf失败, ---error" + '\n')
            else:

                with open(save_address, 'a+') as f:
                    f.write("LINUX系统基本组成题目十：文件sshd_config不存在， 执行cp /examdata/result/jichu06_conf /etc/ssh/sshd_config，, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目十:失败")

        else:
            print("操作LINUX系统基本组成题目十:成功")


class Cat_score_11(object):
    """
    题目 11
    11.显示系统当前的字体集，并把结果存放到/examdata/result/system_character
    """

    @staticmethod
    def run():
        try:

            cmd_df = "echo $LANG"

            com_ret = commands.getoutput(cmd_df)

            if os.path.exists(linux_11_find):

                # 读取文件进行比较
                f = open(linux_11_find, 'r')
                r_ret = f.readlines()[0]
                f.close()

                with open(save_address, 'a+') as f:
                    if com_ret in r_ret:
                        f.write("LINUX系统基本组成题目十一：文件内容与1的输出一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目十一：文件内容与1的输出不一致, ---error" + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目十一：文件%s 不存在, ---error" + '\n') % linux_11_find)


        except:
            print("操作LINUX系统基本组成题目十一:失败")

        else:
            print("操作LINUX系统基本组成题目十一:成功")


class Cat_score_12(object):
    """
    题目 12
    find / -name "ls.1.gz"
    12.找出ls的 man文件目录位置，把结果存放到/examdata/result/ls_man_location
    """

    @staticmethod
    def run():
        try:

            cmd_df = "find / -name 'ls.1.gz'"

            com_ret = commands.getoutput(cmd_df)

            if os.path.exists(linux_12_find):
                # 读取文件进行比较
                f = open(linux_12_find, 'r')
                r_ret = f.readlines()
                f.close()

                with open(save_address, 'a+') as f:

                    if com_ret in r_ret:
                        f.write(("LINUX系统基本组成题目十二：文件在%s, ---ok" + '\n') % com_ret  )

                    else:
                        f.write(("LINUX系统基本组成题目十二：文件不在%s, ---error" + '\n') % com_ret)
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目十二：文件不在%s, ---error" + '\n') % linux_12_find)

        except:
            print("操作LINUX系统基本组成题目十二:失败")

        else:
            print("操作LINUX系统基本组成题目十二:成功")


class Cat_score_13(object):
    """
    题目 13
    修改家目录下的.bashrc，将/opt/kong/sbin添加到PATH，要求echo $PATH能显示修改后
    """

    @staticmethod
    def run():
        try:

            cmd_df = "echo $PATH"
            com_ret = commands.getoutput(cmd_df)

            # 查看是否有要的环境变量
            re_find = re.findall(linux_13_path, com_ret)

            with open(save_address, 'a+') as f:

                if linux_13_path in re_find:
                    f.write(("LINUX系统基本组成题目十三：检查出有%s这个路径, ---ok" + '\n') % linux_13_path  )

                else:
                    f.write(("LINUX系统基本组成题目十三：检查出没有%s这个路径, ---error" + '\n') % linux_13_path)

        except:
            print("操作LINUX系统基本组成题目十三:失败")

        else:
            print("操作LINUX系统基本组成题目十三:成功")


class Cat_score_14(object):
    """
    题目 14
    14.命令显示系统默认由内由几大目录组成，将结果存放到/examdata/result/system_arch_dirs
    """

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_14_find):
                cmd_df = "ls /"
                cmd_df_num = "ls /|wc -w"

                com_ret = commands.getoutput(cmd_df)
                # com_ret_num = commands.getoutput(cmd_df_num)

                cmd_cat_file_1 = "cat /examdata/result/system_arch_dirs"
                cmd_ret_file_1 = commands.getoutput(cmd_cat_file_1)

                # cmd_cat_file_num = "cat /examdata/result/system_arch_dirs | wc -w"
                # cmd_ret_file_num = commands.getoutput(cmd_cat_file_num)

                with open(save_address, 'a+') as f:
                    if com_ret in cmd_ret_file_1:
                        f.write("LINUX系统基本组成题目十四：检查结果是否与1）一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目十四：检查结果是否与1）不一致, ---error" + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目十四：文件%s 不存在, ---error" + '\n') % linux_14_find)

        except:
            print("操作LINUX系统基本组成题目十四:失败")

        else:
            print("操作LINUX系统基本组成题目十四:成功")


class Cat_score_15(object):
    """
    题目 15
    15.显示ssh配置文件在哪个目录，将结果存放到/examdata/result/sshd_cconfig_location。
    """

    @staticmethod
    def run():
        try:
            filename = linux_15_find

            if os.path.exists(filename):
                cmd_cat = "cat /examdata/result/sshd_cconfig_location"
                com_ret = commands.getoutput(cmd_cat)

                # 比较保存文件
                with open(save_address, 'a+') as f:

                    if "/etc/ssh/sshd_config" in com_ret:
                        f.write("LINUX系统基本组成题目十五：检查输出为/etc/ssh/sshd_config, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目十五：检查输出不为/etc/ssh/sshd_config, ---error" + '\n')

            else:
                with open(save_address, 'a+') as f:
                    f.write("LINUX系统基本组成题目十五：文件/examdata/result/sshd_cconfig_location不存在, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目十五:失败")

        else:
            print("操作LINUX系统基本组成题目十五:成功")


def run():
    Cat_score_5().run()
    Cat_score_6().run()
    Cat_score_7().run()
    Cat_score_8().run()
    Cat_score_9().run()
    Cat_score_10().run()
    Cat_score_11().run()
    Cat_score_12().run()
    Cat_score_13().run()
    Cat_score_14().run()
    Cat_score_15().run()

run()