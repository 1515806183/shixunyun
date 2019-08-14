#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目五'
save_address = "/tmp/score.txt"
name = '/examdata/result/port_used'
test_vlu = "命令netstat 输出"
test_vlu1 = "命令rpcinfo 输出"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "netstat -tulnp|grep vsftpd"
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        cmd_1 = "cat %s" % name
        com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
        if com_ret in com_ret_1:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 2
        cmd = "rpcinfo -p"
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        cmd_1 = "cat %s" % name
        com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
        if com_ret in com_ret_1:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu1))

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
