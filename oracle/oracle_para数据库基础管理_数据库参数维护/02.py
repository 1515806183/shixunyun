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
        f.write('数据库参数维护课件题目二:数据库正常打开 ---ok\n')
    else:
        f.write('数据库参数维护课件题目二:数据库打开错误 ---error\n')

    # 2
    try:
        sql = "select value from v$parameter where name='sessions'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret >= 300:
                f.write("数据库参数维护课件题目二:查看参数sessions值正确, ---ok\n")
            else:
                f.write("数据库参数维护课件题目二:查看参数sessions值错误, ---error\n")
        else:
            f.write("数据库参数维护课件题目二:查看参数sessions值错误, ---error\n")

    except:
        f.write('数据库参数维护课件题目二:数据库查询表字段错误,无法查看参数sessions值 ---error\n')

    # 3
    try:
        sql = "select value from v$parameter where name='shared_server_sessions'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = int(ret[0])
            if ret <= 200:
                f.write("数据库参数维护课件题目二:查看参数shared_server_sessions正确, ---ok\n")
            else:
                f.write("数据库参数维护课件题目二:查看参数shared_server_sessions错误, ---error\n")
        else:
            f.write("数据库参数维护课件题目二:查看参数shared_server_sessions错误, ---error\n")

    except:
        f.write('数据库参数维护课件题目二:数据库查询表字段错误,无法查看参数shared_server_sessions ---error\n')


    f.close()
    cursor.close()
    conn.close()
    print("数据库参数维护课件题目二:成功")


if __name__ == '__main__':
    run()