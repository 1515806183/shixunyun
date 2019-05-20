# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_3 = '10.10.10.9'


def test_03():
    try:
        cmd_ip = 'route -n | egrep "10.10.10.9\s+.*\s+255.255.255.0\s+UG\s+0\s+0\s+0\s+eth0"'
        com_ret = commands.getoutput(cmd_ip)
        with open(save_address, 'w') as f:
            if com_ret == "":
                f.write("LINUX系统基本组成题目三：查询路由过滤失败, ---error" + '\n')
            else:
                f.write("LINUX系统基本组成题目三：查询路由过滤成功, ---ok" + '\n')
    except:
        print("LINUX安装与配置题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安装与配置题目三:成功")


if __name__ == '__main__':
    test_03()