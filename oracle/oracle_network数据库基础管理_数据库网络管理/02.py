# -*- coding: utf-8 -*-
import commands, os, re
test_name = '数据库网络管理课件题目二'
test_vlu = '查看监听端口1526'
test_vlu_2 = '查看监听lsnr2是否存在'
save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % 'netstat -an|grep 1526|grep ESTABLISHED|wc -l'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    com_ret = int(com_ret)
    if com_ret > 1:
        f.write("%s:查看%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:查看%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = "%s" % 'lsnrctl status lsnr2|grep READY|wc -l'
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    com_ret = int(com_ret)
    if com_ret > 1:
        f.write("%s:查看%s正确 ---ok\n" % (test_name, test_vlu_2))
    else:
        f.write("%s:查看%s错误 ---error\n" % (test_name, test_vlu_2))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()