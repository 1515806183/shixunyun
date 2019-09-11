#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'


    def run():
        try:
            cmd_df = "df -T | grep ext3 | grep '/test'"
            com_ret_df = commands.getoutput(cmd_df)

            with open(save_address, "w") as f:
                if "test" in com_ret_df:
                    f.write("Linux磁盘存储管理题目七:过滤出信息test ---ok\n")
                else:
                    f.write("Linux磁盘存储管理题目七:没有过滤出信息test ---error\n")

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
