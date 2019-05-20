# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_4 = "/examdata/result/httpd_deps"


def test_04():
    try:
        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("Linux软件安装与配置题目四：文件%s存在, ---ok\n" % linux_txt_4)

            cmd_cat = "cat %s|egrep '(chkconfig|apr|httpd-tools)'" % linux_txt_4
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            with open(save_address, "a+") as f:
                if "chkconfig" in com_ret_cat or "apr" in com_ret_cat or "httpd-tools" in com_ret_cat:
                    f.write("Linux软件安装与配置题目四：输出正确, ---ok\n")
                else:
                    f.write("Linux软件安装与配置题目四：输出错误, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("LinuxLinux软件安装与配置题目四：文件%s不存在, ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目四：文件%s不存在,无法查询httpd依赖哪些包 ---error\n" % linux_txt_4)


    except:
        print("Linux软件安装与配置题目四:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目四:成功")


if __name__ == '__main__':
    test_04()