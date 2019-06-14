# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目四'
save_address = "./score.txt"
name = '/examdata/result/baidu_01.log'
test_vlu = "grep 'www'"
test_vlu1 = "grep 'post'"
test_vlu2 = "grep 'mp3'"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s | grep 'www'|awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 3:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 2
        cmd = "cat %s |grep 'post'|awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 2:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        # 3
        cmd = "cat %s |grep 'post'|awk -F ' ' '{print $1}' | wc -l" % name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 1:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu1))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu2))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()