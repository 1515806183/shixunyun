# -*- coding: utf-8 -*-
# 保存正式score文件
import cx_Oracle, commands, os
save_address = "./score.txt"
name = "/examdata/result/view_dept_emp.log"
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
        f.write("数据库数据段管理课件题目十二:文件%s,存在, ---ok\n" % name)
        # 1.1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if "Create view".lower().replace(" ", "") in com_ret \
                and "Dname".lower().replace(" ", "") in com_ret \
                and "Loc".lower().replace(" ", "") in com_ret \
                and "Ename".lower().replace(" ", "") in com_ret \
                and "Sal".lower().replace(" ", "") in com_ret \
                and "job".lower().replace(" ", "") in com_ret \
                and "dept".lower().replace(" ", "") in com_ret \
                and "emp".lower().replace(" ", "") in com_ret:
            f.write("数据库数据段管理课件题目十二:查看文件%s 配置信息存在 ---ok\n" % name)
        else:
            f.write("数据库数据段管理课件题目十二:查看文件%s 配置信息不存在 ---error\n" % name)

    else:
        f.write("数据库数据段管理课件题目十二:文件%s,不存在, ---error\n" % name)
        f.write("数据库数据段管理课件题目十二:文件%s,不存在,无法查看配置信息... ---error\n" % name)
    # 2
    f = open(save_address, 'w')
    # 1 检查数据库是否能正常打开
    conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(username, pwd, ip, port, tns))
    cursor = conn.cursor()
    cursor.execute("select status from v$instance")
    ret = cursor.fetchone()  # 返回('OPEN',)
    if "OPEN" in ret:
        f.write('数据库参数维护课件题目一:数据库正常打开 ---ok\n')
    else:
        f.write('数据库参数维护课件题目一:数据库打开错误 ---error\n')

    # 3
    try:
        sql = "select count(*) from dba_views where view_name='VIEW_DEPT_EMP' AND OWNER='SCOTT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "1".lower().replace(" ", "") in ret:
                f.write("数据库数据段管理课件题目十二:确认视图view_dept_emp是否存在正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目十二:确认视图view_dept_emp是否存在错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目十二:确认视图view_dept_emp是否存在错误, ---error\n")

    except:
        f.write('数据库数据段管理课件题目十二:数据库查询表字段错误,无法确认视图view_dept_emp是否存在 ---error\n')

    # 关闭连接
    f.close()
    cursor.close()
    conn.close()
    print("数据库数据段管理课件题目十二:成功")


if __name__ == '__main__':
    run()