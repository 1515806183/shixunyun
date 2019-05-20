# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'


def test_07():
    try:
        cmd_df = "df|grep ext3|grep '/test'"
        com_ret_df = commands.getoutput(cmd_df)

        with open(save_address, "w") as f:
            if "test" in com_ret_df:
                f.write("Linux磁盘存储管理题目七：过滤出信息test, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目七：没有过滤出信息test, ---error\n")

    except:
        print("Linux磁盘存储管理题目七:失败")

    else:
        print("Linux磁盘存储管理题目七:成功")


if __name__ == '__main__':
    test_07()