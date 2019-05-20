# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_4 = "/examdata/result/function.sh"


def test_04():
    try:
        if os.path.exists(linux_txt_4):
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目四：文件%s存在, ---ok\n" % linux_txt_4)

            # 1
            cmd_egrep = "egrep .*\(\) %s" % linux_txt_4
            com_ret_egrep = commands.getoutput(cmd_egrep)

            with open(save_address, "a+") as f:
                if com_ret_egrep == '':
                    f.write("Linux命令与SHELL题目四：egrep .*\(\)失败, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目四：egrep .*\(\)成功, ---error\n")

            # 2
            cmd_cat = "cat  /examdata/result/function.sh|egrep '(\$1|\$2)'"
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            with open(save_address, "a+") as f:
                if "$1" in com_ret_cat and "$2" in com_ret_cat:
                    f.write("Linux命令与SHELL题目四：过滤$1,$2成功, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目四：过滤$1,$2失败, ---error\n")

            # 3
            cmd_cat = "cat  /examdata/result/function.sh|egrep  '(51|52)'"
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            with open(save_address, "a+") as f:
                if 'return' in com_ret_cat:
                    f.write("Linux命令与SHELL题目四：过滤return成功, ---ok\n")
                else:
                    f.write("Linux命令与SHELL题目四：过滤return失败, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux命令与SHELL题目四：文件%s不存在, ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目四：文件%s不存在,egrep .*\(\)失败 ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目四：文件%s不存在,过滤$1,$2失败 ---error\n" % linux_txt_4)

            with open(save_address, "a+") as f:
                f.write("Linux命令与SHELL题目四：文件%s不存在,过滤return失败 ---error\n" % linux_txt_4)


    except:
        print("Linux命令与SHELL题目四:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux命令与SHELL题目四:成功")


if __name__ == '__main__':
    test_04()