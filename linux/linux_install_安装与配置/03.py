#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'

    file_name01 = '/etc/inittab'
    filename_2 = "/examdata/result/default_boot_mode"


    def run():
        try:
            f = open(save_address, 'w')
            # 判断/etc/inittab文件是否存在
            if os.path.exists(file_name01):

                f.write("LINUX安装与配置题目三:%s文件存在 ---ok\n" % file_name01)

                cmd_1 = "tail /etc/inittab"
                com_ret_1 = commands.getoutput(cmd_1)
                if "id:3:initdefault:" in com_ret_1:
                    f.write('LINUX安装与配置题目三:文件是以id 3 initdefault 存在开头的一行,修改了原文件 ---error\n')
                else:
                    f.write("LINUX安装与配置题目三:文件不以id 3 initdefault 没修改原文件 ---ok\n")

            else:
                f.write("LINUX安装与配置题目三:%s 文件不存在 ---error\n" % file_name01)
                f.write('LINUX安装与配置题目三:文件%s不存在: 无法判断是否存在id 3 initdefault ---error\n' % file_name01)

            if os.path.exists(filename_2):
                # 查询 /examdata/result/default_boot_mode
                f.write("LINUX安装与配置题目三:%s文件存在 ---ok\n" % filename_2)

                cmd = "tail /examdata/result/default_boot_mode"
                com_ret = commands.getoutput(cmd)

                if "id:3:initdefault:" in com_ret:
                    f.write("LINUX安装与配置题目三:检查%s 文件有id 3 initdefault 开头一行 ---ok\n" % filename_2)
                else:
                    f.write("LINUX安装与配置题目三:检查%s 文件没有id 3 initdefault 开头一行 ---error\n" % filename_2)

            else:
                f.write("LINUX安装与配置题目三:%s 文件不存在 ---error\n" % filename_2)
                f.write('LINUX安装与配置题目三:文件%s不存在 无法判断是否存在id 3 initdefault ---error\n' % filename_2)

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

