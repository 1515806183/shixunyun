# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/system_character"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目八:文件%s存在, ---ok\n" % name)
            cmd = "cat %s" % name
            ret = commands.getoutput(cmd).lower()
            if "en_US.UTF-8".lower() in ret or "en_US.UTF8".lower() in ret:
                f.write("LINUX系统基本组成题目八：检查%s,字符集, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目八：检查%s,字符集, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目八:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目八:文件%s不存在,无法检查字符集, ---error\n" % name)

    except:
        print("LINUX系统基本组成题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目八:成功")
        f.close()


if __name__ == '__main__':
    run()