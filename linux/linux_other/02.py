# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目二'
save_address = "./score.txt"

test_vlu = 'grep cdrom'
test_vlu1 = '安装'


def run():
    f = open(save_address, 'w')

    # 1
    cmd = "yum repolist |grep cdrom"
    com_ret = commands.getoutput(cmd)
    if 'cdrom' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = 'yum --disablerepo=\* --enablerepo=cdrom install bind -y'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'error' in com_ret:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()