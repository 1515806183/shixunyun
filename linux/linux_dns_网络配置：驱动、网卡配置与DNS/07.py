# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_7 = "/examdata/result/process_running"


def test_07():
    try:
        f = open(save_address, 'w')

        if os.path.exists(linux_txt_7):
            f.write("LINUX系统基本组成题目七：文件%s存在, ---ok\n" % linux_txt_7)
            # 1
            cmd_cat_1 = "sed -n 1p %s" % linux_txt_7
            com_ret_1 = commands.getoutput(cmd_cat_1)
            com_ret_1 = re.findall(r'\d+年\s+\d+月\s+\d+日', com_ret_1)
            if com_ret_1:
                f.write("LINUX系统基本组成题目七：日期输出在第一行, ---ok\n'")
            else:
                f.write("LINUX系统基本组成题目七：日期输出不在第一行, ---error\n'")

            # 2
            cmd_cat_2 = "sed -n 2p %s" % linux_txt_7
            com_ret_2 = commands.getoutput(cmd_cat_2)
            if com_ret_2.isdigit():
                f.write("LINUX系统基本组成题目七：第二行为进程数量, ---ok\n")
            else:
                f.write("LINUX系统基本组成题目七：第二行不为进程数量, ---error\n")

        else:
            f.write("LINUX系统基本组成题目七：文件%s不存在, ---error\n" % linux_txt_7)
            f.write("LINUX系统基本组成题目七：文件%s不存在,无法进行过滤查询 ---error\n" % linux_txt_7)

    except:
        print("LINUX系统基本组成题目七:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目七:成功")
        f.close()


if __name__ == '__main__':
    test_07()