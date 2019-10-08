#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import pexpect, time

    test_name = '参数配置题目八'
    test_vlu = '检查Server started in RUNNING'
    save_address = "/tmp/score.txt"
    root = 'weblogic'
    pwd = 'SXadmin#5678'

    def run():
        try:
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
                    child.sendline(root)
                    time.sleep(1)

                if ret == 2:
                    child.sendline(pwd)

                if ret == 3:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                    num = False
                    break
                if ret == 4:
                    break
            if num:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        except Exception as e:
            print str(e) + '---except'
        else:
            f.close()

        finally:
            try:
                with open(save_address) as f:
                    num = f.readlines()

                # 总题目数
                sum = len(num)
                # 一题多少分
                average = 100 // sum

                # 正确的题目总数
                timu_all = 0
                for i in num:
                    print i.strip('\n').split(':')[1]
                    if '---ok' in i:
                        timu_all += 1

                if timu_all == sum:
                    total_score = 100
                else:
                    total_score = timu_all * average

                print str(total_score) + ' ---score'

            except Exception as e:
                print str(e) + '---except'


except Exception as e:
    print str(e) + '---except'

else:
    if __name__ == '__main__':
        run()