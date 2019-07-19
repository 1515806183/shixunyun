# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "./score.txt"
file_name = "/etc/motd"


def test_14():
    try:
        f = open(save_address, 'w')
        cmd = "cat %s" % file_name
        ret = commands.getoutput(cmd).lower().replace(' ', '')

        str_name = "hello, welcome to login linux trainning system"
        str_name = str_name.replace(' ', '')

        if str_name in ret:
            f.write("LINUX系统基本组成题目十四：文件%s存在提示信息hello, welcome to login linux  trainning system, ---ok\n" % file_name)
        else:
            f.write("LINUX系统基本组成题目十四：文件%s不存在提示信息hello, welcome to login linux  trainning system, ---error\n" % file_name)

    except:
        print("LINUX系统基本组成题目十四:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目十四:成功")
        f.close()


if __name__ == '__main__':
    test_14()