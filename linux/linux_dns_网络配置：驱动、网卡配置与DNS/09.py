# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
save_address_test = './test.txt'
linux_9_file = '/examdata/result/xtgl_08.txt'


def test_09():
    try:
        f = open(save_address, 'w')
        if os.path.exists(linux_9_file):
            f.write("LINUX系统基本组成题目九：文件%s存在, ---ok\n" % linux_9_file)
            cmd_1 = "egrep -v '^(#|$|[0-9])' /examdata/training/new_sshd|wc -l"
            cmd_2 = "egrep -v '^(#|$|[0-9])' /etc/ssh/sshd_config|wc -l"
            com_ret_1 = commands.getoutput(cmd_1)
            com_ret_2 = commands.getoutput(cmd_2)

            cmd = "cat %s" % linux_9_file
            com_ret = commands.getoutput(cmd)

            if com_ret_1 in com_ret and com_ret_2 in com_ret:
                f.write("LINUX系统基本组成题目九：检查对比输出正确, ---ok\n'")
            else:
                f.write("LINUX系统基本组成题目九：检查对比输出不正确, ---error\n'")

        else:
            f.write("LINUX系统基本组成题目九:文件%s不存在, ---error\n" % linux_9_file)
            f.write("LINUX系统基本组成题目九:文件%s不存在,无法进行过滤对比 ---error\n" % linux_9_file)

    except:
        print("LINUX安装与配置题目九:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安装与配置题目九:成功")
        f.close()


if __name__ == '__main__':
    test_09()