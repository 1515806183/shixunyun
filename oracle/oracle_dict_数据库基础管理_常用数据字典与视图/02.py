# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
name = "/examdata/result/query_segment_mb.result"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("数据库数据字典与视图课件题目二:文件%s,存在, ---ok\n" % name)
            # 1
            cmd = "cat %s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "dba_segments".lower() in com_ret \
                    and "owner".lower() in com_ret\
                    and "segment_name".lower() in com_ret \
                    and "segment_type".lower() in com_ret \
                    and "bytes".lower() in com_ret\
                    and "orderby".lower() in com_ret:
                f.write("数据库数据字典与视图课件题目二:查看配置信息dba_segments,owner,segment_name,segment_type,bytes,orderby,存在 ---ok\n")
            else:
                f.write("数据库数据字典与视图课件题目二:查看配置信息dba_segments,owner,segment_name,segment_type,bytes,orderby,不存在 ---error\n")

        else:
            f.write("数据库数据字典与视图课件题目二:文件%s,不存在, ---error\n" % name)
            f.write("数据库数据字典与视图课件题目二:文件%s,不存在,无法查看配置信息dba_segments,owner,segment_name,segment_type,bytes,orderby ---error\n" % name)

    except:
        print("数据库数据字典与视图课件题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("数据库数据字典与视图课件题目二:成功")
        f.close()


if __name__ == '__main__':
    run()