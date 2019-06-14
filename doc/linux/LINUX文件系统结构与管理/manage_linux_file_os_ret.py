# coding=utf-8

import commands
import os

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/etc_size"
linux_txt_2_1 = "/examdata/result/boot_bak.tar.gz"
linux_txt_2_2 = "/examdata/result/boot"
linux_txt_3 = "/examdata/result/backup_varlog.tar.gz"
linux_txt_4 = "/testdata1/result/newhelloworld.txt"
linux_txt_4_1 = "/examdata/result/helloworld.backup"
linux_txt_6 = "/examdata/result/"
linux_txt_7 = "/examdata/result/partation_table"
linux_txt_8 = "/examdata/result/html"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux文件系统结构与管理题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_du = "du -sh /etc"
                com_ret_du = commands.getoutput(cmd_du)

                cmd_cat = "egrep '(du|/etc)' /examdata/result/etc_size"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    print(1)
                    if com_ret_du in com_ret_cat:
                        f.write("Linux文件系统结构与管理题目一：对比输出一致, ---ok\n")

                    else:
                        f.write("Linux文件系统结构与管理题目一：对比输出不一致, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("LinuxLinux文件系统结构与管理题目一：文件%s不存在, ---error\n" % linux_txt_1)


        except:
            print("Linux文件系统结构与管理题目一:失败")

        else:
            print("Linux文件系统结构与管理题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_2_1):
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目二：文件%s存在, ---ok\n" % linux_txt_2_1)

                if os.path.exists(linux_txt_2_2):
                    with open(save_address, "a+") as f:
                        f.write("Linux文件系统结构与管理题目二：文件%s存在, ---ok\n" % linux_txt_2_2)

                    cmd_tar = "tar -zxvf /examdata/result/boot_bak.tar.gz"
                    com_ret_tar = commands.getoutput(cmd_tar)

                    cmd_ls = "ls /boot /examdata/result/boot"
                    com_ret_ls = commands.getoutput(cmd_ls)

                    with open(save_address, "a+") as f:
                        if com_ret_tar in com_ret_ls:
                            f.write("Linux文件系统结构与管理题目二：对比输出一致, ---ok\n")

                        else:
                            f.write("Linux文件系统结构与管理题目二：对比输出一致, ---error\n")

                else:
                    with open(save_address, "a+") as f:
                        f.write("LinuxLinux文件系统结构与管理题目二：文件%s不存在, ---error\n" % linux_txt_2_2)


            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux文件系统结构与管理题目二：文件%s不存在, ---error\n" % linux_txt_2_1)


        except:
            print("Linux文件系统结构与管理题目二:失败")

        else:
            print("Linux文件系统结构与管理题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_3):
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目三：文件%s存在, ---ok\n" % linux_txt_3)

                cmd_tar = "tar -zxvf /examdata/result/backup_varlog.tar.gz"
                com_ret_tar = commands.getoutput(cmd_tar)

                cmd_ls = "ls /var/log/*.log  /examdata/result/*.log"
                com_ret_ls = commands.getoutput(cmd_ls)

                with open(save_address, "a+") as f:
                    if com_ret_tar in com_ret_ls:
                        f.write("Linux文件系统结构与管理题目三：对比输出一致, ---ok\n")

                    else:
                        f.write("Linux文件系统结构与管理题目三：对比输出一致, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux文件系统结构与管理题目三：文件%s不存在, ---error\n" % linux_txt_3)


        except:
            print("Linux文件系统结构与管理题目三:失败")

        else:
            print("Linux文件系统结构与管理题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_4):
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目四：文件%s存在, ---ok\n" % linux_txt_4)

                cmd_VM = "grep VMware /testdata1/result/newhelloworld.txt"
                com_ret_VM = commands.getoutput(cmd_VM)

                with open(save_address, "a+") as f:
                    if "VMware" in com_ret_VM:
                        f.write("Linux文件系统结构与管理题目四：有grep到VMware, ---error\n")
                    else:
                        f.write("Linux文件系统结构与管理题目四：没有grep到VMware, ---ok\n")

                cmd_xing = "grep '\*\*\*' /testdata1/result/newhelloworld.txt"
                com_ret_xing = commands.getoutput(cmd_xing)

                with open(save_address, "a+") as f:
                    if "***" in com_ret_xing:
                        f.write("Linux文件系统结构与管理题目四：能grep到***, ---ok\n")
                    else:
                        f.write("Linux文件系统结构与管理题目四：不能grep到***, ---error\n")

                cmd_tools = "grep  -i 'Tools' /testdata1/result/newhelloworld.txt"
                com_ret_tools = commands.getoutput(cmd_tools)

                with open(save_address, "a+") as f:
                    if "Tools" in com_ret_tools or "tools" in com_ret_tools or "TOOLS" in com_ret_tools:
                        f.write("Linux文件系统结构与管理题目四：能grep到 'Tools', ---error\n")
                    else:
                        f.write("Linux文件系统结构与管理题目四：不能grep到 'Tools', ---ok\n")

                cmd_head = "head -n 30 /testdata1/result/newhelloworld.txt|grep '[[:upper:]]'"
                com_ret_head = commands.getoutput(cmd_head)

                with open(save_address, "a+") as f:
                    if "upper" in com_ret_head:
                        f.write("Linux文件系统结构与管理题目四：能grep 'head [[:upper:]]', ---error\n")
                    else:
                        f.write("Linux文件系统结构与管理题目四：不能grep 'head [[:upper:]]', ---ok\n")

                with open(save_address, "a+") as f:
                    if os.path.exists(linux_txt_4_1):
                        f.write("Linux文件系统结构与管理题目四：文件%s存在, ---ok\n" % linux_txt_4_1)
                    else:
                        f.write("LinuxLinux文件系统结构与管理题目四：文件%s不存在, ---error\n" % linux_txt_4_1)

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux文件系统结构与管理题目四：文件%s不存在, ---error\n" % linux_txt_4)


        except:
            print("Linux文件系统结构与管理题目四:失败")

        else:
            print("Linux文件系统结构与管理题目四:成功")


class Cat_score_5(object):

    @staticmethod
    def run():
        try:

            cmd_df = "df -hTP|grep '/dev/shm'|awk '{print $5}'"
            com_ret_df = commands.getoutput(cmd_df)

            with open(save_address, "a+") as f:
                if "4G" in com_ret_df or '4.0G' in com_ret_df:
                    f.write("Linux文件系统结构与管理题目五：过滤出来的结果是4G, ---ok\n")
                else:
                    f.write("Linux文件系统结构与管理题目五：过滤出来的结果不是4G, ---error\n")

        except:
            print("Linux文件系统结构与管理题目五:失败")

        else:
            print("Linux文件系统结构与管理题目五:成功")


class Cat_score_6(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_6):
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目六：文件%s存在, ---ok\n" % linux_txt_6)

                cmd_find = "find /examdata/result/ -size 100M"
                com_ret_find = commands.getoutput(cmd_find)

                with open(save_address, "a+") as f:
                    if com_ret_find == "":
                        f.write("Linux文件系统结构与管理题目六：没有找到100M的文件, ---error\n")

                    else:
                        f.write("Linux文件系统结构与管理题目六：找到100M的文件, ---ok\n")

                cmd_file = "file /examdata/result/100files/*.txt|grep empty|wc -l"
                com_ret_file = commands.getoutput(cmd_file)

                with open(save_address, "a+") as f:
                    if '100' in com_ret_file:
                        f.write("Linux文件系统结构与管理题目六：结果总数为100, ---ok\n")

                    else:
                        f.write("Linux文件系统结构与管理题目六：结果总数不为100, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目六：文件%s存在, ---ok\n" % linux_txt_6)


        except:
            print("Linux文件系统结构与管理题目六:失败")

        else:
            print("Linux文件系统结构与管理题目六:成功")


class Cat_score_7(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_7):
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目七：文件%s存在, ---ok\n" % linux_txt_7)

                cmd_find = "file /examdata/result/partation_table |grep startsector"
                com_ret_find = commands.getoutput(cmd_find)

                with open(save_address, "a+") as f:
                    if "startsector" in com_ret_find:
                        f.write("Linux文件系统结构与管理题目七：过滤出startsector, ---ok\n")

                    else:
                        f.write("Linux文件系统结构与管理题目七：没有过滤出startsector, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目七：文件%s存在, ---ok\n" % linux_txt_7)

        except:
            print("Linux文件系统结构与管理题目七:失败")

        else:
            print("Linux文件系统结构与管理题目七:成功")


class Cat_score_8(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_8):
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目八：文件%s存在, ---ok\n" % linux_txt_8)

                cmd_find = "chcon --reference=/var/www/html/ /examdata/result/html/"
                commands.getoutput(cmd_find)

                cmd_find = "ll -Zd /examdata/result/html|grep 'httpd_sys_content_t'"
                com_ret_find = commands.getoutput(cmd_find)

                with open(save_address, "a+") as f:
                    if "httpd_sys_content_t" in com_ret_find:
                        f.write("Linux文件系统结构与管理题目八：过滤出httpd_sys_content_t, ---ok\n")

                    else:
                        f.write("Linux文件系统结构与管理题目八：没有过滤出httpd_sys_content_t, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux文件系统结构与管理题目八：文件%s存在, ---ok\n" % linux_txt_8)


        except:
            print("Linux文件系统结构与管理题目八:失败")

        else:
            print("Linux文件系统结构与管理题目八:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()
    Cat_score_5().run()
    Cat_score_6().run()
    Cat_score_7().run()
    Cat_score_8().run()

run()