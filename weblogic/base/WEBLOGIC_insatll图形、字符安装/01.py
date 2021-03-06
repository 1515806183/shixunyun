#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    test_name = '安装与基础配置题目一'
    test_vlu = '是否存在参数8002'
    test_vlu1 = '是否存在参数true'

    save_address = "/tmp/score.txt"
    name = "/weblogic/user_projects/domains/test_domainx"
    name_1 = "/weblogic/user_projects/domains/test_domainx/config/config.xml"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("%s:文件%s,存在  ---ok\n" % (test_name, name))
                # 3.1
                cmd = "cat %s" % name_1
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")
                if "<listen-port>8002</listen-port>".lower().replace(" ", "") in com_ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

                # 3.2
                cmd = "cat %s" % name_1
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")
                if "<production-mode-enabled>true</production-mode-enabled>".lower().replace(" ", "") in com_ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

            else:
                f.write("%s:文件%s,不存在  ---error\n" % (test_name, name))
                f.write("%s:文件%s不存在, 无法查询%s ---error\n" % (test_name, name, test_vlu))
                f.write("%s:文件%s不存在, 无法查询%s ---error\n" % (test_name, name, test_vlu1))

        except Exception as e:
            print str(e) + '---except'
        else:
            f.close()

        finally:
            try:
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

except Exception as e:
    print str(e) + '---except'

else:
    if __name__ == '__main__':
        run()