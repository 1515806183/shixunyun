# -*- coding: utf-8 -*-
# 保存正式score文件
import commands
save_address = "./score.txt"
save_address_test = './test.txt'
linux_1_root = 'lv_root:'
linux_1_swap = 'lv_swap:'


def test_01():
    try:
        cmd = "fdisk -l"
        com_ret = commands.getoutput(cmd)
        b = 0

        # 临时保存文件
        with open(save_address_test, 'w') as f:
            f.write(com_ret + '\n')

        f = open(save_address_test, 'r')
        line_list_find = []
        for line in f.readlines():
            line = line.strip('\n')
            line_list_find.append(line)
        f.close()

        for i in line_list_find:
            if linux_1_root in i or linux_1_swap in i:
                b += 1

            else:
                pass

        with open(save_address, 'w') as f:
            if b == 2:
                f.write("LINUX安装与配置题目一：系统存在根分区和swap分区, ---ok" + '\n')
            else:
                f.write("LINUX安装与配置题目一：系统不存在根分区和swap分区, ---ok" + '\n')

    except:
        print("操作LINUX安装与配置题目一:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目一:成功")


if __name__ == '__main__':
    test_01()