# -*- coding: utf-8 -*-
import commands, os, re
test_name = '用户与角色管理课件题目八'
test_vlu = '查询关键信息'

save_address = "./score.txt"
name = "/examdata/result/query_user200.log"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "select created,default_tablespace,TEMPORARY_TABLESPACE from dba_users where username='EXAMUSER200'".lower().replace(" ", "") in com_ret\
                or """select created,default_tablespace,TEMPORARY_TABLESPACE from dba_users where username="EXAMUSER200""""".lower().replace(" ", "") in com_ret:
            f.write("%s:查看文件%s %s正确 ---ok\n" % (test_name, name, test_vlu))
        else:
            f.write("%s:查看文件%s %s错误 ---error\n" % (test_name, name, test_vlu))

    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))


    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()