#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux磁盘存储管理题目四'
save_address = "/tmp/score.txt"
cat_file = '/examdata/result/mountpoint_size'
linux_one = '/examdata/result/exam_lvm'

test_vlu = "执行df -hTP /|awk 'NR >1 {print $1,$2}'命令, 对比内容"
test_vlu1 = "执行df -h /dev/shm|awk 'NR >1 {print $1,$2}'命令, 对比内容"
test_vlu2 = "执行df -h /boot|awk 'NR >1 {print $1,$2}'命令, 对比内容"
test_vlu3 = "执行df -h /examdata/result/exam_lvm |awk 'NR >1 {print $1,$2}'命令, 对比内容"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "df -hTP /|awk 'NR >1 {print $1,$2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    cmd_cat = 'cat %s' % cat_file
    cat_ret = commands.getoutput(cmd_cat).lower().replace(" ", "")

    if com_ret in cat_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = "df -h /dev/shm|awk 'NR >1 {print $1,$2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    cmd_cat = 'cat %s' % cat_file
    cat_ret = commands.getoutput(cmd_cat).lower().replace(" ", "")

    if com_ret in cat_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

    # 3
    cmd = "df -h /boot|awk 'NR >1 {print $1,$2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    cmd_cat = 'cat %s' % cat_file
    cat_ret = commands.getoutput(cmd_cat).lower().replace(" ", "")

    if com_ret in cat_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    # 4
    if os.path.exists(linux_one):
        f.write("%s:文件%s存在 ---ok\n" % (test_name, linux_one))

        cmd = "df -h /examdata/result/exam_lvm |awk 'NR >1 {print $1,$2}'"
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        cmd_cat = 'cat %s' % cat_file
        cat_ret = commands.getoutput(cmd_cat).lower().replace(" ", "")

        if com_ret in cat_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

    else:
        f.write("%s:文件%s不存在 ---error\n" % (test_name, linux_one))
        f.write("%s:文件%s不存在,无法%s ---error\n" % (test_name, linux_one, test_vlu3))

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
