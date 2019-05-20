# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/resolve_dmesg_error"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX故障诊断与调整题目三：文件%s存在, ---ok\n" % name)
            cmd_grep = "cat %s|grep 'service\siptables\sstop'" % name
            com_ret = commands.getoutput(cmd_grep).replace(" ", "")
            if 'serviceiptablesstop' in com_ret:
                f.write("LINUX故障诊断与调整题目三：grep service iptables stop成功, ---ok\n")
            else:
                f.write("LINUX故障诊断与调整题目三：grep service iptables stop失败, ---error\n")

        else:
            f.write("LINUX故障诊断与调整题目三：文件%s不存在, ---error\n" % name)
            f.write("LINUX故障诊断与调整题目三：文件%s不存在,grep service iptables stop失败 ---error\n" % name)

    except:
        print("LINUX故障诊断与调整题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX故障诊断与调整题目三:成功")
        f.close()


if __name__ == '__main__':
    run()