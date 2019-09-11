#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, re
    save_address = "/tmp/score.txt"


    def run():
        try:
            f = open(save_address, 'w')
            cmd_df = "df -hTP|grep '/dev/shm'|awk '{print $5}'"
            com_ret_df = commands.getoutput(cmd_df)
            ret_str = com_ret_df[-1:].lower()
            com_num = re.search(r'\d+', com_ret_df).group()
            if ret_str == 'm':
                if com_num == "4096":
                    f.write("Linux文件系统结构与管理题目五:过滤出来的结果是%sM, 为4096M(4G) ---ok\n" % com_num)
                else:
                    f.write("Linux文件系统结构与管理题目五:过滤出来的结果是%sM, 不为4096M(4G) ---error\n" % com_num)
            else:
                if com_num == "4":
                    f.write("Linux文件系统结构与管理题目五:过滤出来的结果是%sG, 为4G ---ok\n" % com_num)
                else:
                    f.write("Linux文件系统结构与管理题目五:过滤出来的结果是%sG, 不为4G ---error\n" % com_num)

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
                print i.strip("\n").split(":")[1]

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

