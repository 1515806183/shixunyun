# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/file_right"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目七：文件%s存在, ---ok\n" % name)
        else:
            f.write("Linux目录与文件管理题目七：文件%s不存在, ---error\n" % name)

    except:
        print("Linux目录与文件管理题目七:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目七:成功")
        f.close()


if __name__ == '__main__':
    run()