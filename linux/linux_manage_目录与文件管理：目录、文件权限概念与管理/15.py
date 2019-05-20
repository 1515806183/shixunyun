# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_cat = "cat /etc/passwd|grep hill|grep nologin"
        com_ret_cat = commands.getoutput(cmd_cat)
        if com_ret_cat == '':
            f.write("Linux目录与文件管理题目十五：没有查询到用户hill, ---error\n")
        else:
            f.write("Linux目录与文件管理题目十五：查询到用户%s, ---ok\n" % com_ret_cat)

    except:
        print("Linux目录与文件管理题目十五\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十五:成功")
        f.close()


if __name__ == '__main__':
    run()