# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/etc/security/limits.conf"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目三：文件%s存在, ---ok\n" % name)
            cmd_1 = "cat %s|egrep '(\*\s+-\s+nofile\s+65535)'" % name
            com_ret_1 = commands.getoutput(cmd_1)
            if com_ret_1:
                f.write("Linux性能诊断与调优题目三：过滤文件描述符为65535成功, ---ok\n")
            else:
                f.write("Linux性能诊断与调优题目三：过滤文件描述符为65535失败, ---error\n")

        else:
            f.write("Linux性能诊断与调优题目三:文件%s不存在, ---error\n" % name)
            f.write("Linux性能诊断与调优题目三:文件%s不存在,无法过滤文件描述符为65535  ---error\n" % name)

    except:
        print("Linux性能诊断与调优题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux性能诊断与调优题目三:成功")
        f.close()


if __name__ == '__main__':
    run()