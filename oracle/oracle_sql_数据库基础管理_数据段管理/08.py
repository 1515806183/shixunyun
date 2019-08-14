#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
name = "/examdata/result/query_scott_tbl02.log"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("数据库数据段管理课件题目八:文件%s,存在, ---ok\n" % name)
            # 1
            cmd = "cat %s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "Object_name".lower().replace(" ", "") in com_ret \
                    and "Object_type".lower().replace(" ", "") in com_ret\
                    and "Dba_objects".lower().replace(" ", "") in com_ret \
                    and "OWNER".lower().replace(" ", "") in com_ret \
                    and "SCOTT".lower().replace(" ", "") in com_ret:
                f.write("数据库数据段管理课件题目八:查看文件%s 配置信息存在 ---ok\n" % name)
            else:
                f.write("数据库数据段管理课件题目八:查看文件%s 配置信息不存在 ---error\n" % name)

        else:
            f.write("数据库数据段管理课件题目八:文件%s,不存在, ---error\n" % name)
            f.write("数据库数据段管理课件题目八:文件%s,不存在,无法查看配置信息... ---error\n" % name)

    except:
        print("数据库数据段管理课件题目八:\033[0;34m失败\033[0m")

    else:
        print("数据库数据段管理课件题目八:成功")
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
