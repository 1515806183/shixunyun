# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目七'
save_address = "./score.txt"
test_vlu = "查询extundelete版本"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "extundelete -v"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'extundelete version 0.2.4'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()