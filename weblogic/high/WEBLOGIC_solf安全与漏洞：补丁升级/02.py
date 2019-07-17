# -*- coding: utf-8 -*-
import commands, os, re
test_name = '安全与漏洞题目二'
test_vlu = '检查输出Patch ID结果'

save_address = "./score.txt"
name = "/weblogic/utils/bsu/bsu.sh -prod_dir=/weblogic/wlserver_10.3 -status=applied -verbose -view"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "%s" % name
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    print com_ret
    if "Patch ID: EJUW".lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()