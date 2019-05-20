# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/user20_can_write"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目六：文件%s存在, ---ok\n" % name)
            # 1
            cmd_dir = "cat %s" % name
            com_ret = commands.getoutput(cmd_dir)

            if "drwxr--rwx" in com_ret and ".ssh" in com_ret:
                f.write("Linux目录与文件管理题目六：检查文件属性内容一致, ---ok\n")
            else:
                f.write("Linux目录与文件管理题目六：检查文件属性不一致, ---error\n")

        else:
            f.write("Linux目录与文件管理题目六:文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目六:文件%s不存在,无法检查文件属性 ---error\n" % name)

    except:
        print("Linux目录与文件管理题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目六:成功")
        f.close()


if __name__ == '__main__':
    run()