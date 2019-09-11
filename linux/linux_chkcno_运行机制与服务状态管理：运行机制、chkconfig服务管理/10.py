#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands

    test_name = 'LINUX运行机制与服务状态管理题目十'
    save_address = "/tmp/score.txt"
    test_vlu = "检查防火墙是否在运行中"
    test_vlu1 = "检查放行20端口"
    test_vlu2 = "检查放行21端口"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "service iptables status|grep 'Firewall is not running'"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if com_ret and 'Firewall is not running'.lower().replace(" ", ""):
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

            else:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))

            # 2
            cmd = "iptables -L -n --line|egrep 'dports\s+20'|awk -F ' ' '{print $2}'"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if 'ACCEPT'.lower().replace(" ", "") in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))

            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

            # 3
            cmd = "iptables -L -n --line|egrep 'dports\s+21'|awk -F ' ' '{print $2}'"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if 'ACCEPT'.lower().replace(" ", "") in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

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
