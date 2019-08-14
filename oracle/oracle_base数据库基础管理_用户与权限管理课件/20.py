#!/usr/bin/python
# -*- coding: utf-8 -*-
import cx_Oracle, os, commands
test_name = '用户与角色管理课件题目二十'
test_vlu_1 = '查询password_management  profile 文件最大登陆失败次数'
test_vlu_2 = '查询password_management  profile 文件口令有效期'
test_vlu_3 = '查询password_management  profile 文件口令重用时间'
test_vlu_4 = '查询用户examuser211是否具有password_management  profile 文件'

save_address = "/tmp/score.txt"

# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "127.0.0.1"
tns = "oradb"
port = 1521


def run():
    f = open(save_address, 'w')
    # 1 检查数据库是否能正常打开
    conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(username, pwd, ip, port, tns))
    cursor = conn.cursor()
    cursor.execute("select status from v$instance")
    ret = cursor.fetchone()  # 返回('OPEN',)
    if "OPEN" in ret:
        f.write('%s:数据库正常打开 ---ok\n' % test_name)
    else:
        f.write('%s:数据库打开错误 ---error\n' % test_name)

    # 2
    try:
        sql = "select limit from dba_profiles where resource_name='FAILED_LOGIN_ATTEMPTS' and profile='PASSWORD_MANAGEMENT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 8:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_1))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_1))

    # 3
    try:
        sql = "select limit from dba_profiles where resource_name='PASSWORD_LIFE_TIME' and profile='PASSWORD_MANAGEMENT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 120:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_2))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_2))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_2))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_2))

    # 4
    try:
        sql = "select limit from dba_profiles where resource_name='PASSWORD_REUSE_TIME' and profile='PASSWORD_MANAGEMENT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 60:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_3))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_3))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_3))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_3))

    # 5
    try:
        sql = "select count(*) from dba_users where username='EXAMUSER211' and profile='PASSWORD_MANAGEMENT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 1:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_4))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_4))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_4))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_4))


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

    print total_score

if __name__ == '__main__':
    run()
