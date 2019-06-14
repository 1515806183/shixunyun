# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目八'
save_address = "./score.txt"
name = '/etc/samba/smb.conf'
test_vlu = "过滤/etc/samba/smb.conf"
test_vlu1 = "过滤/etc/samba/smb.conf"
test_vlu2 = "过滤valid users"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "grep '/examdata/result/samba_05' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 2
        cmd = "egrep -i '^Hosts allow\s+=\s+172.25.0.0/255.255.255.0' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        cmd_1 = "egrep -i '^Hosts allow\s+=\s+172.25.0.0/24' %s" % name
        com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
        if com_ret or com_ret_1:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

        # 3
        cmd = "grep -E '^valid users\s+=\s+floyd' %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu1))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu2))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()