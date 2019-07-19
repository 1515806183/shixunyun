# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/new_messages/empty1"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目十一：文件%s存在, ---ok\n" % name)
            # 1
            cmd_messages = "ls -l /tmp/empty1 |  awk '{print $9 $10  $11}'"
            com_ret_messages = commands.getoutput(cmd_messages)
            if '/tmp/empty1->/examdata/result/new_messages/empty1' in com_ret_messages:
                f.write("Linux目录与文件管理题目十一：软链接到/tmp目录下成功, ---ok\n")

                # 2
                cmd_empty = "ls -l /tmp/empty1 | awk '{print $3, $4}'"
                com_ret_empty_a = commands.getoutput(cmd_empty).lower().replace(" ", "")

                cmd_empty = "ls -l %s | awk '{print $3 $4}'" % name
                com_ret_empty_b = commands.getoutput(cmd_empty).lower().replace(" ", "")

                if com_ret_empty_a == com_ret_empty_b:
                    f.write("Linux目录与文件管理题目十一：文件%s组主和属组一致, ---ok\n" % name)
                else:
                    f.write("Linux目录与文件管理题目十一：文件%s组主和属组不一致, ---error\n" % name)

            else:
                f.write("Linux目录与文件管理题目十一：软链接到/tmp目录下是吧, ---error\n")
                f.write("Linux目录与文件管理题目十一：文件%s组主和属组不一致, ---error\n" % name)

        else:
            f.write("Linux目录与文件管理题目十一：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目十一：文件%s不存在,无法查看软连接 ---error\n" % name)
            f.write("Linux目录与文件管理题目十一：文件%s不存在,无法查看属组 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目十一:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十一:成功")
        f.close()


if __name__ == '__main__':
    run()