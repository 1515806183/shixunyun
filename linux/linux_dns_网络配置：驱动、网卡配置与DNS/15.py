# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "./score.txt"
file_name = "/boot/grub/grub.conf"


def test_14():
    try:
        f = open(save_address, 'w')
        cmd = "cat %s | grep timeout" % file_name
        ret = commands.getoutput(cmd)
        ret = int(re.findall(r'\d+', ret)[0])

        if ret == 10:
            f.write("LINUX系统基本组成题目十五：系统在引导菜单停留的时间为: %s秒, ---ok\n" % ret)
        else:
            f.write("LINUX系统基本组成题目十五：系统在引导菜单停留的时间为: %s秒, ---error\n" % ret)

    except:
        print("LINUX系统基本组成题目十五:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目十五:成功")
        f.close()


if __name__ == '__main__':
    test_14()