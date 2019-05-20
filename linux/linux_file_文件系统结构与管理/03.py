# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/"


def run():
    try:
        f = open(save_address, 'w')
        cmd = "ls %s" % name
        ret = commands.getoutput(cmd)
        ret_tar = re.search(r'backup_varlog.*', ret)
        if ret_tar is not None:
            ret_tar = ret_tar.group()
            f.write("Linux文件系统结构与管理题目三:备份文件%s存在, ---ok\n" % ret_tar)
            cmd_tar = "tar -zxvf %s/%s -C %s" % (name, ret_tar, name)
            commands.getoutput(cmd_tar)

            cmd_diff = "ls /var/log/*.log|wc -l"
            ret_1 = commands.getoutput(cmd_diff)
            cmd_diff = "ls /examdata/result/*.log|wc -l"
            ret_2 = commands.getoutput(cmd_diff)

            if ret_1 == ret_2:
                f.write("Linux文件系统结构与管理题目三：目录文件对比输出一致, ---ok\n")
            else:
                f.write("Linux文件系统结构与管理题目三：目录文件对比输出一致, ---error\n")

        else:
            f.write("Linux文件系统结构与管理题目三:备份文件不存在, ---error\n")
            f.write("Linux文件系统结构与管理题目三:备份文件不存在, 无法进行对比 ---error\n")

    except:
        print("Linux文件系统结构与管理题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目三:成功")
        f.close()


if __name__ == '__main__':
    run()