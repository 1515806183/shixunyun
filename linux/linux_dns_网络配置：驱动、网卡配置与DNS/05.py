# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_5 = "/examdata/training/exame_server_status.sh"


def test_05():
    try:
        if os.path.exists(linux_txt_5):
            with open(save_address, 'w') as f:
                f.write("LINUX系统基本组成题目五：文件%s存在, ---ok\n" % linux_txt_5)
            cmd_cat = "crontab -l|egrep '(\*/1.*exame_server_status.sh)' --color=auto"
            com_ret = commands.getoutput(cmd_cat)
            num_1 = re.findall(r"\*/1\s+15\s+\*\s+\*\s+1-5\s+root\s+sh\s+%s" % linux_txt_5 , com_ret)
            num_2 = re.findall(r"\*\s+15\s+\*\s+\*\s+1-5\s+root\s+sh\s+%s" % linux_txt_5 , com_ret)
            with open(save_address, 'a+') as f:
                if num_1 or num_2:
                    f.write("LINUX系统基本组成题目五：执行命令输出正确, ---ok" + '\n')
                else:
                    f.write("LINUX系统基本组成题目五：执行命令输出不正确, ---error" + '\n')

        else:
            with open(save_address, 'w') as f:
                f.write("LINUX系统基本组成题目五：文件%s不存在, ---error\n" % linux_txt_5)

            with open(save_address, 'a+') as f:
                f.write("LINUX系统基本组成题目五：文件%s不存在,无法进行过滤查询 ---error\n" % linux_txt_5)

    except:
        print("LINUX系统基本组成题目五:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目五:成功")


if __name__ == '__main__':
    test_05()