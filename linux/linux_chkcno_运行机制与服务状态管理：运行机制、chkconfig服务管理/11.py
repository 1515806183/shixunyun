#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os

test_name = 'LINUX运行机制与服务状态管理题目十一'
save_address = "/tmp/score.txt"
name = '/etc/sysconfig/nfs'
test_vlu = "检查nfs是否已使用更改后的端口"
test_vlu2 = "检查放行111端口"
test_vlu3 = "检查放行2049端口"
test_vlu4 = "检查放行30001端口"
test_vlu5 = "检查放行30002端口"
test_vlu6 = "检查放行30003端口"
test_vlu7 = "检查放行30004端口"


def run():
    f = open(save_address, 'w')
    # 1
    # 1.1
    cmd = "rpcinfo -p|grep '30001'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if '30001' in com_ret:
        f.write("%s:%s30001正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s30001错误 ---error\n" % (test_name, test_vlu))

    # 1.2
    cmd = "rpcinfo -p|grep '30002'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if '30002' in com_ret:
        f.write("%s:%s30002正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s30002错误 ---error\n" % (test_name, test_vlu))

    # 1.3
    cmd = "rpcinfo -p|grep '30003'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if '30003' in com_ret:
        f.write("%s:%s30003正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s30003错误 ---error\n" % (test_name, test_vlu))
    # 1.4
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        cmd = "cat %s |grep '^STATD_PORT=30004'" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if '30004' in com_ret:
            f.write("%s:%s30004正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s30004错误 ---error\n" % (test_name, test_vlu))
    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s30004 ---error\n" % (test_name, name, test_vlu))

    # 2
    cmd = "iptables -L -n --line|egrep 'dports\s+111'|awk -F ' ' '{print $2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ACCEPT'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    # 3
    cmd = "iptables -L -n --line|egrep 'dports\s+2049'|awk -F ' ' '{print $2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ACCEPT'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

    # 4
    cmd = "iptables -L -n --line|egrep 'dports\s+30001'|awk -F ' ' '{print $2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ACCEPT'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu4))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu4))

    # 5
    cmd = "iptables -L -n --line|egrep 'dports\s+30002'|awk -F ' ' '{print $2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ACCEPT'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu5))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu5))

    # 6
    cmd = "iptables -L -n --line|egrep 'dports\s+30003'|awk -F ' ' '{print $2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ACCEPT'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu6))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu6))

    # 7
    cmd = "iptables -L -n --line|egrep 'dports\s+30004'|awk -F ' ' '{print $2}'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ACCEPT'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu7))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu7))

    f.close()
    with open(save_address) as f:
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
