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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
