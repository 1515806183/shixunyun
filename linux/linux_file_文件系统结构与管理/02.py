# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/boot_bak*"


def run():
    try:
        f = open(save_address, 'w')
        cmd = "ls %s" % name
        ret = commands.getoutput(cmd)

        if ret:
            f.write("Linux文件系统结构与管理题目二:备份文件%s存在, ---ok\n" % ret)
        else:
            f.write("Linux文件系统结构与管理题目二:备份文件%s不存在, ---error\n" % ret)

    except:
        print("Linux文件系统结构与管理题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目二:成功")
        f.close()


if __name__ == '__main__':
    run()