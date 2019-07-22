# -*- coding: utf-8 -*-
test_name = '用户与角色管理课件题目六'
test_vlu_1 = '确认用户adams用户默认表空间、临时表空间'
test_vlu_2 = '确认data01表空间配额'
test_vlu_3 = '确认data02表空间配额'


import cx_Oracle
save_address = "./score.txt"
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
        sql = "select default_tablespace,temporary_tablespace from dba_users where username='ADAMS'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if 'USERS'.lower() in ret and 'TEMP'.lower() in ret:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_1))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_1))

    # 3
    try:
        sql = "select max_bytes from dba_ts_quotas where tablespace_name='DATA01' AND username='ADAMS'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if '10*1024*1024'.lower() in ret:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_2))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_2))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_2))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_2))

    # 4
    try:
        sql = "select max_bytes from dba_ts_quotas where tablespace_name='DATA02' AND username='ADAMS'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if '20*1024*1024'.lower() in ret:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_3))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_3))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_3))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_3))


    f.close()
    cursor.close()
    conn.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()