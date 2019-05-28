# -*- coding: utf-8 -*-
import commands, os, cx_Oracle
test_name = '数据库参数维护课件题目九'
save_address = "./score.txt"
name = "/examdata/result/query_para_file.log"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "192.168.32.117"
tns = "oradb"
port = 1521


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if "pfile".lower().replace(" ", "") in com_ret or 'spfile'.lower().replace(" ", "") in com_ret:
            f.write("%s:查看文件%s 存在以下关键信息正确 ---ok\n" % (test_name, name))
        else:
            f.write("%s:查看文件%s 存在以下关键信息错误 ---error\n" % (test_name, name))
    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s 无法查看关键信息 ---error\n" % (test_name, name))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()