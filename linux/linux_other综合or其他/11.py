# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目十一'
save_address = "./score.txt"
name = '/examdata/result/apache.txt'
test_vlu = "过滤46"
test_vlu1 = "过滤47"
test_vlu2 = "过滤41"
test_vlu3 = "过滤42"
test_vlu4 = "过滤49"


def run():
    f = open(save_address, 'w')
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))

        # 1
        cmd = "cat %s | grep '46' | awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 22:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 2
        cmd = "cat %s | grep '47' | awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 21:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

        # 3
        cmd = "cat %s | grep '41' | awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 19:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

        # 4
        cmd = "cat %s | grep '42' | awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 18:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

        # 5
        cmd = "cat %s | grep '49' | awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 9:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu4))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu4))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu1))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu2))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu3))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu4))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()