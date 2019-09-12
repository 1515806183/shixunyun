#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    test_name = '数据库参数维护课件题目六'

    import os
    save_address = "/tmp/score.txt"
    name = "/examdata/result/pfile_tmp.ora"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("%s:文件%s,存在 ---ok\n" % (test_name, name))
            else:
                f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))

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
