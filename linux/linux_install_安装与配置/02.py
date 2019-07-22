# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands
save_address = "./score.txt"
save_address_test = './test.txt'


def test_02():
    try:
        cmd_swap = "swapon -s | awk 'NR>1 {print $3}'"
        com_ret_swap = commands.getoutput(cmd_swap)
        com_ret_swap = com_ret_swap.split('\n')
        num = 0
        for res in com_ret_swap:
            num += int(res)
        num = num/1024
        print num
        with open(save_address, 'w') as f:
            if 2020< num < 2060:
                f.write("LINUX安装与配置题目二：系统当前环境swap 大小为2G, ---ok" + '\n')
            else:
                f.write("LINUX安装与配置题目二：系统当前环境swap 大小不为2G, ---error" + '\n')
    except:
        print("操作LINUX安装与配置题目二:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目二:成功")


if __name__ == '__main__':
    test_02()



