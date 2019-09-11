#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    test_name = 'Linux磁盘存储管理题目六'
    save_address = "/tmp/score.txt"

    test_vlu = "执行命令，结果"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "df -hT /|sed 's/[GgMm]//g' | awk 'NR>1{print $3}'"
            com_ret = int(commands.getoutput(cmd).lower().replace(" ", ""))

            if com_ret == 16:
                f.write("%s:%s %s 正确 ---ok\n" % (test_name, test_vlu, com_ret))
            else:
                f.write("%s:%s %s 错误 ---error\n" % (test_name, test_vlu, com_ret))

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
