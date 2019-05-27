# -*- coding: utf-8 -*-
# 保存正式score文件
import cx_Oracle, commands, os
save_address = "./score.txt"
name = "/examdata/result/query_ind.log"
# 数据库信息
username = "system"
pwd = "SXadmin#1234"
ip = "192.168.32.117"
tns = "oradb"
port = 1521


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("数据库数据段管理课件题目九:文件%s,存在, ---ok\n" % name)
        # 1.1
        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if "Tablespace_name".lower().replace(" ", "") in com_ret \
                and "Bytes".lower().replace(" ", "") in com_ret \
                and "Dba_segments".lower().replace(" ", "") in com_ret \
                and "id_idx".lower().replace(" ", "") in com_ret:
            f.write("数据库数据段管理课件题目九:查看文件%s 配置信息存在 ---ok\n" % name)
        else:
            f.write("数据库数据段管理课件题目九:查看文件%s 配置信息不存在 ---error\n" % name)

    else:
        f.write("数据库数据段管理课件题目九:文件%s,不存在, ---error\n" % name)
        f.write("数据库数据段管理课件题目九:文件%s,不存在,无法查看配置信息... ---error\n" % name)
    # 2
    try:
        # 1 检查数据库是否能正常打开
        conn = cx_Oracle.connect('{}/{}@{}:{}/{}'.format(username, pwd, ip, port, tns))
        cursor = conn.cursor()
        cursor.execute("select status from v$instance")
        ret = cursor.fetchone()  # 返回('OPEN',)
        if "OPEN" in ret:
            f.write('数据库数据段管理课件题目九:数据库正常打开 ---ok\n')

    except:
        f.write('数据库数据段管理课件题目九:数据库打开错误 ---error\n')

    # 3
    try:
        sql = "select column_name from dba_ind_columns where index_name='ID_IDX'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "ID".lower().replace(" ", "") in ret:
                f.write("数据库数据段管理课件题目九:确认索引列是否为id正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目九:确认索引列是否为id错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目九:确认索引列是否为id错误, ---error\n")

    except:
        f.write('数据库数据段管理课件题目九:数据库查询表字段错误,无法确认索引列是否为id ---error\n')

    # 关闭连接
    f.close()
    cursor.close()
    conn.close()
    print("数据库数据段管理课件题目九:成功")


if __name__ == '__main__':
    run()