# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_grep = "sysctl -p 2>/dev/null|grep 'net.ipv4.tcp_tw_reuse\s=\s1'"
        com_ret = commands.getoutput(cmd_grep).replace(" ", "")
        if 'net.ipv4.tcp_tw_reus=1' in com_ret:
            f.write("LINUX内核用户限制参数题目三：grep net.ipv4.tcp_tw_reuse = 1成功, ---ok\n")
        else:
            f.write("LINUX内核用户限制参数题目三：grep net.ipv4.tcp_tw_reuse = 1失败, ---error\n")

    except:
        print("LINUX内核用户限制参数题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX内核用户限制参数题目三:成功")
        f.close()


if __name__ == '__main__':
    run()