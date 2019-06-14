# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目一'
save_address = "./score.txt"


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "curl http://rhel65-training01.example.com"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "csg linux training".lower().replace(" ", "") in com_ret and "Couldn".lower().replace(" ", "") not in com_ret:
        f.write("%s:输出csg linux training正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出csg linux training错误 ---error\n" % test_name)

    # 2
    cmd = "curl www.example.com"
    com_ret = commands.getoutput(cmd).lower().replace(" ", "")
    if "example.com".lower().replace(" ", "") in com_ret and "Couldn".lower().replace(" ", "") not in com_ret:
        f.write("%s:输出example.com正确 ---ok\n" % test_name)
    else:
        f.write("%s:输出example.com错误 ---error\n" % test_name)

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()