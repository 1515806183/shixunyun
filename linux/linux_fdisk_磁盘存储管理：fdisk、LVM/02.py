#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, re
test_name = 'Linux磁盘存储管理题目二'
save_address = "/tmp/score.txt"

test_vlu = 'grep vg_exam'
test_vlu1 = '大小在150M~160M之间'
test_vlu2 = '过滤/examdata/result/exam_lvm'


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "lsblk | grep vg_exam | wc -l"
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret == 2:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = "df -hP | grep vg_exam | awk '{print $2}'"
    com_ret = commands.getoutput(cmd)
    if com_ret:
        ret = int(re.match(r'\d+', com_ret).group())
        if 150 <= ret <= 160:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

    # 3
    cmd = "df -hP | grep vg_exam | awk '{print $6}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if '/examdata/result/exam_lvm' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))


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

    print total_score


if __name__ == '__main__':
    run()
