# coding=utf-8

import commands
import os

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'


linux_txt_1 = "/examdata/result/apache_install_log"
linux_txt_3 = "/examdata/result/httpd_files"
linux_txt_4 = "/examdata/result/httpd_deps"
linux_txt_5 = "/examdata/result/vim_uninstall_log"
linux_txt_6 = "/examdata/result/rpmbuild_package_install.log"
linux_txt_7_1 = "/mnt/Packages/mysql-server-5.1.71-1.el6.x86_64.rpm"
linux_txt_7_2 = "/examdata/result/mysql.txt"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:

            cmd_rpm = "rpm -qa httpd"
            com_ret_egrep = commands.getoutput(cmd_rpm)

            with open(save_address, "w") as f:
                if com_ret_egrep == "":
                    f.write("Linux软件安装与配置题目一：设置httpd开机启动失败, ---error\n")

                else:
                    f.write("Linux软件安装与配置题目一：设置httpd开机启动成功, ---ok\n")

            if os.path.exists(linux_txt_1):
                with open(save_address, "a+") as f:
                    f.write("Linux软件安装与配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_grep = "grep 'will be installed' /examdata/result/apache_install_log"
                com_ret_grep = commands.getoutput(cmd_grep)

                with open(save_address, "a+") as f:
                    if "will be installed" in com_ret_grep:
                        f.write("Linux软件安装与配置题目一：有重定向日志, ---ok\n")

                    else:
                        f.write("Linux软件安装与配置题目一：无重定向日志, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux软件安装与配置题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux软件安装与配置题目一:失败")

        else:
            print("Linux软件安装与配置题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:

            cmd_chkconfig = "chkconfig --list httpd| grep '3:启用'"
            com_ret_chkconfig = commands.getoutput(cmd_chkconfig)

            with open(save_address, "a+") as f:
                if "3:启用" in com_ret_chkconfig:
                    f.write("Linux软件安装与配置题目二：设置httpd开机启动成功, ---ok\n")

                else:
                    f.write("Linux软件安装与配置题目二：设置httpd开机启动成功, ---error\n")

        except:
            print("Linux软件安装与配置题目二:失败")

        else:
            print("Linux软件安装与配置题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:

            cmd_rpm = "rpm  -ql httpd"
            com_ret_egrep = commands.getoutput(cmd_rpm)

            if os.path.exists(linux_txt_3):
                with open(save_address, "a+") as f:
                    f.write("Linux软件安装与配置题目三：文件%s存在, ---ok\n" % linux_txt_3)

                cmd_cat = "cat /examdata/result/httpd_files"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if com_ret_egrep in com_ret_cat:
                        f.write("Linux软件安装与配置题目三：对比输出正确, ---ok\n")

                    else:
                        f.write("Linux软件安装与配置题目三：对比输出错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux软件安装与配置题目三：文件%s不存在, ---error\n" % linux_txt_3)

        except:
            print("Linux软件安装与配置题目三:失败")

        else:
            print("Linux软件安装与配置题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_4):
                with open(save_address, "a+") as f:
                    f.write("Linux软件安装与配置题目四：文件%s存在, ---ok\n" % linux_txt_4)

                cmd_cat = "cat /examdata/result/httpd_deps|egrep '(chkconfig|apr|httpd-tools)'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "chkconfig" in com_ret_cat or "apr" in com_ret_cat or "httpd-tools" in com_ret_cat:
                        f.write("Linux软件安装与配置题目四：输出正确, ---ok\n")

                    else:
                        f.write("Linux软件安装与配置题目四：输出错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux软件安装与配置题目四：文件%s不存在, ---error\n" % linux_txt_4)

        except:
            print("Linux软件安装与配置题目四:失败")

        else:
            print("Linux软件安装与配置题目四:成功")


class Cat_score_5(object):

    @staticmethod
    def run():
        try:

            cmd_rpm = "rpm -qa | grep vim-common"
            com_ret_egrep = commands.getoutput(cmd_rpm)

            with open(save_address, "a+") as f:
                if "vim-common" in com_ret_egrep:
                    f.write("Linux软件安装与配置题目五：输出正确, ---ok\n")

                else:
                    f.write("Linux软件安装与配置题目五：输出错误, ---error\n")

            if os.path.exists(linux_txt_5):
                with open(save_address, "a+") as f:
                    f.write("Linux软件安装与配置题目五：文件%s存在, ---ok\n" % linux_txt_5)

                cmd_cat = "cat /examdata/result/vim_uninstall_log|egrep '(vim-enhanced|vim-common)'"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "vim-enhanced" in com_ret_cat or "vim-common" in com_ret_cat:
                        f.write("Linux软件安装与配置题目五：对比输出正确, ---ok\n")

                    else:
                        f.write("Linux软件安装与配置题目五：对比输出错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux软件安装与配置题目五：文件%s不存在, ---error\n" % linux_txt_5)

        except:
            print("Linux软件安装与配置题目五:失败")

        else:
            print("Linux软件安装与配置题目五:成功")


class Cat_score_6(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_6):
                with open(save_address, "a+") as f:
                    f.write("Linux软件安装与配置题目六：文件%s存在, ---ok\n" % linux_txt_6)

                cmd_cat = "cat /examdata/result/rpmbuild_package_install.log|grep rpm-build"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "rpm-build" in com_ret_cat:
                        f.write("Linux软件安装与配置题目六：对比输出正确, ---ok\n")

                    else:
                        f.write("Linux软件安装与配置题目六：对比输出错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux软件安装与配置题目六：文件%s不存在, ---error\n" % linux_txt_6)

        except:
            print("Linux软件安装与配置题目六:失败")

        else:
            print("Linux软件安装与配置题目六:成功")


class Cat_score_7(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_7_1):
                with open(save_address, "a+") as f:
                    f.write("Linux软件安装与配置题目七：文件%s存在, ---ok\n" % linux_txt_7_1)

                cmd_rpm = "rpm -qpR /mnt/Packages/mysql-server-5.1.71-1.el6.x86_64.rpm"
                com_ret_rpm = commands.getoutput(cmd_rpm)

                if os.path.exists(linux_txt_7_2):
                    with open(save_address, "a+") as f:
                        f.write("Linux软件安装与配置题目七：文件%s存在, ---ok\n" % linux_txt_7_2)

                    cmd_cat = "cat /examdata/result/mysql.txt"
                    com_ret_cat = commands.getoutput(cmd_cat)

                    with open(save_address, "a+") as f:
                        if com_ret_cat in com_ret_rpm and "error" not in com_ret_rpm:
                            f.write("Linux软件安装与配置题目七：对比输出正确, ---ok\n")

                        else:
                            f.write("Linux软件安装与配置题目七：对比输出错误, ---error\n")

                else:
                    with open(save_address, "a+") as f:
                        f.write("LinuxLinux软件安装与配置题目七：文件%s不存在, ---error\n" % linux_txt_7_2)

            else:
                with open(save_address, "a+") as f:
                    f.write("LinuxLinux软件安装与配置题目七：文件%s不存在, ---error\n" % linux_txt_7_1)

        except:
            print("Linux软件安装与配置题目七:失败")

        else:
            print("Linux软件安装与配置题目七:成功")


class Cat_score_8(object):

    @staticmethod
    def run():
        try:

            cmd_rpm = "rpm -qa|grep e2fsprogs|wc -l"
            com_ret_rpm = commands.getoutput(cmd_rpm)

            cmd_help = "extundelete --help"
            com_ret_help = commands.getoutput(cmd_help)

            with open(save_address, "a+") as f:
                if int(com_ret_rpm) == 3:
                    f.write("Linux软件安装与配置题目八：结果输出为3, ---ok\n")
                else:
                    f.write("Linux软件安装与配置题目八：结果输出不为3, ---error\n")

            with open(save_address, "a+") as f:
                if "command not found" in com_ret_help:
                    f.write("Linux软件安装与配置题目八：无帮助信息输出, ---error\n")

                else:
                    f.write("Linux软件安装与配置题目八：有帮助信息输出, ---ok\n")

        except:
            print("Linux软件安装与配置题目八:失败")

        else:
            print("Linux软件安装与配置题目八:成功")

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
