# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目十'
save_address = "./score.txt"
name = '/examdata/training/special_file.txt'
test_vlu = "过滤shopt"
test_vlu1 = "过滤tmp"


def run():
    f = open(save_address, 'w')
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))

        # 1
        cmd = "cat %s | grep 'shopt'" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if 'shopt'.lower().replace(" ", "") in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 2
        cmd = "cat %s | grep '!(tmp)'" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "tmp".lower().replace(" ", "") in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu))
        f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu1))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()