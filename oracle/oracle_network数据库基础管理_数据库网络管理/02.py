#!/usr/bin/python
# -*- coding: utf-8 -*-
try:

    import commands
    test_name = '数据库网络管理课件题目二'
    test_vlu = '查看监听端口1526'
    test_vlu_2 = '查看监听lsnr2是否存在'
    save_address = "/tmp/score.txt"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "%s" % 'netstat -an|grep 1526|grep ESTABLISHED|wc -l'
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            com_ret = int(com_ret)
            if com_ret > 1:
                f.write("%s:查看%s正确 ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:查看%s错误 ---error\n" % (test_name, test_vlu))

            # 2
            cmd = "%s" % 'lsnrctl status lsnr2|grep READY|wc -l'
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            com_ret = int(com_ret)
            if com_ret > 1:
                f.write("%s:查看%s正确 ---ok\n" % (test_name, test_vlu_2))
            else:
                f.write("%s:查看%s错误 ---error\n" % (test_name, test_vlu_2))

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
