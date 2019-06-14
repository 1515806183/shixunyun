# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目六'
save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "grep '/var/ftp/pub/test' /etc/passwd"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if com_ret:
        f.write("%s:/var/ftp/pub/test正确 ---ok\n" % test_name)
    else:
        f.write("%s:/var/ftp/pub/test错误 ---error\n" % test_name)

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()