# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/training/sam.txt"
name_1 = "/examdata/result/jack.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目三：文件%s存在, ---ok\n" % name)
        else:
            f.write("Linux目录与文件管理题目三:文件%s不存在, ---error\n" % name)

        if os.path.exists(name_1):
            f.write("Linux性能诊断与调优题目三：文件%s存在, ---ok\n" % name_1)
        else:
            f.write("Linux目录与文件管理题目三:文件%s不存在, ---error\n" % name_1)

    except:
        print("Linux目录与文件管理题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目三:成功")
        f.close()


if __name__ == '__main__':
    run()