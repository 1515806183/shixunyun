#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    test_name = 'LINUX综合or其他题目二'
    save_address = "/tmp/score.txt"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "curl http://rhel65-training01.example.com"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if "csg linux training".lower().replace(" ", "") in com_ret and "Couldn".lower().replace(" ", "") not in com_ret:
                f.write("%s:输出csg linux training正确 ---ok\n" % test_name)
            else:
                f.write("%s:输出csg linux training错误 ---error\n" % test_name)

            # 2
            cmd = "curl http://www.example.com"
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if "example.com".lower().replace(" ", "") in com_ret and "Couldn".lower().replace(" ", "") not in com_ret:
                f.write("%s:输出 http //www.example.com正确 ---ok\n" % test_name)
            else:
                f.write("%s:输出 http //www.example.com错误 ---error\n" % test_name)

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
