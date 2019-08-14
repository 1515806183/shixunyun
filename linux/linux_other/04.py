#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目四'
save_address = "/tmp/score.txt"
txt_one = '/examdata/soft.iso/epel-release-6-5.noarc'

test_vlu = 'grep epel-release-6-5.noarch'


def run():
    f = open(save_address, 'w')
    if os.path.exists(txt_one):
        f.write("%s:文件%s存在 ---ok\n" % (test_name, txt_one))
        # 1
        cmd = 'rpm -qa|grep epel-release-6-5.noarch'
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if 'epel-release-6-5.noarch' in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s不存在 ---error\n" % (test_name, txt_one))
        f.write("%s:文件%s不存在, 无法进行grep ---error\n" % (test_name, txt_one))

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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
