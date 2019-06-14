# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目七'
save_address = "./score.txt"
name = '/etc/vsftpd/vsftpd.conf '
test_vlu = "查看输出"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "grep '^chroot_local_user=YES' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s, 不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()