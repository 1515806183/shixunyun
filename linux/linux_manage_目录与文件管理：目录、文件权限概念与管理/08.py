# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/group_exam"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目八：文件%s存在, ---ok\n" % name)

            cmd_dir = "ls -ld /examdata/result/group_exam|grep 'drwxr-s'"
            com_ret = commands.getoutput(cmd_dir)
            if 'drwxr-s' in com_ret:
                f.write("Linux目录与文件管理题目八：文件和子目录继承文件和子目录, ---ok\n")
            else:
                f.write("Linux目录与文件管理题目八：文件和子目录没有继承文件和子目录, ---error\n")

        else:
            f.write("Linux目录与文件管理题目八：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目八：文件%s不存在,无法查询继承文件和子目录 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目八:成功")
        f.close()


if __name__ == '__main__':
    run()