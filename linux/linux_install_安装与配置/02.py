# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands
save_address = "./score.txt"
save_address_test = './test.txt'


def test_02():
    try:
        cmd_swap = "lsblk | grep lv_swap | awk '{print $5}'"
        com_ret_swap = commands.getoutput(cmd_swap)

        with open(save_address, 'w') as f:
            if com_ret_swap == '2G':
                f.write("LINUX安装与配置题目二：系统当前环境swap 大小为2G, ---ok" + '\n')
            else:
                f.write("LINUX安装与配置题目二：系统当前环境swap 大小不为2G, ---error" + '\n')
    except:
        print("操作LINUX安装与配置题目二:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目二:成功")


if __name__ == '__main__':
    test_02()



