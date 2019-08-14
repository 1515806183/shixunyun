#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目五'
save_address = "/tmp/score.txt"
txt_one = '/etc/yum.repos.d/extundelete.repo'

test_vlu = 'grep "baseurl=file:///examdata/soft.iso/extundelete"'
test_vlu1 = 'grep extundelete'


def run():
    f = open(save_address, 'w')
    if os.path.exists(txt_one):
        f.write("%s:文件%s存在 ---ok\n" % (test_name, txt_one))
        # 1
        cmd = 'cat %s | grep "baseurl=file:///examdata/soft.iso/extundelete"' % txt_one
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if 'baseurl=file:///examdata/soft.iso/extundelete' in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
    else:
        f.write("%s:文件%s不存在 ---error\n" % (test_name, txt_one))
        f.write("%s:文件%s不存在, 无法进行grep ---error\n" % (test_name, txt_one))

    # 2
    cmd = 'yum repolist|grep extundelete'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'extundelete' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

    f.close()
    print("%s:成功" % test_name)



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
