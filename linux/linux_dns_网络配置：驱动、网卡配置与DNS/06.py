#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    # 保存正式score文件
    import commands, os, re

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_txt_6 = "/examdata/result/sysdf.log"


    def run():
        try:
            f = open(save_address, 'w')

            if os.path.exists(linux_txt_6):
                f.write("LINUX系统基本组成题目六:文件%s存在, ---ok\n" % linux_txt_6)

                cmd_cat = "crontab -l|egrep '(15\s+\*\s+\*\s+\*\s+\*.*sysdf.log)' --color=auto"
                com_ret = commands.getoutput(cmd_cat)
                num = re.findall(r"15\s+\*\s+\*\s+\*\s+\*.*sysdf.log", com_ret)

                if num:
                    f.write("LINUX系统基本组成题目六:执行命令过滤sysdf.log输出正确, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目六:执行命令过滤sysdf.log输出不正确, ---error" + '\n')

            else:
                f.write("LINUX系统基本组成题目六:文件%s不存在, ---error\n" % linux_txt_6)
                f.write("LINUX系统基本组成题目六:文件%s不存在,无法进行过滤查询 ---error\n" % linux_txt_6)

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
