# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
save_address_test = './test.txt'

file_name01 = '/etc/inittab'
filename_2 = "/examdata/result/default_boot_mode"


def test_04():
    try:
        # 1
        cmd = 'echo $LANG'
        com_ret = commands.getoutput(cmd).lower()
        with open(save_address, 'w') as f:
            if "en_US.utf8".lower() in com_ret or 'en_US.utf-8'.lower() in com_ret:
                f.write("LINUX安装与配置题目四：echo $LANG,输出结果为 %s , ---ok" % com_ret + '\n')
            else:
                f.write("LINUX安装与配置题目四：echo $LANG,输出结果为 %s , ---error" % com_ret + '\n')
        # 2
        cmd = 'cat /etc/sysconfig/i18n'
        com_ret = commands.getoutput(cmd).lower()
        with open(save_address, 'a+') as f:
            if 'en_US.UTF-8'.lower() in com_ret or "en_US.UTF8".lower() in com_ret:
                f.write("LINUX安装与配置题目四：检查cat /etc/sysconfig/i18n,输出结果为 %s , ---ok" % com_ret + '\n')
            else:
                f.write("LINUX安装与配置题目四：检查cat /etc/sysconfig/i18n,输出结果为 %s , ---error" % com_ret + '\n')

    except:
        print("操作LINUX安装与配置题目四:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目四:成功")


if __name__ == '__main__':
    test_04()






