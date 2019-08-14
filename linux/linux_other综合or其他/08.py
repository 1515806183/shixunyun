#!/usr/bin/python
# -*- coding: utf-8 -*-
import commands, os
test_name = 'LINUX综合or其他题目八'
save_address = "/tmp/score.txt"
name = '/tmp/lilei/passwd'
name1 = '/examdata/training/awk_file.txt'
test_vlu = "文件内容进行比较"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))

    # 2
    if os.path.exists(name1):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name1))

        # 结果进行比较
        cmd = "awk -F ':' 'NR>=10 && NR<=20 {print $3}' /etc/passwd"
        ret_cmd = commands.getoutput(cmd).lower().replace(" ", "")

        cmd = "cat %s" % name1
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if ret_cmd in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s,不存在 ---error\n" % (test_name, name1))
        f.write("%s:文件%s,不存在无法进行比较 ---error\n" % (test_name, name1))

    f.close()
    print("%s:成功" % test_name)



    with open(save_address) as f :
        num = f.readlines()

    # 总题目数
    sum = len(num)
    # 一题多少分
    average = 100 // sum

    # 正确的题目总数
    timu_all = 0
    for i in num:
        if '---ok' in i:
                timu_all += 1
    total_score = timu_all * average

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
