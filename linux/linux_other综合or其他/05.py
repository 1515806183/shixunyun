# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目五'
save_address = "./score.txt"
name = '/examdata/result/zonghe_05.txt'
test_vlu = "查询循环打印输出内容"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        # 1
        cmd = "cat %s | wc -l"% name
        com_ret = commands.getoutput(cmd)
        com_ret = int(com_ret)
        if com_ret == 6:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
        f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()