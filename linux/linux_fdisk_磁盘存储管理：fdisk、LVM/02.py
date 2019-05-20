# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "./score.txt"
save_address_test = './test.txt'


def test_02():
    try:
        cmd_lv = "df -hTP|grep '/examdata/result/exam_lvm'"
        com_ret_lv = commands.getoutput(cmd_lv)

        with open(save_address, "w") as f:
            if "examdata/result/exam_lvm" in com_ret_lv:
                f.write("Linux磁盘存储管理题目二：检查examdata/result/exam_lvm,lv被挂载, ---ok\n")
            else:
                f.write("Linux磁盘存储管理题目二：检查examdata/result/exam_lvm, lv没有被挂载, ---error\n")

        cmd_lv = "df -hTP /|awk 'NR>1 {print $3}'|sed 's/[M|m]//g'"
        com_ret_lv = commands.getoutput(cmd_lv)
        com_ret_lv = int(re.search(r'\d+', com_ret_lv).group())

        with open(save_address, "a+") as f:
            if 100 < com_ret_lv < 150:
                f.write("Linux磁盘存储管理题目二：检查LV的大小为%s, 在100~150之间, ---ok\n" % com_ret_lv)
            else:
                f.write("Linux磁盘存储管理题目二：检查LV的大小为%s,不在100~150之间, ---error\n" % com_ret_lv)

    except:
        print("操作LINUX安装与配置题目二:\033[0;34m失败\033[0m")

    else:
        print("操作LINUX安装与配置题目二:成功")

if __name__ == '__main__':
    test_02()