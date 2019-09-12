#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    name = "/home/oracle/.bash_profile"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("数据库安装与配置题目一:用户oracle存在 ---ok\n")
                # 1
                cmd = "cat %s" % name
                com_ret = commands.getoutput(cmd).lower()

                if "path" in com_ret and "$ORACLE_HOME/bin".lower() in com_ret and "ORACLE_SID".lower() in com_ret:
                    f.write("数据库安装与配置题目一:查看配置信息path,$ORACLE_HOME/bin,ORACLE_SID ---ok\n")
                else:
                    f.write("数据库安装与配置题目一:查看配置信息path,$ORACLE_HOME/bin,ORACLE_SID ---error\n")

            else:
                f.write("数据库安装与配置题目一:用户oracle不存在 ---error\n")
                f.write("数据库安装与配置题目一:用户oracle不存在,无法查看配置信息path,$ORACLE_HOME/bin,ORACLE_SID ---error\n")

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
