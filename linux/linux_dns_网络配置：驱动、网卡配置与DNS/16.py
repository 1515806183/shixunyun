# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
import re

save_address = "./score.txt"
save_address_test = './test.txt'
file = '/examdata/result/hosts.bak'


def test_16():
    try:
        f = open(save_address, 'w')
        if os.path.exists(file):
            f.write("LINUX系统基本组成题目十一：文件%s存在, ---ok\n" % file)
            cmd = "date"
            ret = commands.getoutput(cmd)
            ret_date = re.search(r'\d+年\s+\d+月', ret).group()
            cmd_host_name = "hostname"
            ret_host_name = commands.getoutput(cmd_host_name)
            cmd = "cat %s|egrep '(%s|%s)'" % (file, ret_date, ret_host_name)
            ret = commands.getoutput(cmd)
            if ret:
                f.write("LINUX系统基本组成题目十一：文件%s里包含日期和主机名, ---ok\n" % file)
            else:
                f.write("LINUX系统基本组成题目十一：文件%s里不包含日期和主机名, ---error\n" % file)
        else:
            f.write("LINUX系统基本组成题目十一:文件%s不存在, ---error\n" % file)
            f.write("LINUX系统基本组成题目十一:文件%s不存在,无法进行过滤主机名日期对比 ---error\n" % file)

    except:
        print("LINUX安装与配置题目十一:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX安装与配置题目十一:成功")
        f.close()


if __name__ == '__main__':
    test_16()