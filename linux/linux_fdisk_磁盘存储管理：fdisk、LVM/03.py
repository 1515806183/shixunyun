#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'

    linux_txt_3_1 = "/examdata/result/lvm_config_file"
    linux_txt_3_2 = "/etc/lvm/lvm.conf"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(linux_txt_3_1):
                f.write("Linux磁盘存储管理题目三:文件%s存在 ---ok\n" % linux_txt_3_1)
                if os.path.exists(linux_txt_3_2):
                    f.write("Linux磁盘存储管理题目三:文件%s存在 ---ok\n" % linux_txt_3_2)

                    cmd_diff = "diff %s %s" % (linux_txt_3_1, linux_txt_3_2)
                    com_ret_diff = commands.getoutput(cmd_diff)

                    if com_ret_diff == "":
                        f.write("Linux磁盘存储管理题目三:备份lvm配置文件内容一致 ---ok\n")
                    else:
                        f.write("Linux磁盘存储管理题目三:备份lvm配置文件内容不一致 ---error\n")
                else:
                    f.write("Linux磁盘存储管理题目三:文件%s不存在 ---error\n" % linux_txt_3_2)

            else:
                f.write("Linux磁盘存储管理题目三:文件%s不存在 ---error\n" % linux_txt_3_1)
                f.write("Linux磁盘存储管理题目三:文件%s不存在, 无法进行备份lvm配置文件内容进行比较 ---error\n" % linux_txt_3_1)

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
