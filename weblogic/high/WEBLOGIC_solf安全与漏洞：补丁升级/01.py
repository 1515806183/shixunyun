#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    test_name = '安全与漏洞题目一'
    test_vlu = '检查输出结果Patch ID'

    save_address = "/tmp/score.txt"
    name = "cd /weblogic/utils/bsu/ && bsu.sh -prod_dir=/weblogic/wlserver_10.3 -status=applied -verbose -view"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "%s" % name
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "Patch ID: EJUW".lower().replace(" ", "") in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))

            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

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