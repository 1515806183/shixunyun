# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os
save_address = "./score.txt"
save_address_test = './test.txt'

file_name01 = '/etc/inittab'
filename_2 = "/examdata/result/default_boot_mode"


def test_03():
    try:
        # 判断/etc/inittab文件是否存在
        if os.path.exists(file_name01):
            with open(save_address, 'w') as f:
                f.write("LINUX安装与配置题目三:%s文件存在, ---ok" % file_name01 + '\n')

            cmd_1 = "tail /etc/inittab"
            com_ret_1 = commands.getoutput(cmd_1)
            if "id:3:initdefault:" in com_ret_1:
                with open(save_address, 'a+') as f:
                    f.write('LINUX安装与配置题目三:文件是以id:3:initdefault: 存在开头的一行,修改了原文件---error'+ '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write("LINUX安装与配置题目三:文件不以id:3:initdefault: 没修改原文件---ok"+ '\n')
        else:
            with open(save_address, 'w') as f:
                f.write("LINUX安装与配置题目三: %s 文件不存在, ---error" % file_name01 + '\n')

            with open(save_address, 'a+') as f:
                f.write('LINUX安装与配置题目三:文件%s不存在: 无法判断是否存在id:3:initdefault:---error' % file_name01 + '\n')

        if os.path.exists(filename_2):
            # 查询 /examdata/result/default_boot_mode
            cmd = "tail /examdata/result/default_boot_mode"
            com_ret = commands.getoutput(cmd)

            if "id:3:initdefault:" in com_ret:
                with open(save_address, 'a+') as f:
                    f.write("LINUX安装与配置题目三：检查%s 文件有id:3:initdefault: 开头一行, ---ok" % filename_2 + '\n')
            else:
                with open(save_address, 'a+') as f:
                    f.write("LINUX安装与配置题目三：检查%s 文件没有id:3:initdefault: 开头一行, ---error" % filename_2 + '\n')

        else:
            with open(save_address, 'a+') as f:
                f.write("LINUX安装与配置题目三: %s 文件不存在, ---error" % filename_2 + '\n')

            with open(save_address, 'a+') as f:
                f.write('LINUX安装与配置题目三:文件%s不存在: 无法判断是否存在id:3:initdefault:---error' % filename_2 + '\n')

    except:
        print("操作LINUX安装与配置题目三:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目三:成功")


if __name__ == '__main__':
    test_03()






