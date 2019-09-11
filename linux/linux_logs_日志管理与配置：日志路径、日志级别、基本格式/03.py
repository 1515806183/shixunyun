#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_3 = "/examdata/result/mail.log"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_3):

                f.write("Linux日志管理与配置题目三:文件%s存在 ---ok\n" % linux_txt_3)

                cmd_egrep = "egrep '^mail.*[[:space:]]+-/examdata/result/mail.log' /examdata/result/mail.log"
                com_ret_egrep = commands.getoutput(cmd_egrep).lower().replace(" ", "")

                if com_ret_egrep:
                    f.write("Linux日志管理与配置题目三:查看  mail.*级别日志路径成功 ---ok\n")
                else:
                    f.write("Linux日志管理与配置题目三:查看 mail.*级别日志路径失败 ---error\n")

            else:

                f.write("Linux日志管理与配置题目三:文件%s不存在 ---error\n" % linux_txt_3)
                f.write("Linux日志管理与配置题目三:文件%s不存在,无法查询 mail.*级别日志路径 ---error\n" % linux_txt_3)

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
