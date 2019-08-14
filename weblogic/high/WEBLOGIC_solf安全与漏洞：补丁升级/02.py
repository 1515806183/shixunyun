#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = '安全与漏洞题目二'
test_vlu = '检查是否存在config.xml相关备份文件'
test_vlu2 = '检查bsu.sh文件，-Xms后面参数是否大于10m'
test_vlu3 = '检查bsu.sh文件，-Xmx后面参数是否大于20m'
test_vlu4 = '检查输出Patch ID: EJUW'

save_address = "/tmp/score.txt"
name = "find /weblogic/user_projects/domains/test_domain1/config/ -name 'config.xml*' | wc -l"
name_2 = "/weblogic/utils/bsu/bsu.sh"
name_4 = "cd /weblogic/utils/bsu/ && bsu.sh -prod_dir=/weblogic/wlserver_10.3 -status=applied -verbose -view"


def run():
    f = open(save_address, 'w')
    # 1 相关备份文件
    cmd = "%s" % name
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret > 1:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = "cat %s | grep 'Xms'" % name_2
    com_ret = commands.getoutput(cmd)
    Xms = int(com_ret.split('-Xms')[1].split('m')[0])
    Xmx = int(com_ret.split('Xmx')[1].split('m')[0])

    if Xms > 10:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))
    # 3
    if Xmx > 20:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

    # 4
    cmd = "%s" % name_4
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "Patch ID: EJUW".lower().replace(" ", "") in com_ret:
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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()