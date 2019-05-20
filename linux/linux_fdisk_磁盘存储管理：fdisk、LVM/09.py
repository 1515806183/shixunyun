# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re

save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_9 = "/dev/raw/raw1"


def test_09():
    try:
        cmd_ls = "ls /dev/raw/raw｛1..4}"
        com_ret_ls = commands.getoutput(cmd_ls)
        with open(save_address, "w") as f:
            if "ls:" in com_ret_ls or "没有那个文件或目录" in com_ret_ls:
                f.write("Linux磁盘存储管理题目九：查看｛1..4}错误, ---error\n")

            else:
                f.write("Linux磁盘存储管理题目九：查看｛1..4}正确, ---ok\n")

        if os.path.exists(linux_txt_9):
            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目九：文件%s存在, ---ok\n" % linux_txt_9)

            cmd_ll = "ll /dev/raw/raw1|grep oracle|grep oinstall"
            com_ret_ll = commands.getoutput(cmd_ll)

            with open(save_address, "a+") as f:
                if "oinstall" in com_ret_ll:
                    f.write("Linux磁盘存储管理题目九：grep 到oinstall正确, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目九：没有grep 到oinstall错误, ---error\n")

        else:
            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目九:文件%s不存在, ---error\n" % linux_txt_9)
            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目九:文件%s不存在,查询oinstall失败 ---error\n" % linux_txt_9)

    except:
        print("Linux磁盘存储管理题目九:失败")

    else:
        print("Linux磁盘存储管理题目九:成功")


if __name__ == '__main__':
    test_09()