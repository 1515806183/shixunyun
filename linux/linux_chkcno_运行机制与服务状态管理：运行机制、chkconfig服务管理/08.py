#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目八'
save_address = "/tmp/score.txt"
name = '/etc/samba/smb.conf'
test_vlu = "过滤/etc/samba/smb.conf"
test_vlu1 = "过滤/etc/samba/smb.conf"
test_vlu2 = "过滤valid users"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "grep '/examdata/result/samba_05' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 2
        cmd = "egrep -i '^Hosts allow\s+=\s+172.25.0.0/255.255.255.0' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        cmd_1 = "egrep -i '^Hosts allow\s+=\s+172.25.0.0/24' %s" % name
        com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
        if com_ret or com_ret_1:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

        # 3
        cmd = "grep -E '^valid users\s+=\s+floyd' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu1))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu2))

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
