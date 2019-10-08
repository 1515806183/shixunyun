#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    test_name = 'Node_Manager配置题目四'
    save_address = "/tmp/score.txt"

    domains_path = '/weblogic/user_projects/domains/test_domain6/bin/nodemanager.domains'
    sh_1 = '参数test_domain6=/weblogic/user_projects/domains/test_domain6'

    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(domains_path):
                f.write("%s:文件%s存在 ---ok\n" % (test_name, domains_path))
                # 1
                cmd = "cat %s | grep test_domain6=/weblogic/user_projects/domains/test_domain6" % domains_path
                sh_ret = commands.getoutput(cmd)
                if sh_ret:
                    f.write("%s:%s 正确 ---ok\n" % (test_name, sh_1))
                else:
                    f.write("%s:%s 错误 ---error\n" % (test_name, sh_1))

            else:
                f.write("%s:文件%s不存在 ---error\n" % (test_name, domains_path))
                f.write("%s:文件%s不存在 %s 错误 ---error\n" % (test_name, domains_path, sh_1))

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