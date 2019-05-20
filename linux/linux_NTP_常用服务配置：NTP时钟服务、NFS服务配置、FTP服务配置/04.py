# -*- coding: utf-8 -*-
import commands
import os, re
# 保存正式score文件
save_address = "./score.txt"
# 测试文件
save_address_test = './test.txt'
linux_txt_4 = "/examdata/result/future_day"


def test_04():
    try:
        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目四：文件%s存在, ---ok\n" % linux_txt_4)

            cmd_data = 'date +%F -d "+20 days" '
            com_ret_data_now = commands.getoutput(cmd_data)

            cmd_cat_txt = "cat %s" % linux_txt_4
            com_ret_cat = commands.getoutput(cmd_cat_txt)

            with open(save_address, "a+") as f:
                if com_ret_data_now in com_ret_cat:
                    f.write("Linux常用服务配置题目四：跟文件%s,输出一致, ---ok\n" % linux_txt_4)
                else:
                    f.write("Linux常用服务配置题目四：跟文件%s,输出不一致, ---error\n" % linux_txt_4)

        else:
            with open(save_address, "w") as f:
                f.write("Linux常用服务配置题目四：文件%s不存在, ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux常用服务配置题目四：文件%s不存在,无法进行输出比较 ---error\n" % linux_txt_4)

    except:
        print("Linux常用服务配置题目四:\033[0;34m失败\033[0m")

    else:
        print("Linux常用服务配置题目四:成功")


if __name__ == '__main__':
    test_04()