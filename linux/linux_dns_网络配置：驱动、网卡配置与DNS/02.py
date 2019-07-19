# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'
linux_txt_2 = '192.168.100.3'


def test_02():
    try:
        cmd_cat = "ip addr"
        com_ret = commands.getoutput(cmd_cat)
        ip_list = re.findall(r'%s' % linux_txt_2, com_ret)
        with open(save_address, 'w') as f:
            if linux_txt_2 in ip_list:
                f.write("LINUX系统基本组成题目二：检查eth1的IP地址，正常输出为192.168.100.3, ---ok" + '\n')
            else:
                f.write("LINUX系统基本组成题目二：检查eth1的IP地址，正常输出不为192.168.100.3, ---error" + '\n')
    except:
        print("LINUX系统基本组成题目二:\033[0;34m失败\033[0m")
        raise

    else:
        print("LINUX系统基本组成题目二:成功")


if __name__ == '__main__':
    test_02()