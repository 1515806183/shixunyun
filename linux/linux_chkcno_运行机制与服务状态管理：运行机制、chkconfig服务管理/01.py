#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    test_name = 'LINUX运行机制与服务状态管理题目一'
    save_address = "/tmp/score.txt"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "ps -ef|grep rpcbind|grep -v grep"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if com_ret:
                f.write("%s:rpcbind输出正确 ---ok\n" % test_name)

            else:
                f.write("%s:rpcbind输出错误 ---error\n" % test_name)

            # 2
            cmd = "ps -ef|grep nfs|grep -v grep | wc -l"
            com_ret = commands.getoutput(cmd)
            com_ret = int(com_ret)
            if com_ret > 0:
                f.write("%s:ps输出正确 ---ok\n" % test_name)
            else:
                f.write("%s:ps输出错误 ---error\n" % test_name)

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
    print str(e) + ' ---except'

else:
    if __name__ == '__main__':
        run()
