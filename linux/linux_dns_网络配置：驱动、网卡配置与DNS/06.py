# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_6 = "/examdata/result/sysdf.log"


def test_06():
    try:
        if os.path.exists(linux_txt_6):
            with open(save_address, 'w') as f:
                f.write("LINUX系统基本组成题目六：文件%s存在, ---ok\n" % linux_txt_6)
            cmd_cat = "crontab -l|egrep '(15\s+\*\s+\*\s+\*\s+\*.*sysdf.log)' --color=auto"
            com_ret = commands.getoutput(cmd_cat)
            num = re.findall(r"15\s+\*\s+\*\s+\*\s+\*.*sysdf.log", com_ret)
            with open(save_address, 'a+') as f:
                if num:
                    f.write("LINUX系统基本组成题目六：执行命令过滤sysdf.log输出正确, ---ok" + '\n')
                else:
                    f.write("LINUX系统基本组成题目六：执行命令过滤sysdf.log输出不正确, ---error" + '\n')

        else:
            with open(save_address, 'w') as f:
                f.write("LINUX系统基本组成题目六：文件%s不存在, ---error\n" % linux_txt_6)

            with open(save_address, 'a+') as f:
                f.write("LINUX系统基本组成题目六：文件%s不存在,无法进行过滤查询 ---error\n" % linux_txt_6)

    except:
        print("LINUX系统基本组成题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目六:成功")


if __name__ == '__main__':
    test_06()