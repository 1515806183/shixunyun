# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_1 = "/examdata/result/apache_install_log"


def test_02():
    try:
        cmd_chkconfig = "chkconfig --list httpd| grep '3:启用'"
        com_ret_chkconfig = commands.getoutput(cmd_chkconfig)

        with open(save_address, "w") as f:
            if "3:启用" in com_ret_chkconfig:
                f.write("Linux软件安装与配置题目二：设置httpd开机启动成功, ---ok\n")

            else:
                f.write("Linux软件安装与配置题目二：设置httpd开机启动失败, ---error\n")

    except:
        print("Linux软件安装与配置题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目二:成功")


if __name__ == '__main__':
    test_02()