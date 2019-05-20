# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/training/wenjian.sh"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目一：文件%s存在, ---ok\n" % name)
            # 1
            cmd_ll = "ls -l /examdata/training/wenjian.sh |grep -E '(-rwxrwxr--)'"
            com_ret_ll = commands.getoutput(cmd_ll)
            if com_ret_ll:
                f.write("Linux目录与文件管理题目一：文件%s其权限属性为-rwxrwxr--, ---ok\n" % name)
            else:
                f.write("Linux目录与文件管理题目一：文件%s其权限属性不为-rwxrwxr--, ---error\n" % name)

        else:
            f.write("Linux目录与文件管理题目一:文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目一:文件%s不存在,无法查询文件属性 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目一:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目一:成功")
        f.close()


if __name__ == '__main__':
    run()