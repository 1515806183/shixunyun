# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_grep = "openssl version | grep 1.0.2k"
        com_ret = commands.getoutput(cmd_grep)
        if '1.0.2k' in com_ret:
            f.write("LINUX安全加固openssl升级题目一：grep 1.0.2k成功, ---ok\n")
        else:
            f.write("LINUX安全加固openssl升级题目一：grep 1.0.2k失败, ---error\n")

    except:
        print("LINUX安全加固openssl升级题目一:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安全加固openssl升级题目一:成功")
        f.close()


if __name__ == '__main__':
    run()