# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/"
name1 = "/examdata/result/file_right"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_dir = "ls -d %s | grep rwxrwxrwt --color=auto " % name
        com_ret = commands.getoutput(cmd_dir)

        if "rwxrwxrwt" in com_ret:
            f.write("Linux目录与文件管理题目七：/examdata/result目录的权限为1777, ---ok\n")

            if os.path.exists(name1):
                f.write("Linux目录与文件管理题目七：文件%s存在, ---ok\n" % name1)

            else:
                f.write("Linux目录与文件管理题目七：文件%s不存在, ---error\n" % name1)


        else:
            f.write("Linux目录与文件管理题目七：/examdata/result目录的权限不为1777, ---error\n")
            f.write("Linux目录与文件管理题目七：文件%s不存在 ---error\n" % name1)


    except:
        print("Linux目录与文件管理题目七:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目七:成功")
        f.close()


if __name__ == '__main__':
    run()