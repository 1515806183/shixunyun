# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/etc_size"


def test_01():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目一：文件%s存在, ---ok\n" % name)
            cmd = "du -sh /etc"
            ret = commands.getoutput(cmd)

            cmd_cat = "cat %s" % name
            ret_cat = commands.getoutput(cmd_cat)

            if ret in ret_cat:
                f.write("Linux文件系统结构与管理题目一:/etc/目录的总文件大小, ---ok\n'")
            else:
                f.write("Linux文件系统结构与管理题目一:/etc/目录的总文件大小, ---error\n'")

        else:
            f.write("Linux文件系统结构与管理题目一:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目一:文件%s不存在,无法进行过滤对比 ---error\n" % name)

    except:
        print("Linux文件系统结构与管理题目一:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目一:成功")
        f.close()


if __name__ == '__main__':
    test_01()