# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/html"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目八：文件%s存在, ---ok\n" % name)

            cmd_find = "ls -Zld %s|grep 'httpd_sys_content_t'" % name
            com_ret_find = commands.getoutput(cmd_find).lower()

            if "httpd_sys_content_t" in com_ret_find:
                f.write("Linux文件系统结构与管理题目八：过滤出httpd_sys_content_t, ---ok\n")
            else:
                f.write("Linux文件系统结构与管理题目八：没有过滤出httpd_sys_content_t, ---error\n")

        else:
            f.write("Linux文件系统结构与管理题目八:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目八:文件%s不存在,无法过滤httpd_sys_content_t ---error\n" % name)

    except:
        print("Linux文件系统结构与管理题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目八:成功")
        f.close()


if __name__ == '__main__':
    run()