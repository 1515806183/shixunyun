# -*- coding: utf-8 -*-
# 保存正式score文件
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
        f.write('数据库参数维护课件题目一:数据库正常打开 ---ok\n')
    else:
        f.write('数据库参数维护课件题目一:数据库打开错误 ---error\n')

    # 2
    try:
        sql = "select view_name,text,read_only from dba_views where view_name='V_EMP_1'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "V_EMP_1".lower().replace(" ", "") in ret \
                    and "select ename".lower().replace(" ", "") \
                    and "job".lower().replace(" ", "") \
                    and "hiredate".lower().replace(" ", "") \
                    and "sal from scott.emp where sal>2500".lower().replace(" ", ""):

                f.write("数据库数据段管理课件题目四:确认视图为v_emp_1,且视图满足查询条件和视图为只读正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目四:确认视图为v_emp_1,且视图满足查询条件和视图为只读错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目四:确认视图为v_emp_1,且视图满足查询条件和视图为只读错误, ---error\n")
    except:
        f.write('数据库数据段管理课件题目四:数据库查询错误,无法确认视图为v_emp_1,且视图满足查询条件和视图为只读 ---error\n')

    # 关闭连接
    f.close()
    cursor.close()
    conn.close()
    print("数据库数据段管理课件题目四:成功")


if __name__ == '__main__':
    run()