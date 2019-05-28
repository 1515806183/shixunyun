# -*- coding: utf-8 -*-
# 保存正式score文件
import cx_Oracle
save_address = "./score.txt"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "192.168.32.117"
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
        f.write('数据库参数维护课件题目一:数据库正常打开 ---ok\n')
    else:
        f.write('数据库参数维护课件题目一:数据库打开错误 ---error\n')

    # 2
    try:
        sql = "select REFRESH_METHOD from dba_mviews where MVIEW_NAME='MV_EMP' AND OWNER='SCOTT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "FORCE".lower().replace(" ", "") in ret:
                f.write("数据库数据段管理课件题目五:确认物化视图更新方式正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目五:确认物化视图更新方式错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目五:确认物化视图更新方式错误, ---error\n")
    except:
        f.write('数据库数据段管理课件题目五:数据库查询错误,无法确认物化视图更新方式 ---error\n')

    # 3
    try:
        sql = "Select query from dba_mviews where MVIEW_NAME='MV_EMP' AND OWNER='SCOTT'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "select ename".lower().replace(" ", "") in ret \
                    and "job".lower().replace(" ", "") in ret \
                    and "hiredate".lower().replace(" ", "") in ret \
                    and "sal from scott.emp where sal>200".lower().replace(" ", "") in ret:

                f.write("数据库数据段管理课件题目五:确认物化视图的查询语句正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目五:确认物化视图的查询语句错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目五:确认物化视图的查询语句错误, ---error\n")

    except:
        f.write('数据库数据段管理课件题目五:数据库打开错误,无法确认物化视图的查询语句 ---error\n')

    # 关闭连接
    f.close()
    cursor.close()
    conn.close()
    print("数据库数据段管理课件题目五:成功")


if __name__ == '__main__':
    run()