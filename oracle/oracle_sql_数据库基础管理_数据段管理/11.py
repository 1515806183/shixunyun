#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import cx_Oracle
save_address = "/tmp/score.txt"
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
        sql = "select count(*) from dba_indexes where index_name='EMP_FUN_IND' and owner='HR'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "1".lower().replace(" ", "") in ret:
                f.write("数据库数据段管理课件题目十一:确认索引emp_fun_ind正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目十一:确认索引emp_fun_ind错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目十一:确认索引emp_fun_ind错误, ---error\n")

    except:
        f.write('数据库数据段管理课件题目十一:数据库查询表字段错误,无法确认索引emp_fun_ind存在 ---error\n')

    # 3
    try:
        sql = "select column_name from dba_ind_columns where index_name='EMP_FUN_IND'"
        cursor.execute(sql)
        ret = cursor.fetchone()
        if ret is not None:
            ret = str(ret).lower().replace(" ", "")
            if "SYS".lower().replace(" ", "") in ret:
                f.write("数据库数据段管理课件题目十一:确认索引列为函数upper(last_name)正确, ---ok\n")
            else:
                f.write("数据库数据段管理课件题目十一:确认索引列为函数upper(last_name)错误, ---error\n")
        else:
            f.write("数据库数据段管理课件题目十一:确认索引列为函数upper(last_name)错误, ---error\n")
    except:
        f.write('数据库数据段管理课件题目十一:数据库查询表字段错误,无法确认索引列为函数upper(last_name) ---error\n')

    f.close()
    cursor.close()
    conn.close()
    print("数据库数据段管理课件题目十一:成功")



    with open(save_address) as f :
        num = f.readlines()

    # 总题目数
    sum = len(num)
    # 一题多少分
    average = 100 // sum

    # 正确的题目总数
    timu_all = 0
    for i in num:
        if '---ok' in i:
                timu_all += 1
    total_score = timu_all * average

    print total_score

if __name__ == '__main__':
    run()
