# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/user08.sh"


def run():
    try:
        f = open(save_address, 'w')

        cmd_cat = "cat /etc/passwd | grep '^stu' | awk -F ':' '{print $1}'"
        com_ret_cat = commands.getoutput(cmd_cat)
        if com_ret_cat:
            com_ret_cat = com_ret_cat.split('\n')
            if len(com_ret_cat) == 10:
                f.write("Linux目录与文件管理题目十九：文件%s,用户stu01-stu10存在, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目十九：文件%s,用户stu01-stu10不存在, ---error\n" % name)
        else:
            f.write("Linux目录与文件管理题目十九：文件%s,用户stu01-stu10不存在, ---error\n" % name)

    except:
        print("Linux目录与文件管理题目十九:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十九:成功")
        f.close()


if __name__ == '__main__':
    run()