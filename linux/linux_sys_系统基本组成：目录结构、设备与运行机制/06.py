# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/jichu06_conf"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目六：文件%s存在, ---ok\n" % name)
            # 1
            num = True
            cmd_find = "ls -l /etc/ssh/sshd_config %s | awk '{print $2}'" % name
            com_ret = commands.getoutput(cmd_find)
            com_ret = com_ret.split('\n')
            for ret in com_ret:
                if ret != 2:
                    num = False
                    break

            if num:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config存在超链接, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config不存在超链接, ---error\n" % name)
            # 2
            cmd_diff = "diff /etc/ssh/sshd_config %s" % name
            ret = commands.getoutput(cmd_diff)
            if not ret:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config内容一致, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目六：检查%s, /etc/ssh/sshd_config内容不一致, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目六:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行判断是否存在超链接, ---error\n" % name)
            f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行判断内容不一致, ---error\n" % name)

    except:
        print("LINUX系统基本组成题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目六:成功")
        f.close()


if __name__ == '__main__':
    run()