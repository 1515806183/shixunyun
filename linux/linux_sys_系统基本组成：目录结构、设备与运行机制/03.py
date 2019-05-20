# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/df.tx"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX系统基本组成题目三：文件%s存在, ---ok\n" % name)

            cmd = "df -h | grep -n 1 | awk '{print $5}' | sed -e 's/%//g'"
            com_ret = commands.getoutput(cmd).lower()

            cmd_cat = "cat %s" % name
            com_ret_cat = commands.getoutput(cmd_cat)

            if com_ret in com_ret_cat:
                f.write("LINUX系统基本组成题目四：%s文件内容输出一致, ---ok\n" % name)
            else:
                f.write("LINUX系统基本组成题目四：%s文件内容输出不一致, ---error\n" % name)

        else:
            f.write("LINUX系统基本组成题目三:文件%s不存在, ---error\n" % name)
            f.write("LINUX系统基本组成题目三:文件%s不存在,无法进行过滤对比 ---error\n" % name)

    except:
        print("LINUX系统基本组成题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目三:成功")
        f.close()


if __name__ == '__main__':
    run()