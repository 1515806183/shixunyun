# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/share_mem_size"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX内核用户限制参数题目二：文件%s存在, ---ok\n" % name)
            cmd_grep = "sysctl -p 2>/dev/null|grep 'kernel.shmmax\s=\s2147483648'"
            com_ret = commands.getoutput(cmd_grep).replace(" ", "")
            if 'kernel.shmmax=2147483648' in com_ret:
                f.write("LINUX内核用户限制参数题目二：grep kernel.shmmax = 2147483648成功, ---ok\n")
            else:
                f.write("LINUX内核用户限制参数题目二：grep kernel.shmmax = 2147483648失败, ---error\n")

        else:
            f.write("LINUX内核用户限制参数题目二：文件%s不存在, ---error\n" % name)
            f.write("LINUX内核用户限制参数题目二：文件%s不存在,grep kernel.shmmax = 2147483648失败 ---error\n" % name)

    except:
        print("LINUX内核用户限制参数题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX内核用户限制参数题目二:成功")
        f.close()


if __name__ == '__main__':
    run()