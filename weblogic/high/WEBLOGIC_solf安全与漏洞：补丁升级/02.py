#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    test_name = '安全与漏洞题目二'
    test_vlu = '检查是否存在config.xml相关备份文件'
    test_vlu2 = '检查bsu.sh文件，-Xms后面参数是否大于10m'
    test_vlu3 = '检查bsu.sh文件，-Xmx后面参数是否大于20m'
    test_vlu4 = '检查输出Patch ID: EJUW'

    save_address = "/tmp/score.txt"
    name = "find /weblogic/user_projects/domains/test_domain1/config/ -name 'config.xml*' | wc -l"
    name_2 = "/weblogic/utils/bsu/bsu.sh"
    name_4 = "cd /weblogic/utils/bsu/ && bsu.sh -prod_dir=/weblogic/wlserver_10.3 -status=applied -verbose -view"


    def run():
        try:
            f = open(save_address, 'w')
            # 1 相关备份文件
            cmd = "%s" % name
            com_ret = commands.getoutput(cmd)
            com_ret = int(com_ret)
            if com_ret > 1:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

            # 2
            cmd = "cat %s | grep 'Xms'" % name_2
            com_ret = commands.getoutput(cmd)
            Xms = int(com_ret.split('-Xms')[1].split('m')[0])
            Xmx = int(com_ret.split('Xmx')[1].split('m')[0])

            if Xms > 10:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))
            # 3
            if Xmx > 20:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

            # 4
            cmd = "%s" % name_4
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