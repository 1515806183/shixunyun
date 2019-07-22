# -*- coding: utf-8 -*-
import commands, re
test_name = 'Linux磁盘存储管理题目九'
save_address = "./score.txt"

test_vlu = '/dev/raw/raw｛1..4}'
test_vlu1 = 'oinstall'


def run():
    f = open(save_address, 'w')
    # 1
    cmd = "ls /dev/raw/raw*"
    com_ret = commands.getoutput(cmd).split('\r')
    # com_ret = ['/dev/raw/raw1', '/dev/raw/raw2', '/dev/raw/raw3', '/dev/raw/raw4']
    list_num = []
    for ret in com_ret:
        list_num += re.findall(r'\d+', ret)
    num_str = ''.join(list_num)

    if '1234' == num_str:
        f.write("%s:过滤%s 正确 ---ok\n" % (test_name, test_vlu))
        cmd = "ls -l /dev/raw/raw1|grep oracle|grep oinstall"
        com_ret = commands.getoutput(cmd).lower().replace(' ', '')
        if 'oinstall' in com_ret:
            f.write("%s:过滤%s 正确 ---ok\n" % (test_name, test_vlu1))
        else:
            f.write("%s:过滤%s 错误 ---error\n" % (test_name, test_vlu1))

    else:
        f.write("%s:过滤%s 错误 ---error\n" % (test_name, test_vlu))
        f.write("%s:过滤%s 错误, 无法过滤oinstall ---error\n" % (test_name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()