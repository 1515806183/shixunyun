# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_grep = "sysctl -p 2>/dev/null |egrep 'net.ipv4.ip_local_port_range = 1024\s+65000'"
        com_ret = commands.getoutput(cmd_grep).replace(" ", "")
        if 'net.ipv4.ip_local_port_range=102465000' in com_ret:
            f.write("LINUX内核用户限制参数题目四：grep net.ipv4.ip_local_port_range = 1024 65000成功, ---ok\n")
        else:
            f.write("LINUX内核用户限制参数题目四：grep net.ipv4.ip_local_port_range = 1024 65000失败, ---error\n")

    except:
        print("LINUX内核用户限制参数题目四:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX内核用户限制参数题目四:成功")
        f.close()


if __name__ == '__main__':
    run()