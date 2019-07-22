# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux磁盘存储管理题目六'
save_address = "./score.txt"

test_vlu = "执行命令，结果"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "df -hT /|sed 's/[GgMm]//g' | awk 'NR>1{print $3}'"
    com_ret = int(commands.getoutput(cmd).lower().replace(" ", ""))

    if com_ret == 16:
        f.write("%s:%s %s 正确 ---ok\n" % (test_name, test_vlu, com_ret))
    else:
        f.write("%s:%s %s 错误 ---error\n" % (test_name, test_vlu, com_ret))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()