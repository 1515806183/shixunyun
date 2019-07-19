# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "./score.txt"


def test_12():
    try:
        f = open(save_address, 'w')
        # rsyslog、crond、network、sshd、sysstat、autofs、auditd、haldaemon、messagebus、
        cmd = "chkconfig --list | grep 3:启用 | awk '{print $1}'"
        ret = commands.getoutput(cmd).lower()
        ret_list = ret.split('\n')
        res_on = ['rsyslog', 'crond', 'network', 'sshd', 'sysstat', 'autofs', 'auditd', 'haldaemon', 'messagebus']

        set_ret_list = set(ret_list).intersection(res_on)

        if set(res_on) == set_ret_list:
            f.write("LINUX系统基本组成题目十二：检查显示几项为开启的, ---ok\n'")
        else:
            f.write("LINUX系统基本组成题目十二：检查显示几项有不开启的, ---error\n'")

    except:
        print("LINUX系统基本组成题目十二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目十二:成功")
        f.close()


if __name__ == '__main__':
    test_12()