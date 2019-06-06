# -*- coding: utf-8 -*-
test_name = '用户与角色管理课件题目十五'
test_vlu_1 = '查询角色def_role是否存在'
test_vlu_2 = '查询角色验证方式'
test_vlu_3 = '查询角色赋予的系统角色'
test_vlu_4 = '查询角色赋予的系统权限'
test_vlu_5 = '查询角色赋予的对象权限'

name = '/examdata/result/grant_object_priv.log'


import cx_Oracle, os
save_address = "./score.txt"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "192.168.32.109"
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
        sql = "select count(*) from dba_roles where role='DEF_ROLE'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 1:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_1))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_1))

    # 3
    try:
        sql = "select AUTHENTICATION_TYPE from dba_roles where role='DEF_ROLE'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if 'NONE'.lower().replace(" ", "") in ret:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_2))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_2))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_2))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_2))

    # 4
    try:
        sql = "select GRANTED_ROLE from dba_role_privs where grantee='DEF_ROLE'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if 'RESOURCE'.lower().replace(" ", "") in ret:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_3))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_3))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_3))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_3))

    # 5
    try:
        sql = "select privilege from role_sys_privs where role='DEF_ROLE'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if 'CREATE SESSION'.lower().replace(" ", "") in ret:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_4))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_4))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_4))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_4))

    # 6
    try:
        sql = "select count(*) from role_tab_privs where role='DEF_ROLE' and PRIVILEGE='SELECT' AND owner='SCOTT' AND TABLE_NAME='DEPT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 1:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_5))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_5))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_5))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_5))

    f.close()
    cursor.close()
    conn.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()