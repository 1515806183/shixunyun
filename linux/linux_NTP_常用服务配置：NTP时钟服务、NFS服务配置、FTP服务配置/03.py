# -*- coding: utf-8 -*-
import commands
import os, re
# 保存正式score文件
save_address = "./score.txt"
# 测试文件
save_address_test = './test.txt'
linux_txt_3 = "/etc/ntp.conf"


def test_03():
    try:
        if os.path.exists(linux_txt_3):
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_data = "egrep 'server[[:space:]]+10.10.10.12' /etc/ntp.conf"
            com_ret_data = commands.getoutput(cmd_data)

            with open(save_address, "a+") as f:
                if com_ret_data == "":
                    f.write("Linux常用服务配置题目三：不存在配置server 10.10.10.12, ---error\n")
                else:
                    f.write("Linux常用服务配置题目三：存在配置server 10.10.10.12, ---ok\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目三：文件%s不存在, ---error\n" % linux_txt_3)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目三：文件%s不存在, 无法查询配置server 10.10.10.12, ---error\n" % linux_txt_3)

    except:
        print("Linux常用服务配置题目三:\033[0;34m失败\033[0m")

    else:
        print("Linux常用服务配置题目三:成功")


if __name__ == '__main__':
    test_03()