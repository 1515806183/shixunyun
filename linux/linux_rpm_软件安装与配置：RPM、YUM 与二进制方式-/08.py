# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_6 = "/examdata/result/rpmbuild_package_install.log"


def test_08():
    try:
        # 1
        cmd_rpm = "rpm -qa|grep e2fsprogs|wc -l"
        com_ret_rpm = int(commands.getoutput(cmd_rpm))
        with open(save_address, "w") as f:
            if com_ret_rpm == 3:
                f.write("Linux软件安装与配置题目八：结果输出为:%s 为3, ---ok\n" % com_ret_rpm)
            else:
                f.write("Linux软件安装与配置题目八：结果输出:%s 不为3, ---error\n"  % com_ret_rpm)

        # 2
        cmd_help = "extundelete --help"
        com_ret_help = commands.getoutput(cmd_help)
        with open(save_address, "a+") as f:
            if "command not found" in com_ret_help:
                f.write("Linux软件安装与配置题目八：extundelete 无帮助信息输出, ---error\n")
            else:
                f.write("Linux软件安装与配置题目八：extundelete 有帮助信息输出, ---ok\n")
    except:
        print("Linux软件安装与配置题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目八:成功")


if __name__ == '__main__':
    test_08()