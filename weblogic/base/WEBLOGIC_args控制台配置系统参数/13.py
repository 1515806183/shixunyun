# -*- coding: utf-8 -*-
import commands, os
test_name = '参数配置题目十三'
test_vlu = '检查是否存在config.xml相关备份文件'
test_vlu2 = '检查config.xml是否存在参数'

save_address = "./score.txt"
name = "find /weblogic/user_projects/domains/test_domain1/config/ -name 'config.xml*' | wc -l"
name1 = '/weblogic/user_projects/domains/test_domain1/config/config.xml'


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
    if "<timeout-seconds>600</timeout-seconds>".lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()