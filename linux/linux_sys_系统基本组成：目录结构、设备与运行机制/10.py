# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/opt/kong/sbin".lower()

def run():
    try:
        f = open(save_address, 'w')
        cmd = "echo $PATH"
        ret = commands.getoutput(cmd).lower()
        if name in ret:
            f.write(("LINUX系统基本组成题目十：检查出有%s这个路径, ---ok\n") % name)
        else:
            f.write(("LINUX系统基本组成题目十：检查出没有%s这个路径, ---error\n") % name)

    except:
        print("LINUX系统基本组成题目十:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目十:成功")
        f.close()


if __name__ == '__main__':
    run()