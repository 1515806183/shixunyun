#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = '配置文件参数调整题目四'
test_vlu = '检查是否存在commEnv.sh相关备份文件'
test_vlu2 = '检查commEnv.sh是否存在参数'
test_vlu3 = '检查是否存在setDomainEnv.sh相关备份文件'
test_vlu4 = '检查setDomainEnv.sh是否存在参数'

save_address = "/tmp/score.txt"
name = "find /weblogic/wlserver_10.3/common/bin/ -name 'commEnv.sh*' | wc -l"
name1 = "/weblogic/wlserver_10.3/common/bin/commEnv.sh"
name2 = "find /weblogic/wlserver_10.3/common/bin/ -name 'commEnv.sh*' | wc -l"
name3 = "/weblogic/wlserver_10.3/common/bin/commEnv.sh"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % name
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret > 1:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    cmd = "cat %s" % name1
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "Sun)".lower().replace(" ", "") in com_ret\
            and "JAVA_VM=-server".lower().replace(" ", "") in com_ret \
            and 'MEM_ARGS="-Xms32m -Xmx200m -XX:MaxPermSize=259m"'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    # 2
    cmd = "%s" % name2
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret > 1:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

    cmd = "cat %s" % name3
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'MEM_PERM_SIZE_32BIT="-XX:PermSize=259m"'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu4))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu4))

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