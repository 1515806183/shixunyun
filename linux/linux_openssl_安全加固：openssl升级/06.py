#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import commands, os, re

    save_address = "/tmp/score.txt"
    name = "/examdata/result/get_ftp_file.log"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "ls /home"
            ret = commands.getoutput(cmd).lower()
            if "test2" in ret:
                f.write("LINUX安全加固openssl升级题目六:用户test2存在 ---ok\n")
                cmd_diff = "diff /etc/fstab /home/test2/fstab"
                com_ret_diff = commands.getoutput(cmd_diff)
                if com_ret_diff == '':
                    f.write("Linux安全加固题目六:/etc/fstab /home/test2/fstab比较两文件是一致 ---ok\n")
                else:
                    f.write("Linux安全加固题目六:/etc/fstab /home/test2/fstab比较两文件不是一致 ---error\n")
            else:
                f.write("LINUX安全加固openssl升级题目六:用户test2不存在 ---error\n")
                f.write("LINUX安全加固openssl升级题目六:用户test2不存在,/etc/fstab /home/test2/fstab比较两文件无法比较 ---error\n")
            # 2
            if os.path.exists(name):
                f.write("LINUX安全加固openssl升级题目六:文件%s存在, ---ok\n" % name)
                # 2.1
                cmd_cat = "cat %s" % name
                com_ret_cat = commands.getoutput(cmd_cat).replace(" ", "").lower()
                if 'remote:/etc/fstab' in com_ret_cat:
                    f.write("LINUX安全加固openssl升级题目六:文件%s grep remote /etc/fstab成功 ---ok\n" % name)
                else:
                    f.write("LINUX安全加固openssl升级题目六:文件%s grep remote /etc/fstab失败 ---error\n" % name)

                # 2.2
                cmd_cat = "cat %s" % name
                com_ret_cat = commands.getoutput(cmd_cat).replace(" ", "").lower()
                if 'receivedin' in com_ret_cat:
                    f.write("LINUX安全加固openssl升级题目六:文件%s grep received in成功 ---ok\n" % name)
                else:
                    f.write("LINUX安全加固openssl升级题目六:文件%s grep received in失败 ---error\n" % name)

            else:
                f.write("LINUX安全加固openssl升级题目六:文件%s不存在 ---error\n" % name)
                f.write("LINUX安全加固openssl升级题目六:文件%s不存在,grep remote: /etc/fstab失败 ---error\n" % name)
                f.write("LINUX安全加固openssl升级题目六:文件%s不存在,grep received in失败 ---error\n" % name)

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
