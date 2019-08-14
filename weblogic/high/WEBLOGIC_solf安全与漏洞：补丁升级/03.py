#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = '安全与漏洞题目三'
test_vlu = '检查输出结果Patch ID'

save_address = "/tmp/score.txt"
name = "cd /weblogic/utils/bsu/ && bsu.sh -prod_dir=/weblogic/wlserver_10.3 -status=applied -verbose -view"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % name
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if "Patch ID: EJUW".lower().replace(" ", "") in com_ret and 'ZLNA'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

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