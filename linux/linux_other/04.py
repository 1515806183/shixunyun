# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目四'
save_address = "./score.txt"
txt_one = '/examdata/soft.iso/epel-release-6-5.noarc'

test_vlu = 'grep epel-release-6-5.noarch'


def run():
    f = open(save_address, 'w')
    if os.path.exists(txt_one):
        f.write("%s:文件%s存在 ---ok\n" % (test_name, txt_one))
        # 1
        cmd = 'rpm -qa|grep epel-release-6-5.noarch'
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")

        if 'epel-release-6-5.noarch' in com_ret:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

    else:
        f.write("%s:文件%s不存在 ---error\n" % (test_name, txt_one))
        f.write("%s:文件%s不存在, 无法进行grep ---error\n" % (test_name, txt_one))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()