#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/result/num_users"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目二十：文件%s存在, ---ok\n" % name)
            cmd_grep = "grep -v 'nologin' /etc/passwd|awk -F ':' '{print $1}' | wc -l"
            com_ret_grep = int(commands.getoutput(cmd_grep))
            cmd_cat = "cat %s | wc -l" % name
            com_ret_cat = int(commands.getoutput(cmd_cat))

            if com_ret_grep == com_ret_cat:
                f.write("Linux目录与文件管理题目二十：系统上允许登陆的用户有 %s个,与输出文件%s内容一致, ---ok\n" % (com_ret_grep, name))
            else:
                f.write("Linux目录与文件管理题目二十：系统上允许登陆的用户有 %s个,与输出文件%s内容不一致, ---ok\n" % (com_ret_grep, name))


        else:
            f.write("Linux目录与文件管理题目二十：文件%s不存在, ---errory\n" % name)
            f.write("Linux目录与文件管理题目二十：文件%s不存在, 无法对比查询内容 ---errory\n" % name)


    except:
        print("Linux目录与文件管理题目二十:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux目录与文件管理题目二十:成功")
        f.close()



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
    run()
