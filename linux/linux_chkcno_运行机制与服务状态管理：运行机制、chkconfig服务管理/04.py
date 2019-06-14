# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目四'
save_address = "./score.txt"
name = '/etc/vsftpd/vsftpd.conf'
test_vlu = "ftp不允许匿名登陆"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s |grep 'anonymous_enable=no'" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        cmd_1 = "cat  %s | grep 'anonymous_enable=NO'" % name
        com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")

        if com_ret or com_ret_1:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()