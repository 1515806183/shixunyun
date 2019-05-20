# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "./score.txt"
save_address_test = './test.txt'
linux_11_file = '/examdata/result/init_files'


def test_11():
    try:
        f = open(save_address, 'w')
        if os.path.exists(linux_11_file):
            f.write("LINUX系统基本组成题目十一：文件%s存在, ---ok\n" % linux_11_file)
            cmd = "ls /etc --file-type |grep -v /$|grep ^init"
            ret = commands.getoutput(cmd)

            cmd_cat = "cat %s" % linux_11_file
            ret_cat = commands.getoutput(cmd_cat)

            if ret in ret_cat:
                f.write("LINUX系统基本组成题目十一：检查对比输出正确, ---ok\n'")
            else:
                f.write("LINUX系统基本组成题目十一：检查对比输出不正确, ---error\n'")

        else:
            f.write("LINUX系统基本组成题目十一:文件%s不存在, ---error\n" % linux_11_file)
            f.write("LINUX系统基本组成题目十一:文件%s不存在,无法进行过滤对比 ---error\n" % linux_11_file)

    except:
        print("LINUX安装与配置题目十一:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安装与配置题目十一:成功")
        f.close()


if __name__ == '__main__':
    test_11()