# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
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


if __name__ == '__main__':
    run()