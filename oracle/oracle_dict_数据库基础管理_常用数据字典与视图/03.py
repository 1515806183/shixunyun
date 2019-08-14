#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
name = "/examdata/result/default_tbs_sys.result"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("数据库数据字典与视图课件题目三:文件%s,存在, ---ok\n" % name)
            # 1
            cmd = "cat %s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "dba_users".lower() in com_ret \
                    and "default_tablespace".lower() in com_ret:

                f.write("数据库数据字典与视图课件题目三:查看配置信息default_tablespace,dba_users,存在 ---ok\n")
            else:
                f.write("数据库数据字典与视图课件题目三:查看配置信息default_tablespace,dba_users,不存在 ---error\n")

        else:
            f.write("数据库数据字典与视图课件题目三:文件%s,不存在, ---error\n" % name)
            f.write("数据库数据字典与视图课件题目三:文件%s,不存在,无法查看配置信息default_tablespace,dba_users ---error\n" % name)

    except:
        print("数据库数据字典与视图课件题目三:\033[0;34m失败\033[0m")
        raise

    else:
        print("数据库数据字典与视图课件题目三:成功")
        f.close()



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
