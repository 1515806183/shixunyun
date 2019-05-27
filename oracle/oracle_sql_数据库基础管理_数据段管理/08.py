# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
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


if __name__ == '__main__':
    run()