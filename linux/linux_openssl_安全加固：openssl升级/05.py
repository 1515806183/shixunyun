# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_grep = "cat /etc/pam.d/login|egrep '(deny=5|unlock_time=600)'"
        com_ret = commands.getoutput(cmd_grep).replace(" ", "")
        if 'deny=5' in com_ret and 'unlock_time=600' in com_ret:
            f.write("LINUX安全加固openssl升级题目五：grep deny=5和unlock_time=600成功, ---ok\n")
        else:
            f.write("LINUX安全加固openssl升级题目五：grep deny=5和unlock_time=600失败,---error\n")

    except:
        print("LINUX安全加固openssl升级题目五:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安全加固openssl升级题目五:成功")
        f.close()


if __name__ == '__main__':
    run()