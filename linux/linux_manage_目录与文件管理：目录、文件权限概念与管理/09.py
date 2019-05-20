# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')

        cmd_dir = "getfacl /etc/passwd|grep 'user:user20:rwx'"
        com_ret = commands.getoutput(cmd_dir)
        if 'user:user20:rwx' in com_ret:
            f.write("Linux目录与文件管理题目九：grep user:user20:rwx,有正常结果返回, ---ok\n")
        else:
            f.write("Linux目录与文件管理题目九：grep user:user20:rwx,没有正常结果返回, ---error\n")


    except:
        print("Linux目录与文件管理题目九:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目九:成功")
        f.close()


if __name__ == '__main__':
    run()