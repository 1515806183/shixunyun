# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目九'
save_address = "./score.txt"
test_vlu = "过滤vsftpd"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "netstat -tulnp|grep vsftpd|grep '21'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")

    cmd_1 = "netstat -tulnp|grep vsftpd|grep '9999'"
    com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
    if com_ret and com_ret_1:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()