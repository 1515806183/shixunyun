# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_6 = "/examdata/result/extend.log"


def test_06():
    try:

        cmd_df = "df -hT /|sed 's/[GgMm]//g' | awk '{print $3}'"
        com_ret_df = commands.getoutput(cmd_df)
        com_ret_df = int(re.search(r'\d+', com_ret_df).group())

        if os.path.exists(linux_txt_6):
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目六：文件%s存在, ---ok\n" % linux_txt_6)

            cmd_cat = "cat %s" % linux_txt_6
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if 37.9 < com_ret_df < 38.1:
                    f.write("Linux磁盘存储管理题目六：检查根目录的空间大小为%s, ---ok\n" % com_ret_df)
                else:
                    f.write("Linux磁盘存储管理题目六：检查根目录的空间大小为%s, ---error\n" % com_ret_df)

            with open(save_address, "a+") as f:
                if com_ret_df in com_ret_cat:
                    f.write("Linux磁盘存储管理题目六：对比输出的结果正确, ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目六：对比输出的结果错误, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux磁盘存储管理题目六：文件%s不存在, ---error\n" % linux_txt_6)

            with open(save_address, "a+") as f:
                f.write("Linux磁盘存储管理题目六：文件%s不存在,无法进行比较 ---error\n" % linux_txt_6)

    except:
        print("操作LINUX安装与配置题目六:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目六:成功")


if __name__ == '__main__':
    test_06()