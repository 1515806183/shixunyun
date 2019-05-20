# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/100files"

def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_find = "find /examdata/result/ -size 100M"
        com_ret_find = commands.getoutput(cmd_find)
        if com_ret_find == "":
            f.write("Linux文件系统结构与管理题目六：没有找到100M的文件, ---error\n")
        else:
            f.write("Linux文件系统结构与管理题目六：找到100M的文件, ---ok\n")

        # 2
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目六：文件%s存在, ---ok\n" % name)

            cmd_file = "file /examdata/result/100files/*.txt|grep empty|wc -l"
            com_ret_file = int(commands.getoutput(cmd_file))
            if com_ret_file == 100:
                f.write("Linux文件系统结构与管理题目六：文件%s文件结果总数为 %s, 等于100, ---ok\n" % (name, com_ret_file))
            else:
                f.write("Linux文件系统结构与管理题目六：文件%s文件结果总数为 %s 不等于100, ---error\n" % (name, com_ret_file))

        else:
            f.write("Linux文件系统结构与管理题目六:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目六:文件%s不存在,根据题意取错误答案,结果总数不为100 ---error\n" % name)

    except:
        print("Linux文件系统结构与管理题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目六:成功")
        f.close()


if __name__ == '__main__':
    run()