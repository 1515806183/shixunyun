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
        sql = '''select COMPRESSION from dba_indexes where index_name in (select index_name from dba_ind_columns where column_name='COUNTRY_ID' and table_name='CUSTOMERS' AND TABLE_OWNER='SH' intersect select index_name from dba_ind_columns where column_name='CUST_CITY' and table_name='CUSTOMERS' AND TABLE_OWNER='SH') '''
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            if "ENABLED".lower() in str(ret).lower():
                f.write("数据库数据段管理课件题目二:查看索引是否压缩正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目二:查看索引是否压缩错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目二:查看索引是否压缩错误, ---error\n")
    except:
        f.write('数据库数据段管理课件题目二:数据库打开错误,无法查看索引是否压缩 ---error\n')

    # 关闭连接
    f.close()
    cursor.close()
    conn.close()
    print("数据库数据段管理课件题目二:成功")


if __name__ == '__main__':
    run()