# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
name = "/examdata/result/top.txt"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("Linux性能诊断与调优题目二：文件%s存在, ---ok\n" % name)
            # 1
            cmd_1 = "cat %s|awk '{print $4}'" % name
            com_ret_1 = commands.getoutput(cmd_1)
            if com_ret_1:
                f.write("Linux性能诊断与调优题目二：%s|awk '{print $4}'过滤成功, ---ok\n" % name)
            else:
                f.write("Linux性能诊断与调优题目二：%s|awk '{print $4}'过滤失败, ---error\n" % name)

            # 2
            cmd_2 = "cat %s|awk '{print $8}'" % name
            com_ret_2 = commands.getoutput(cmd_2).lower()

            if com_ret_2:
                f.write("Linux性能诊断与调优题目二：%s|awk '{print $7}'过滤成功, ---ok\n" % name)
            else:
                f.write("Linux性能诊断与调优题目二：%s|awk '{print $7}'过滤失败, ---error\n" % name)

        else:
            f.write("Linux性能诊断与调优题目二:文件%s不存在, ---error\n" % name)
            f.write("Linux性能诊断与调优题目二:文件%s不存在,无法过滤/examdata/result/top.txt|awk '{print $4}'  ---error\n" % name)
            f.write("Linux性能诊断与调优题目二:文件%s不存在,无法过滤/examdata/result/top.txt|awk '{print $7}' ---error\n" % name)

    except:
        print("Linux性能诊断与调优题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux性能诊断与调优题目二:成功")
        f.close()


if __name__ == '__main__':
    run()