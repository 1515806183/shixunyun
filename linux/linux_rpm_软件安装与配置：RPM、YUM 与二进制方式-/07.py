# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_7_1 = "/mnt/Packages/mysql-server-5.1.71-1.el6.x86_64.rpm"
linux_txt_7_2 = "/examdata/result/mysql.txt"


def test_07():
    try:
        # 1
        com_ret_rpm = None
        if os.path.exists(linux_txt_7_1):
            with open(save_address, "w") as f:
                f.write("Linux软件安装与配置题目七：文件%s存在, ---ok\n" % linux_txt_7_1)
            cmd_rpm = "rpm -qpR %s" % linux_txt_7_1
            com_ret_rpm = commands.getoutput(cmd_rpm)
        else:
            with open(save_address, "w") as f:
                f.write("LinuxLinux软件安装与配置题目七：文件%s不存在, ---error\n" % linux_txt_7_1)

        # 2
        if os.path.exists(linux_txt_7_2):
            with open(save_address, "a+") as f:
                f.write("Linux软件安装与配置题目七：文件%s存在, ---ok\n" % linux_txt_7_2)

            cmd_cat = "cat %s" % linux_txt_7_2
            com_ret_cat = commands.getoutput(cmd_cat)
            with open(save_address, "a+") as f:
                if com_ret_rpm is not None:
                    if com_ret_cat in com_ret_rpm and "error" not in com_ret_rpm:
                        f.write("Linux软件安装与配置题目七：对比文件输出正确, ---ok\n")
                    else:
                        f.write("Linux软件安装与配置题目七：对比文件输出错误, ---error\n")
                else:
                    f.write("Linux软件安装与配置题目七：没有查询到mysql-server, ---error\n")

        else:
            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目七：文件%s不存在, ---error\n" % linux_txt_7_2)

            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目七：文件%s不存在,无法进行比较 ---error\n" % linux_txt_7_2)

    except:
        print("Linux软件安装与配置题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目六:成功")


if __name__ == '__main__':
    test_07()