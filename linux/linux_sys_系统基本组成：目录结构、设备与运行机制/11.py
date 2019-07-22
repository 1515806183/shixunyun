# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/system_arch_dirs"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目十一:文件%s存在, ---ok\n" % name)
            cmd_1 = "ls / | wc -l"
            ret_1 = int(commands.getoutput(cmd_1))
            cmd_2 = "cat %s | wc -l" % name
            ret_2 = int(commands.getoutput(cmd_2))

            if ret_2 >= ret_1:
                f.write("LINUX系统基本组成题目十一：检查%s,结果正常, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目十一：检查%s,结果错误, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目十一:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目十一:文件%s不存在,无法检查输出情况, ---error\n" % name)

    except:
        print("LINUX系统基本组成题目十一:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目十一:成功")
        f.close()


if __name__ == '__main__':
    run()