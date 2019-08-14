#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "/tmp/score.txt"
name = "/examdata/result/conf_table.log"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("数据库数据段管理课件题目三:文件%s,存在, ---ok\n" % name)
            # 1
            cmd = "cat %s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "Create table sh.costs_1 as select * from sh.costs".lower().replace(" ", "") in com_ret \
                    and "Create table sh.costs_2 as select * from sh.costs".lower().replace(" ", "") in com_ret\
                    and "Delete sh.costs_1".lower().replace(" ", "") in com_ret \
                    and "Delete sh.costs_2".lower().replace(" ", "") in com_ret \
                    and "Truncate table sh.costs_1".lower().replace(" ", "") in com_ret\
                    and "Truncate table sh.costs_2".lower().replace(" ", "") in com_ret:
                f.write("数据库数据段管理课件题目三:查看文件%s 配置信息存在 ---ok\n" % name)
            else:
                f.write("数据库数据段管理课件题目三:查看文件%s 配置信息不存在 ---error\n" % name)

        else:
            f.write("数据库数据段管理课件题目三:文件%s,不存在, ---error\n" % name)
            f.write("数据库数据段管理课件题目三:文件%s,不存在,无法查看配置信息... ---error\n" % name)

    except:
        print("数据库数据段管理课件题目三:\033[0;34m失败\033[0m")

    else:
        print("数据库数据段管理课件题目三:成功")
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
