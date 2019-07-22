# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目六'
save_address = "./score.txt"

test_vlu = 'grep php-5.3'
test_vlu1 = 'grep compat-glibc'


def run():
    f = open(save_address, 'w')
    # 1
    cmd = 'rpm -qa | grep php-5.3'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'compat-glibc' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = 'rpm -qa |grep compat-glibc'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    if 'compat-glibc' in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()