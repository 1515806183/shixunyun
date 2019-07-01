# -*- coding: utf-8 -*-
import commands, os, re
test_name = '配置文件参数调整题目九'
test_vlu = '检查是否存在setDomainEnv.sh相关备份文件'
test_vlu2 = '检查setDomainEnv.sh是否存在参数'

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

    cmd = "cat %s" % name1
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if 'JAVA_HOME="/weblogic/jdk160_29"'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))


if __name__ == '__main__':
    run()