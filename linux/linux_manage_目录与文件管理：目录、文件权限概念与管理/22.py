# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/admins"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目二十二：文件%s存在, ---ok\n" % name)
            # 1
            cmd_ll = "ls -ld %s | awk '{print $4}'" % name
            com_ret_ll = commands.getoutput(cmd_ll)
            if "manager" in com_ret_ll:
                f.write("Linux目录与文件管理题目二十二：文件所属组为:%s, 为manager ---ok\n" % com_ret_ll)
            else:
                f.write("Linux目录与文件管理题目二十二：文件所属组为:%s, 不为manager ---error\n" % com_ret_ll)

            # 2
            cmd_harry = "ls -ld %s|grep 'drwxrws---'" % name
            com_ret_harry = commands.getoutput(cmd_harry)
            if "drwxrws---" in com_ret_harry:
                f.write("Linux目录与文件管理题目二十二：检查文件%s权限为drwxrws---正确, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目二十二：检查文件%s权限不为drwxrws---错误, ---error\n" % name)

        else:
            f.write("Linux目录与文件管理题目二十二：文件%s不存在, ---errory\n" % name)
            f.write("Linux目录与文件管理题目二十二：文件%s不存在, 无法检查文件所属组 ---errory\n" % name)
            f.write("Linux目录与文件管理题目二十二：文件%s不存在, 无法检查文件权限 ---errory\n" % name)

    except:
        print("Linux目录与文件管理题目二十二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目二十二:成功")
        f.close()


if __name__ == '__main__':
    run()