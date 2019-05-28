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
        sql = "select value from v$parameter where name='undo_retention'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret >= 5400:
                f.write("数据库参数维护课件题目一:查看参数undo_retention值正确, ---ok\n")
            else:
                f.write("数据库参数维护课件题目一:查看参数undo_retention值错误, ---error\n")
        else:
            f.write("数据库参数维护课件题目一:查看参数undo_retention值错误, ---error\n")

    except:
        f.write('数据库参数维护课件题目一:数据库查询表字段错误,无法查看参数undo_retention值 ---error\n')

    # 3
    try:
        sql = "select value from v$parameter where upper(name)='PROCESSES'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret >= 550:
                f.write("数据库参数维护课件题目一:查询参数processes值正确, ---ok\n")
            else:
                f.write("数据库参数维护课件题目一:查询参数processes值错误, ---error\n")
        else:
            f.write("数据库参数维护课件题目一:查询参数processes值错误, ---error\n")

    except:
        f.write('数据库参数维护课件题目一:数据库查询表字段错误,无法查询参数processes值 ---error\n')

    # 4
    try:
        sql = "select value from v$parameter where upper(name)='JOB_QUEUE_PROCESSES'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret >= 15:
                f.write("数据库参数维护课件题目一:查询参数job值正确, ---ok\n")
            else:
                f.write("数据库参数维护课件题目一:查询参数job值错误, ---error\n")
        else:
            f.write("数据库参数维护课件题目一:查询参数job值错误, ---error\n")

    except:
        f.write('数据库参数维护课件题目一:数据库查询表字段错误,无法查询参数job值 ---error\n')

    f.close()
    cursor.close()
    conn.close()
    print("数据库参数维护课件题目一:成功")


if __name__ == '__main__':
    run()