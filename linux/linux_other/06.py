#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands

    test_name = 'Linux其他题目六'
    save_address = "/tmp/score.txt"

    test_vlu = 'rpm -qa |grep mysql-server'
    test_vlu1 = 'rpm -qa|grep sendmail'


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = 'rpm -qa |grep mysql-server'
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if 'server' in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

            # 2
            cmd = 'rpm -qa|grep sendmail'
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if com_ret:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))
            else:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))

        except Exception as e:
            print str(e) + ' ---except'

        else:
            f.close()

        finally:
            with open(save_address) as f:
                num = f.readlines()

            # 总题目数
            sum = len(num)
            # 一题多少分
            average = 100 // sum

            # 正确的题目总数
            timu_all = 0
            for i in num:
                print i.strip("\n").split(":")[1]

                if '---ok' in i:
                    timu_all += 1

            if timu_all == sum:
                total_score = 100
            else:
                total_score = timu_all * average

            print str(total_score) + ' ---score'

except Exception as e:
    print str(e) + ' ---except'

else:

    if __name__ == '__main__':
        run()
