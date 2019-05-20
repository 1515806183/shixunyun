# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/get_ftp_file.log"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd= "ls /home"
        ret = commands.getoutput(cmd).lower()
        if "test2" in ret:
            f.write("LINUX安全加固openssl升级题目六：用户test2存在, ---ok\n")
            cmd_diff = "diff /etc/fstab /home/test2/fstab"
            com_ret_diff = commands.getoutput(cmd_diff)
            if com_ret_diff == '':
                f.write("Linux安全加固题目六：/etc/fstab /home/test2/fstab比较两文件是一致, ---ok\n")
            else:
                f.write("Linux安全加固题目六：/etc/fstab /home/test2/fstab比较两文件不是一致, ---error\n")
        else:
            f.write("LINUX安全加固openssl升级题目六：用户test2不存在, ---error\n")
            f.write("LINUX安全加固openssl升级题目六：用户test2不存在,/etc/fstab /home/test2/fstab比较两文件无法比较 ---error\n")
        # 2
        if os.path.exists(name):
            f.write("LINUX安全加固openssl升级题目六：文件%s存在, ---ok\n" % name)
            # 2.1
            cmd_cat = "cat %s|grep 'remote:\s/etc/fstab'" % name
            com_ret_cat = commands.getoutput(cmd_cat)
            if 'remote:' in com_ret_cat and 'com_ret_cat' in com_ret_cat:
                f.write("LINUX安全加固openssl升级题目六：文件%s grep remote: /etc/fstab成功, ---ok\n" % name)
            else:
                f.write("LINUX安全加固openssl升级题目六：文件%s grep remote: /etc/fstab失败, ---error\n" % name)

            # 2.2
            cmd_cat = "cat %s |grep 'received\sin' --color=auto" % name
            com_ret_cat = commands.getoutput(cmd_cat)
            if 'received' in com_ret_cat and 'in' in com_ret_cat:
                f.write("LINUX安全加固openssl升级题目六：文件%s grep received in成功, ---ok\n" % name)
            else:
                f.write("LINUX安全加固openssl升级题目六：文件%s grep received in失败, ---error\n" % name)

        else:
            f.write("LINUX安全加固openssl升级题目六：文件%s不存在, ---error\n" % name)
            f.write("LINUX安全加固openssl升级题目六：文件%s不存在,grep remote: /etc/fstab失败 ---error\n" % name)
            f.write("LINUX安全加固openssl升级题目六：文件%s不存在,grep received in失败 ---error\n" % name)

    except:
        print("LINUX安全加固openssl升级题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安全加固openssl升级题目六:成功")
        f.close()


if __name__ == '__main__':
    run()