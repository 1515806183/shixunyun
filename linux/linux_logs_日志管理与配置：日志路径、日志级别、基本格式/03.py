# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_3 = "/examdata/result/mail.log"


def test_03():
    try:
        if os.path.exists(linux_txt_3):
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目三：文件%s存在, ---ok\n" % linux_txt_3)

            cmd_egrep = "egrep '^mail.*[[:space:]]+-/examdata/result/mail.log' /etc/rsyslog.conf"
            com_ret_egrep = commands.getoutput(cmd_egrep)

            with open(save_address, "a+") as f:
                if com_ret_egrep == "":
                    f.write("Linux日志管理与配置题目三：查看 mail.*级别日志失败, ---error\n")

                else:
                    f.write("Linux日志管理与配置题目三：查看  mail.*级别日志成功, ---ok\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目三：文件%s不存在, ---error\n" % linux_txt_3)

            with open(save_address, "a+") as f:
                f.write("Linux日志管理与配置题目三：文件%s不存在,无法查询 mail.*级别日志 ---error\n" % linux_txt_3)

    except:
        print("Linux日志管理与配置题目三:\033[0;34m失败\033[0m")
        raise
    else:
        print("Linux日志管理与配置题目三:成功")


if __name__ == '__main__':
    test_03()