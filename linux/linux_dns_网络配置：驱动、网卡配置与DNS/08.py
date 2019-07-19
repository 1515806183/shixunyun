# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_8 = "/examdata/training/file1"
linux_txt_8_1 = "/examdata/result/file1"


def test_08():
    try:
        f = open(save_address, 'w')

        if os.path.exists(linux_txt_8) and os.path.exists(linux_txt_8_1):
            f.write("LINUX系统基本组成题目八：文件%s, %s存在, ---ok\n" % (linux_txt_8, linux_txt_8_1))

            cmd_1 = "grep -n ^$ /examdata/training/file1"
            cmd_2 = "grep abc$ /examdata/training/file1"
            cmd_3 = "head -n 3 /examdata/training/file1"
            com_ret_1 = commands.getoutput(cmd_1)
            com_ret_2 = commands.getoutput(cmd_2)
            com_ret_3 = commands.getoutput(cmd_3)

            cmd = "cat %s" % linux_txt_8_1
            ret = commands.getoutput(cmd)

            if com_ret_1 in ret and com_ret_2 in ret and com_ret_3 in ret:
                f.write("LINUX系统基本组成题目八：检查对比输出正确, ---ok\n'")
            else:
                f.write("LINUX系统基本组成题目八：检查对比输出不正确, ---error\n'")

        else:
            f.write("LINUX系统基本组成题目八：文件%s, %s不存在, ---error\n" % (linux_txt_8, linux_txt_8_1))
            f.write("LINUX系统基本组成题目八：文件%s, %s不存在,无法进行过滤对比 ---error\n" % (linux_txt_8, linux_txt_8_1))

    except:
        print("LINUX系统基本组成题目八:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目八:成功")
        f.close()


if __name__ == '__main__':
    test_08()