# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"


def run():
    try:
        f = open(save_address, 'w')
        cmd_df = "df -hTP|grep '/dev/shm'|awk '{print $5}'"
        com_ret_df = commands.getoutput(cmd_df)
        ret_str = com_ret_df[-1:].lower()
        com_num = re.search(r'\d+', com_ret_df).group()
        if ret_str == 'm':
            if com_num == "4096":
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sM, 为4096M(4G) ---ok\n" % com_num)
            else:
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sM, 不为4096M(4G) ---ok\n" % com_num)
        else:
            if com_num == "4":
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sG, 为4G ---ok\n" % com_num)
            else:
                f.write("Linux文件系统结构与管理题目五：过滤出来的结果是%sG, 不为4G ---ok\n" % com_num)

    except:
        print("Linux文件系统结构与管理题目五:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目五:成功")
        f.close()


if __name__ == '__main__':
    run()