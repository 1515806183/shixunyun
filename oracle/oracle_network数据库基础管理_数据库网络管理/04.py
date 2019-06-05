# -*- coding: utf-8 -*-
import commands, os, re
test_name = '数据库网络管理课件题目四'
test_vlu = '服务名为tns_exam'
save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % 'tnsping tns_exam'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'ok' in com_ret:
        f.write("%s:查看%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:查看%s错误 ---error\n" % (test_name, test_vlu))
    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()