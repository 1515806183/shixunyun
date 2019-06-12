# -*- coding: utf-8 -*-
import commands, os, re
test_name = 'JDBC数据源题目五'
test_vlu = '检查jdbc_jdbc5.xml是否存在参数'

save_address = "./score.txt"
name = "/weblogic/user_projects/domains/test_domain1/config/jdbc/jdbc_jdbc5.xml"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))

        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "<url>jdbc:oracle:thin:@127.0.0.1:1521:oradb</url>".lower().replace(" ", "") in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s不存在, 无法查询%s ---error\n" % (test_name, name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()