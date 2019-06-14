# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX运行机制与服务状态管理题目三'
save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "exportfs -v|egrep '(^/test1\s+172.25.0.0/24|,root_squash)'"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if com_ret:
        f.write("%s:输出正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出错误 ---error\n" % test_name)

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()