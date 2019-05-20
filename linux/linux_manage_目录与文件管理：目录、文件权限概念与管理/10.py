# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')

        cmd_dir = "ls -F /examdata/result/ | grep ^dir_level.*/$ | wc -l"
        com_ret = int(commands.getoutput(cmd_dir))
        if com_ret == 5:
            f.write("Linux目录与文件管理题目十：目录前缀为dir_level的数量为:%s, ---ok\n" % com_ret)
        else:
            f.write("Linux目录与文件管理题目十：目录前缀为dir_level的数量为:%s, ---error\n" % com_ret)


    except:
        print("Linux目录与文件管理题目十:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目十:成功")
        f.close()


if __name__ == '__main__':
    run()