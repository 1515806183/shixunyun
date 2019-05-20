# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/partation_table"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目七：文件%s存在, ---ok\n" % name)

            cmd_find = "file /examdata/result/partation_table |grep startsector"
            com_ret_find = commands.getoutput(cmd_find).lower()

            if "startsector" in com_ret_find:
                f.write("Linux文件系统结构与管理题目七：过滤出startsector, ---ok\n")
            else:
                f.write("Linux文件系统结构与管理题目七：没有过滤出startsector, ---error\n")


        else:
            f.write("Linux文件系统结构与管理题目七:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目七:文件%s不存在,无法过滤对比 ---error\n" % name)

    except:
        print("Linux文件系统结构与管理题目七:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目七:成功")
        f.close()


if __name__ == '__main__':
    run()