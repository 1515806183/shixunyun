# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_3 = "/examdata/result/adduser_01.sh"


def test_03():
    try:
        # 1
        cmd_for = "for i in user{09..16};do id $i;done"
        com_ret_for = commands.getoutput(cmd_for).lower()
        with open(save_address, "w") as f:
            if "No such user".lower() in com_ret_for or "无此用户" in com_ret_for:
                f.write("Linux命令与SHELL题目三：检查用户是否创建了,没有创建用户, ---error\n")
            else:
                f.write("Linux命令与SHELL题目三：检查用户是否创建了,创建用户, ---ok\n")
        # 2
        if os.path.exists(linux_txt_3):
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_for = "egrep 'passwd\s+--stdin' %s" % linux_txt_3
            com_ret_for = commands.getoutput(cmd_for)

            with open(save_address, "a+") as f:

                if "" not in com_ret_for:
                    f.write("Linux命令与SHELL题目三：过滤passwd成功, ---ok\n")

                else:
                    f.write("Linux命令与SHELL题目三：过滤passwd失败, ---error\n")
        else:
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目三：文件%s不存在, ---error\n" % linux_txt_3)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目三：文件%s不存在,无法过滤passwd ---error\n" % linux_txt_3)


    except:
        print("Linux命令与SHELL题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux命令与SHELL题目三:成功")


if __name__ == '__main__':
    test_03()