#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
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

    with open(save_address) as f :
        num = f.readlines()

    # 总题目数
    sum = len(num)
    # 一题多少分
    average = 100 // sum

    # 正确的题目总数
    timu_all = 0
    for i in num:
        if '---ok' in i:
                timu_all += 1
    total_score = timu_all * average

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score


if __name__ == '__main__':
    test_06()
