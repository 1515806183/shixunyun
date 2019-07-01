# -*- coding: utf-8 -*-
import commands, os, re
test_name = '配置文件参数调整题目一'
test_vlu = '检查是否存在setDomainEnv.sh相关备份文件'
test_vlu2 = '检查是否存在参数'
test_vlu3 = '检查是否存在命令'


save_address = "./score.txt"
name = "find /weblogic/user_projects/domains/test_domain1/bin/ -name 'setDomainEnv.sh*' | wc -l"
name1 = "/weblogic/user_projects/domains/test_domain1/bin/setDomainEnv.sh"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % name
    com_ret = commands.getoutput(cmd)
    com_ret = int(com_ret)
    if com_ret > 1:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    # 2
    cmd = "cat %s" % name1
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "WLS_MEM_ARGS_32BIT='-Xms1024m –Xmx1024m'".lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    # 3
    if "MEM_PERM_SIZE_32BIT='-XX:PermSize=512m'".lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()