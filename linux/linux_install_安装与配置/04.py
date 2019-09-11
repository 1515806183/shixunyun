#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    save_address = "/tmp/score.txt"
    save_address_test = './test.txt'
    name = "/etc/sysconfig/i18n"


    def run():
        try:
            # 1
            f = open(save_address, 'w')
            cmd = 'echo $LANG'
            com_ret = commands.getoutput(cmd).lower()

            if "en_US.utf8".lower() in com_ret or 'en_US.utf-8'.lower() in com_ret:
                f.write("LINUX安装与配置题目四:echo $LANG,输出结果为 %s ---ok\n" % com_ret)
            else:
                f.write("LINUX安装与配置题目四:echo $LANG,输出结果为 %s ---error\n" % com_ret)
            # 2
            if os.path.exists(name):
                f.write("LINUX安装与配置题目四:%s文件存在 ---ok\n" % name)
                cmd = 'cat %s' % name
                com_ret = commands.getoutput(cmd).lower()

                if 'en_US.UTF-8'.lower() in com_ret or "en_US.UTF8".lower() in com_ret:
                    f.write("LINUX安装与配置题目四:检查cat /etc/sysconfig/i18n,输出en_US.UTF-8正确 ---ok\n")
                else:
                    f.write("LINUX安装与配置题目四:检查cat /etc/sysconfig/i18n,输出en_US.UTF-8错误 ---error\n")
            else:
                f.write("LINUX安装与配置题目四:%s文件不存在 ---error\n" % name)
                f.write("LINUX安装与配置题目四:%s文件不存在,无法查看en_US.UTF-8 是否存在 ---error\n" % name)

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
