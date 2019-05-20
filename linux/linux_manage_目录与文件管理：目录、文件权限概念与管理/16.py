# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_cat = "cat /etc/shadow|grep tom|awk -F ':' '{print $3}'"
        com_ret_cat = commands.getoutput(cmd_cat)
        if '0' in com_ret_cat:
            f.write("Linux目录与文件管理题目十六：用户tom输出数据为: 0, 为0 ---ok\n")
        else:
            f.write("Linux目录与文件管理题目十六：用户tom不存在 ---error\n")

    except:
        print("Linux目录与文件管理题目十六\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十六:成功")
        f.close()


if __name__ == '__main__':
    run()