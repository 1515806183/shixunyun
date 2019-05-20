# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_1 = "cat /proc/sys/net/core/somaxconn"
        com_ret_1 = commands.getoutput(cmd_1)
        if "1024" in com_ret_1:
            f.write("Linux性能诊断与调优题目四：过滤输出为:%s 成功,为1024 ---ok\n" % com_ret_1)
        else:
            f.write("Linux性能诊断与调优题目四：过滤输出为:%s 失败,不为1024 ---error\n" % com_ret_1)

        # 2
        cmd_cat = "cat /etc/sysctl.conf|egrep '(net.core.somaxconn\s+=\s+1024)'"
        com_ret_cat = commands.getoutput(cmd_cat)
        if com_ret_cat:
            f.write("Linux性能诊断与调优题目四：过滤输出net.core.somaxconn = 1024成功 ---ok\n")
        else:
            f.write("Linux性能诊断与调优题目四：过滤输出net.core.somaxconn = 1024失败 ---error\n")


    except:
        print("Linux性能诊断与调优题目四:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux性能诊断与调优题目四:成功")
        f.close()


if __name__ == '__main__':
    run()