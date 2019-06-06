# -*- coding: utf-8 -*-
import cx_Oracle, os, commands
test_name = '用户与角色管理课件题目二十三'
test_vlu_1 = '确认exam_management PROFILE已经删除'
test_vlu_2 = '查询关键信息'
name = '/examdata/result/query_profile_user212.log'
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
        sql = "select count(*) from dba_profiles where profile='EXAM_MANAGEMENT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret == 0:
                f.write("%s:%s正确, ---ok\n" % (test_name, test_vlu_1))
            else:
                f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))
        else:
            f.write("%s:%s错误, ---error\n" % (test_name, test_vlu_1))

    except:
        f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_1))

    # 3
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if "profile".lower().replace(" ", "") in com_ret and "dba_users".lower().replace(" ", "") in com_ret and "EXAMUSER212".lower().replace(" ", "") in com_ret:
                f.write("%s:查看文件%s %s正确 ---ok\n" % (test_name, name, test_vlu_2))

        else:
            f.write("%s:查看文件%s %s错误 ---error\n" % (test_name, name, test_vlu_2))

    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu_2))



    f.close()
    cursor.close()
    conn.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()