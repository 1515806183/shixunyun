# -*- coding: utf-8 -*-
import commands, os
test_name = 'Linux其他题目三'
save_address = "./score.txt"
txt_one = '/examdata/result/install_software'

test_vlu = 'egrep "yum install lrzsz'


def run():
    f = open(save_address, 'w')

    if os.path.exists(txt_one):
        f.write("%s:文件%s存在 ---ok\n" % (test_name, txt_one))
        # 1
        cmd = 'cat %s ||egrep "yum\s+install\s+lrzsz"' % txt_one
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if 'yuminstalllrzsz' in com_ret:
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