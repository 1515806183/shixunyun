# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_2_1 = "/examdata/result/ping_01.sh"
linux_txt_2_2 = "/examdata/result/ping_log"


def test_02():
    try:
        # 1
        if os.path.exists(linux_txt_2_1):
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目二：文件%s存在, ---ok\n" % linux_txt_2_1)

            cmd_cat = "cat /examdata/result/ping_01.sh|grep '192.168.31.'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if "192.168.31." in com_ret_cat:
                    f.write("Linux命令与SHELL题目二：192.168.31.在文件中, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目二：192.168.31.不在文件中, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在, ---error\n" % linux_txt_2_1)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在,grep 192.168.31. 失败 ---error\n" % linux_txt_2_1)

        # 2
        if os.path.exists(linux_txt_2_2):
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s存在, ---ok\n" % linux_txt_2_2)

            cmd_cat = "head -n 5 /examdata/result/ping_log | grep '100%'"
            com_ret_cat = commands.getoutput(cmd_cat).replace(" ", "").lower()
            with open(save_address, "a+") as f:
                if "100%packetloss" in com_ret_cat:
                    f.write("Linux命令与SHELL题目二：100% packet loss过滤成功, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目二：100% packet loss过滤失败, ---error\n")
        else:
            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在, ---error\n" % linux_txt_2_2)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目二：文件%s不存在,100 packet loss过滤失败 ---error\n" % linux_txt_2_2)

    except:
        print("Linux命令与SHELL题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux命令与SHELL题目二:成功")


if __name__ == '__main__':
    test_02()