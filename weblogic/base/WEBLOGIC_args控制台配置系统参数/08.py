# -*- coding: utf-8 -*-
import commands, pexpect, time

test_name = '参数配置题目八'
test_vlu = '检查Server started in RUNNING'
save_address = "./score.txt"


def run():
    num = True
    f = open(save_address, 'w')

    # 2
    child = pexpect.spawn('/weblogic/user_projects/domains/test_domain1/bin/startWebLogic.sh')

    while 1:
        ret = child.expect([pexpect.TIMEOUT, 'Enter username', 'Enter password', '<BEA-000360> <Server started in RUNNING mode>', pexpect.exceptions.EOF])
        if ret == 0:
            print('[-] Error connecting')
            break

        if ret == 1:
            child.sendline('weblogic')
            time.sleep(1)

        if ret == 2:
            child.sendline('SXadmin#5678')

        if ret == 3:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
            num = False
            break
        if ret == 4:
            break
    if num:
        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()