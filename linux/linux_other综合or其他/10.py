#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os

    test_name = 'LINUX综合or其他题目十'
    save_address = "/tmp/score.txt"
    name = '/examdata/training/special_file.txt'
    test_vlu = "过滤shopt"
    test_vlu1 = "过滤tmp"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))

                # 1
                cmd = "cat %s | grep 'shopt'" % name
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")

                if 'shopt'.lower().replace(" ", "") in com_ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

                # 2
                cmd = "cat %s | grep '!(tmp)'" % name
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")
                if "tmp".lower().replace(" ", "") in com_ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))

            else:
                f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu))
                f.write("%s:文件%s,不存在无法%s ---error\n" % (test_name, name, test_vlu1))

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
