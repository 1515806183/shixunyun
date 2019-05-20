# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/list_file"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目四：文件%s存在, ---ok\n" % name)
            # 1
            cmd_txt = "ll -a / >/a.txt"
            commands.getoutput(cmd_txt)
            # 2
            cmd_jack = "diff /a.txt %s" % name
            com_ret = commands.getoutput(cmd_jack)

            if com_ret == "":
                f.write("Linux目录与文件管理题目四：文件%s跟/目录下文件一致, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目四：文件%s跟/目录下文件不一致, ---error\n" % name)

        else:
            f.write("Linux目录与文件管理题目四:文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目四:文件%s不存在,无法比较是否一致 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目四:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目四:成功")
        f.close()


if __name__ == '__main__':
    run()