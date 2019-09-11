#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, re
    save_address = "/tmp/score.txt"
    name = "/examdata/result/"


    def run():
        try:
            f = open(save_address, 'w')
            cmd = "ls %s" % name
            ret = commands.getoutput(cmd)
            ret_tar = re.search(r'backup_varlog.*', ret)
            if ret_tar is not None:
                ret_tar = ret_tar.group()
                f.write("Linux文件系统结构与管理题目三:备份文件%s存在 ---ok\n" % ret_tar)
                cmd_tar = "tar -zxvf %s/%s -C %s" % (name, ret_tar, name)
                commands.getoutput(cmd_tar)

                cmd_diff = "ls /var/log/*.log|wc -l"
                ret_1 = commands.getoutput(cmd_diff)
                cmd_diff = "ls /examdata/result/*.log|wc -l"
                ret_2 = commands.getoutput(cmd_diff)

                if ret_1 == ret_2:
                    f.write("Linux文件系统结构与管理题目三:目录文件对比输出一致 ---ok\n")
                else:
                    f.write("Linux文件系统结构与管理题目三:目录文件对比输出不一致 ---error\n")

            else:
                f.write("Linux文件系统结构与管理题目三:备份文件不存在 ---error\n")
                f.write("Linux文件系统结构与管理题目三:备份文件不存在, 无法进行对比 ---error\n")

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

