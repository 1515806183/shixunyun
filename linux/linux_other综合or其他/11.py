#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    test_name = 'LINUX综合or其他题目十一'
    save_address = "/tmp/score.txt"
    name = '/examdata/result/apache.txt'
    test_vlu = "过滤46"
    test_vlu1 = "过滤47"
    test_vlu2 = "过滤41"
    test_vlu3 = "过滤42"
    test_vlu4 = "过滤49"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))

                # 1
                cmd = """ cat %s |grep '46'|awk -F " " '{print $1}'  | wc -l """ % name
                com_ret = commands.getoutput(cmd)
                com_ret = int(com_ret)
                if com_ret == 22:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

                # 2
                cmd = """ cat %s |grep '47'|awk -F " " '{print $1}' | wc -l """ % name
                com_ret = commands.getoutput(cmd)
                com_ret = int(com_ret)
                if com_ret == 21:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

                # 3
                cmd = """ cat %s |grep '41'|awk -F " " '{print $1}' | wc -l """ % name
                com_ret = commands.getoutput(cmd)
                com_ret = int(com_ret)
                if com_ret == 19:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

                # 4
                cmd = """ cat %s |grep '42'|awk -F " " '{print $1}' | wc -l """ % name
                com_ret = commands.getoutput(cmd)
                com_ret = int(com_ret)
                if com_ret == 18:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

                # 5
                cmd = """ cat %s | grep '49'|awk -F " " '{print $1}'| wc -l  """ % name
                com_ret = commands.getoutput(cmd)
                com_ret = int(com_ret)
                if com_ret == 9:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu4))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu4))

            else:
                f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu1))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu2))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu3))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu4))

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
