# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目七'
save_address = "./score.txt"

test_vlu = 'yum'


def run():
    f = open(save_address, 'w')
    # 1
    cmd = 'yum --help'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    ret = "UnicodeDecodeError: 'ascii' codec can't decode byte 0xe4 in position 0: ordinal not in range(128)".lower().replace(" ", "")

    if ret in com_ret:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()