#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, re
    test_name = 'Linux磁盘存储管理题目九'
    save_address = "/tmp/score.txt"

    test_vlu = '/dev/raw/raw｛1..4}'
    test_vlu1 = 'oinstall'


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "ls /dev/raw/raw*"
            com_ret = commands.getoutput(cmd).split('\r')
            # com_ret = ['/dev/raw/raw1', '/dev/raw/raw2', '/dev/raw/raw3', '/dev/raw/raw4']
            list_num = []
            for ret in com_ret:
                list_num += re.findall(r'\d+', ret)
            num_str = ''.join(list_num)

            if '1234' == num_str:
                f.write("%s:过滤%s 正确 ---ok\n" % (test_name, test_vlu))
                cmd = "ls -l /dev/raw/raw1|grep oracle|grep oinstall"
                com_ret = commands.getoutput(cmd).lower().replace(' ', '')
                if 'oinstall' in com_ret:
                    f.write("%s:过滤%s 正确 ---ok\n" % (test_name, test_vlu1))
                else:
                    f.write("%s:过滤%s 错误 ---error\n" % (test_name, test_vlu1))

            else:
                f.write("%s:过滤%s 错误 ---error\n" % (test_name, test_vlu))
                f.write("%s:过滤%s 错误, 无法过滤oinstall ---error\n" % (test_name, test_vlu))

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
