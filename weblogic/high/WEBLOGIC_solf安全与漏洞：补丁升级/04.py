#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    test_name = '安全与漏洞题目四'

    test_vlu1 = '检查jar包属组为weblogic'
    test_vlu_3 = '检查输出结果Patch ID'

    save_address = "/tmp/score.txt"
    name = "/weblogic/utils/bsu/"
    name_3 = "cd /weblogic/utils/bsu/ && bsu.sh -prod_dir=/weblogic/wlserver_10.3 -status=applied -verbose -view"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            if os.path.exists(name):
                f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
                # 2
                cmd = "ls -l %s*.jar | awk '{print $3 $4}'" % name
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")
                com_ret_list = com_ret.split('\n')
                num = 0
                for i in com_ret_list:
                    if 'weblogicweblogic' == i:
                        num += 1
                    else:
                        pass
                if num == 2:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

            else:
                f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
                f.write("%s:文件%s,不存在无法查看属组, ---error\n" % (test_name, name))

            # 3
            cmd = "%s" % name_3
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")

            if "Patch ID: EJUW".lower().replace(" ", "") in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu_3))

            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_3))

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