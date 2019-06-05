# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
name = "/examdata/result/start_db.log"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("数据库安装与配置题目二:文件%s,存在, ---ok\n" % name)
            # 1
            cmd = "cat %s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "startupnomount" in com_ret and "alterdatabasemount".lower() in com_ret and "alterdatabaseopen".lower() in com_ret:
                f.write("数据库安装与配置题目二:查看配置信息startup nomount,alter database mount,alter database open ---ok\n")
            else:
                f.write("数据库安装与配置题目二:查看配置信息startup nomount,alter database mount,alter database open ---error\n")

        else:
            f.write("数据库安装与配置题目二:文件%s,不存在, ---error\n" % name)
            f.write("数据库安装与配置题目二:文件%s,不存在,无法查看配置信息startup nomount,alter database mount,alter database open ---error\n" % name)


    except:
        print("数据库安装与配置题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("数据库安装与配置题目二:成功")
        f.close()


if __name__ == '__main__':
    run()