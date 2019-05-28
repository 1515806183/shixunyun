# -*- coding: utf-8 -*-
import commands, os, re
test_name = '数据库网络管理课件题目三'
save_address = "./score.txt"
name = "/examdata/result/clear_listener_log.txt"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
    # 2
    # 2.1 获取主机名
    cmd = "hostname"
    host_name = commands.getoutput(cmd)

    # 2.2 执行命令
    cmd = "du -h /u01/app/oracle/diag/tnslsnr/%s/listener/trace/listener.log | awk '{print $1}'| grep '[0-9]'" % host_name
    com_ret = commands.getoutput(cmd)
    com_ret = re.match(r'\d+', com_ret)

    if com_ret:
        com_ret = int(com_ret.group())
        if com_ret > 1:
            f.write("%s:%s,统计文件大小成功, ---ok\n" % (test_name, cmd))
        else:
            f.write("%s:%s,统计文件大小错误, ---error\n" % (test_name, cmd))
    else:
        f.write("%s:%s,统计文件大小错误, ---error\n" % (test_name, cmd))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()