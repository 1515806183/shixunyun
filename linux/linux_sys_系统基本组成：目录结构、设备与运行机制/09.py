# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/ls_man_location"
file_name = "/usr/share/man/man1/ls.1.gz"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目九:文件%s存在, ---ok\n" % name)
            cmd = "cat %s" % name
            ret = commands.getoutput(cmd).lower()
            if file_name.lower() in ret:
                f.write("LINUX系统基本组成题目九：输出正确, ---ok\n")
            else:
                f.write("LINUX系统基本组成题目九：输出错误, ---error\n")

        else:
            f.write("LINUX系统基本组成题目九:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目九:文件%s不存在,无法检查输出情况, ---error\n" % name)

    except:
        print("LINUX系统基本组成题目九:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目九:成功")
        f.close()


if __name__ == '__main__':
    run()