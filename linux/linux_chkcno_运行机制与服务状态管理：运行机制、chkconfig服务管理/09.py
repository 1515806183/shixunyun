#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os
    test_name = 'LINUX运行机制与服务状态管理题目九'
    save_address = "/tmp/score.txt"
    test_vlu = "过滤vsftpd"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "netstat -tulnp|grep vsftpd|grep '21'"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            cmd_1 = "netstat -tulnp|grep vsftpd|grep '9999'"
            com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
            if com_ret and com_ret_1:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

        except Exception as e:
            print str(e) + '---except'

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

else:
    if __name__ == '__main__':
        run()
