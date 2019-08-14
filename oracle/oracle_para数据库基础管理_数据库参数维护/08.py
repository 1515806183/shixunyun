#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os, cx_Oracle
test_name = '数据库参数维护课件题目八'
test_vlu = '查询参数undo_retention值'
save_address = "/tmp/score.txt"
name = "/examdata/result/query_undo_retention.log"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "127.0.0.1"
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

        if "undo_retention".lower().replace(" ", "") in com_ret:
            f.write("%s:查看文件%s 配置信息存在 ---ok\n" % (test_name, name))
        else:
            f.write("%s:查看文件%s 配置信息不存在 ---error\n" % (test_name, name))
    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s 配置信息不存在 ---error\n" % (test_name, name))

    # 2 检查数据库是否能正常打开
    conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(username, pwd, ip, port, tns))
    cursor = conn.cursor()
    cursor.execute("select status from v$instance")
    ret = cursor.fetchone()  # 返回('OPEN',)
    if "OPEN" in ret:
        f.write('%s:数据库正常打开 ---ok\n' % test_name)
    else:
        f.write('%s:数据库打开错误 ---error\n' % test_name)

    # 3
    try:
        sql = "select value from v$parameter where name='undo_retention'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 4800:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu))

    f.close()
    cursor.close()
    conn.close()
    print("%s:成功" % test_name)



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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
