# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_6 = "/examdata/result/rpmbuild_package_install.log"


def test_06():
    try:
        # 1
        if os.path.exists(linux_txt_6):
            with open(save_address, "w") as f:
                f.write("Linux软件安装与配置题目六：文件%s存在, ---ok\n" % linux_txt_6)
            cmd_cat = "cat %s|grep rpm-build" % linux_txt_6
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            with open(save_address, "a+") as f:
                if "rpm-build" in com_ret_cat:
                    f.write("Linux软件安装与配置题目六：过滤 rpm-build正确, ---ok\n")
                else:
                    f.write("Linux软件安装与配置题目六：过滤 rpm-build错误, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("LinuxLinux软件安装与配置题目六：文件%s不存在, ---error\n" % linux_txt_6)

            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目六：文件%s不存在,无法过滤 rpm-build ---error\n" % linux_txt_6)

    except:
        print("Linux软件安装与配置题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目六:成功")


if __name__ == '__main__':
    test_06()