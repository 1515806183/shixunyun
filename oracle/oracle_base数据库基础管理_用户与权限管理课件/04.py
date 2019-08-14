#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = '用户与角色管理课件题目四'
test_vlu = '查询命令'

save_address = "/tmp/score.txt"
name = "/examdata/result/reset_password.sql"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "alter user dbuser1 identified by".lower().replace(" ", "") in com_ret\
                and "alter user dbuser2 identified by".lower().replace(" ", "") in com_ret\
                and "alter user dbuser2 identified by".lower().replace(" ", "") in com_ret:
            f.write("%s:查看文件%s %s正确 ---ok\n" % (test_name, name, test_vlu))
        else:
            f.write("%s:查看文件%s %s错误 ---error\n" % (test_name, name, test_vlu))

    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))


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
