#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = '用户与角色管理课件题目十三'
test_vlu = '查询关键信息'

save_address = "/tmp/score.txt"
name = "/examdata/result/grant_user217_priv.log"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "dba_tab_privs".lower().replace(" ", "") in com_ret or "all_tab_privs".lower().replace(" ", "") in com_ret:
            if "dba_col_privs".lower().replace(" ", "") in com_ret or "all_tab_privs".lower().replace(" ", "") in com_ret:
                f.write("%s:查看文件%s %s正确 ---ok\n" % (test_name, name, test_vlu))
            else:
                f.write("%s:查看文件%s %s错误 ---error\n" % (test_name, name, test_vlu))
        else:
            f.write("%s:查看文件%s %s错误 ---error\n" % (test_name, name, test_vlu))

    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))

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
