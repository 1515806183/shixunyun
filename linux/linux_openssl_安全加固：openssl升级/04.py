# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_grep = "sysctl -p|grep 'net.ipv4.tcp_syncookies = 1'"
        com_ret = commands.getoutput(cmd_grep).replace(" ", "")
        if 'net.ipv4.tcp_syncookies=1' in com_ret:
            f.write("LINUX安全加固openssl升级题目四：grep net.ipv4.tcp_syncookies=1成功, ---ok\n")
        else:
            f.write("LINUX安全加固openssl升级题目四：grep net.ipv4.tcp_syncookies=1失败,---error\n")

    except:
        print("LINUX安全加固openssl升级题目四:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安全加固openssl升级题目四:成功")
        f.close()


if __name__ == '__main__':
    run()