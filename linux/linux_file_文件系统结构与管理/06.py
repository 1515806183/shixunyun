#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
name = "/examdata/result/100files"

def run():
    try:
        f = open(save_address, 'w')
        # 1
        cmd_find = "find /examdata/result/ -size 100M"
        com_ret_find = commands.getoutput(cmd_find)
        if com_ret_find == "":
            f.write("Linux文件系统结构与管理题目六：没有找到100M的文件, ---error\n")
        else:
            f.write("Linux文件系统结构与管理题目六：找到100M的文件, ---ok\n")

        # 2
        if os.path.exists(name):
            f.write("Linux文件系统结构与管理题目六：文件%s存在, ---ok\n" % name)

            cmd_file = "file /examdata/result/100files/*.txt|grep empty|wc -l"
            com_ret_file = int(commands.getoutput(cmd_file))
            if com_ret_file == 100:
                f.write("Linux文件系统结构与管理题目六：文件%s文件结果总数为 %s, 等于100, ---ok\n" % (name, com_ret_file))
            else:
                f.write("Linux文件系统结构与管理题目六：文件%s文件结果总数为 %s 不等于100, ---error\n" % (name, com_ret_file))

        else:
            f.write("Linux文件系统结构与管理题目六:文件%s不存在, ---error\n" % name)
            f.write("Linux文件系统结构与管理题目六:文件%s不存在,根据题意取错误答案,结果总数不为100 ---error\n" % name)

    except:
        print("Linux文件系统结构与管理题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux文件系统结构与管理题目六:成功")
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
