# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "./score.txt"


def test_12():
    try:
        f = open(save_address, 'w')
        cmd = "chkconfig  --list |grep 3:启用 | awk '{print $1}' |  sed -r 's#(.*)#chkconfig \1 off#g' | awk '{print $3}'"
        ret = commands.getoutput(cmd).lower()
        if 'off' not in ret:
            f.write("LINUX系统基本组成题目十二：检查显示几项为开启的, ---ok\n'")
        else:
            f.write("LINUX系统基本组成题目十二：检查显示几项有不开启的, ---error\n'")

    except:
        print("LINUX安装与配置题目十二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安装与配置题目十二:成功")
        f.close()


if __name__ == '__main__':
    test_12()