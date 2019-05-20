# -*- coding: utf-8 -*-
import commands
import os
# 保存正式score文件
save_address = "./score.txt"
# 测试文件
save_address_test = './test.txt'

linux_txt_1 = "/examdata/result/date_ago.txt"


def test_01():
    try:
        if os.path.exists(linux_txt_1):
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目一：文件%s存在, ---ok\n" % linux_txt_1)

            cmd = "date +%F -d '-100 days'"
            com_ret = commands.getoutput(cmd)
            cmd = "cat /examdata/result/date_ago.txt"
            cmd_ret_txt = commands.getoutput(cmd)

            with open(save_address, "a+") as f:
                if com_ret in cmd_ret_txt:
                    f.write("Linux常用服务配置题目一：输出一致, ---ok\n")
                else:
                    f.write("Linux常用服务配置题目一：输出不一致, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目一：文件%s不存在, ---error\n" % linux_txt_1)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目一：文件%s不存在,无法进行对比输出, ---error\n" % linux_txt_1)
    except:
        print("Linux常用服务配置题目一:\033[0;34m失败\033[0m")

    else:
        print("Linux常用服务配置题目一:成功")


if __name__ == '__main__':
    test_01()