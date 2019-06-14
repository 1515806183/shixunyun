# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目一'
save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "ps -ef|grep rpcbind|grep -v grep"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if com_ret:
        f.write("%s:输出正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出错误 ---error\n" % test_name)

    # 2
    cmd = "ps -ef|grep nfs|grep -v grep | wc -l"
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret > 0:
        f.write("%s:ps输出正确 ---ok\n" % test_name)
    else:
        f.write("%s:ps输出错误 ---error\n" % test_name)

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()