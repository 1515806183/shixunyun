#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
name = "/examdata/result/system_default_tbs.log"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("数据库数据字典与视图课件题目六:文件%s,存在, ---ok\n" % name)
            # 1
            cmd = "cat %s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "dba_users".lower() in com_ret \
                    and "temporary_tablespace".lower() in com_ret\
                    and "SCOTT".lower() in com_ret\
                    and "SYSTEM".lower() in com_ret:

                f.write("数据库数据字典与视图课件题目六:查看配置信息dba_users,temporary_tablespace,SCOTT,SYSTEM,存在 ---ok\n")
            else:
                f.write("数据库数据字典与视图课件题目六:查看配置信息dba_users,temporary_tablespace,SCOTT,SYSTEM,不存在 ---error\n")

        else:
            f.write("数据库数据字典与视图课件题目六:文件%s,不存在, ---error\n" % name)
            f.write("数据库数据字典与视图课件题目六:文件%s,不存在,无法查看配置信息dba_users,temporary_tablespace,SCOTT,SYSTEM, ---error\n" % name)

    except:
        print("数据库数据字典与视图课件题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("数据库数据字典与视图课件题目六:成功")
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

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
