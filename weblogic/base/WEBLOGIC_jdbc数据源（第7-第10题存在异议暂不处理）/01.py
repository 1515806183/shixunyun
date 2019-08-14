#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, re
test_name = 'JDBC数据源题目一'
test_vlu = '检查是否存在config.xml相关备份文件'
test_vlu2 = '检查/weblogic/user_projects/domains/test_domain1/config/config.xml是否存在参数'
test_vlu3 = '检查jdbc_testdb1-jdbc.xml是否存在参数'


save_address = "/tmp/score.txt"
name = "find /weblogic/user_projects/domains/test_domain1/config -name 'config.xml*' | wc -l"
name1 = "/weblogic/user_projects/domains/test_domain1/config/config.xml"
name3 = '/weblogic/user_projects/domains/test_domain1/config/jdbc/jdbc_testdb1-jdbc.xml'


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
    if "<name>jdbc_testdb1</name>".lower().replace(" ", "") in com_ret and "<target>AdminServer</target>".lower().replace(" ", "") in com_ret and '<descriptor-file-name>jdbc/jdbc_testdb1-jdbc.xml</descriptor-file-name>'.lower().replace(" ", "") in com_ret:
        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

    else:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

    # 3
    if os.path.exists(name3):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name3))
        # 3.1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "<url>jdbc:oracle:thin:@127.0.0.1:1521:oradb</url>".lower().replace(" ", "") in com_ret\
                and "<value>DLUSER</value>".lower().replace(" ", "") in com_ret\
                and "<jndi-name>MyDataSource</jndi-name>".lower().replace(" ", "") in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name3))
        f.write("%s:查看文件%s不存在, 无法%s ---error\n" % (test_name, name3, test_vlu3))

    f.close()



    with open(save_address) as f :
        num = f.readlines()

    # 总题目数
    sum = len(num)
    # 一题多少分
    average = 100 // sum

    # 正确的题目总数
    timu_all = 0
    for i in num:
        if '---ok' in i:
                timu_all += 1
    total_score = timu_all * average

    print total_score

if __name__ == '__main__':
    run()