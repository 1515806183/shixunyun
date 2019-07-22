# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_2 = "/examdata/result/rsyslog_log_level"


def test_02():
    try:
        if os.path.exists(linux_txt_2):
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目二：文件%s存在, ---ok\n" % linux_txt_2)

            cmd_egrep = "egrep '^*\.\*' /etc/rsyslog.conf | egrep -v '@|#'"
            com_ret_egrep = commands.getoutput(cmd_egrep)

            cmd_cat = "cat %s" % linux_txt_2
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if com_ret_egrep in com_ret_cat:
                    f.write("Linux日志管理与配置题目二：输出一致, ---ok\n")
                else:
                    f.write("Linux日志管理与配置题目二：输出不一致, ---error\n")

        else:
            with open(save_address, "w") as f:
                f.write("Linux日志管理与配置题目二：文件%s不存在, ---error\n" % linux_txt_2)
                f.write("Linux日志管理与配置题目二：文件%s不存在,无法进行输出比较 ---error\n" % linux_txt_2)

    except:
        print("Linux日志管理与配置题目二:\033[0;34m失败\033[0m")
        raise
    else:
        print("Linux日志管理与配置题目二:成功")


if __name__ == '__main__':
    test_02()