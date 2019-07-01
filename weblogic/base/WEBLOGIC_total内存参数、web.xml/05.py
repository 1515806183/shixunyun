# -*- coding: utf-8 -*-
import commands, os, re
test_name = '配置文件参数调整题目五'
test_vlu = '检查是否存在weblogic.xml相关备份文件'
test_vlu2 = '检查weblogic.xml是否存在参数'

save_address = "./score.txt"
name = "find /weblogic/wlserver_10.3/server/lib/consoleapp/webapp/WEB-INF/ -name 'weblogic.xml*' | wc -l"
name1 = "/weblogic/wlserver_10.3/server/lib/consoleapp/webapp/WEB-INF/weblogic.xml"


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
    if "<timeout-secs>340</timeout-secs>".lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))


if __name__ == '__main__':
    run()