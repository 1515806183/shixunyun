# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/fix_login_prompt.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("LINUX故障诊断与调整题目二：文件%s存在, ---ok\n" % name)
            cmd_grep = "cat %s|grep '/etc/skel/.bashrc'" % name
            com_ret = commands.getoutput(cmd_grep)
            if '/etc/skel/.bashrc' in com_ret:
                f.write("LINUX故障诊断与调整题目二：文件%s grep /etc/skel/.bashrc成功, ---ok\n" % name)
            else:
                f.write("LINUX故障诊断与调整题目二：文件%s grep /etc/skel/.bashrc失败, ---error\n" % name)

        else:
            f.write("LINUX故障诊断与调整题目二：文件%s不存在, ---error\n" % name)
            f.write("LINUX故障诊断与调整题目二：文件%s不存在,grep /etc/skel/.bashrc失败 ---error\n" % name)

    except:
        print("LINUX故障诊断与调整题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX故障诊断与调整题目二:成功")
        f.close()


if __name__ == '__main__':
    run()