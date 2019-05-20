# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_5 = "/examdata/result/vim_uninstall_log"


def test_05():
    try:
        # 1
        cmd_rpm = "rpm -qa | grep vim-common"
        com_ret_egrep = commands.getoutput(cmd_rpm).lower()


        with open(save_address, "w") as f:
            if "vim-common" in com_ret_egrep:
                f.write("Linux软件安装与配置题目五：查询vim-common, ---ok\n")
            else:
                f.write("Linux软件安装与配置题目五：查询vim-common, ---error\n")

        # 2
        if os.path.exists(linux_txt_5):
            with open(save_address, "a+") as f:
                f.write("Linux软件安装与配置题目五：文件%s存在, ---ok\n" % linux_txt_5)

            cmd_cat = "cat %s|egrep '(vim-enhanced|vim-common)'" % linux_txt_5
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            with open(save_address, "a+") as f:
                if "vim-enhanced" in com_ret_cat or "vim-common" in com_ret_cat:
                    f.write("Linux软件安装与配置题目五：查看文件%s过滤正确, ---ok\n" % linux_txt_5)
                else:
                    f.write("Linux软件安装与配置题目五：查看文件%s过滤错误, ---error\n" % linux_txt_5)

        else:
            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目五：文件%s不存在, ---error\n" % linux_txt_5)

            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目五：文件%s不存在,无法进行过滤查看 ---error\n" % linux_txt_5)

    except:
        print("Linux软件安装与配置题目五:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目五:成功")


if __name__ == '__main__':
    test_05()