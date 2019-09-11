#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    linux_1_root = 'lv_root:'
    linux_1_swap = 'lv_swap:'


    def run():
        try:
            cmd = "fdisk -l"
            com_ret = commands.getoutput(cmd)
            b = 0

            # 临时保存文件
            with open(save_address_test, 'w') as f:
                f.write(com_ret + '\n')

            f = open(save_address_test, 'r')
            line_list_find = []
            for line in f.readlines():
                line = line.strip('\n')
                line_list_find.append(line)
            f.close()

            for i in line_list_find:
                if linux_1_root in i or linux_1_swap in i:
                    b += 1

                else:
                    pass

            with open(save_address, 'w') as f:
                if b == 2:
                    f.write("LINUX安装与配置题目一:系统存在根分区和swap分区 ---ok" + '\n')
                else:
                    f.write("LINUX安装与配置题目一:系统不存在根分区和swap分区 ---error" + '\n')

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

