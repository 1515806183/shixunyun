# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/dir"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目十七：文件%s存在, ---ok\n" % name)
            cmd_cat = "ls -ld %s|egrep '(user01\sadmin)'" % name
            com_ret_cat = commands.getoutput(cmd_cat)

            if com_ret_cat != "":
                f.write("Linux目录与文件管理题目十七：文件%s 属主属组设置正确, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目十七：文件%s 属主属组设置错误, ---error\n" % name)
        else:
            f.write("Linux目录与文件管理题目十七：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目十七：文件%s不存在,无法查看属主属组设置 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目十七:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十七:成功")
        f.close()


if __name__ == '__main__':
    run()