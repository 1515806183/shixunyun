#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    test_name = 'Linux其他题目三'
    save_address = "/tmp/score.txt"
    txt_one = '/examdata/result/install_software'

    test_vlu = 'egrep "yum install lrzsz'


    def run():
        try:
            f = open(save_address, 'w')

            if os.path.exists(txt_one):
                f.write("%s:文件%s存在 ---ok\n" % (test_name, txt_one))
                # 1
                cmd = 'cat %s ||egrep "yum\s+install\s+lrzsz"' % txt_one
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")
                if 'yuminstalllrzsz' in com_ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

            else:
                f.write("%s:文件%s不存在 ---error\n" % (test_name, txt_one))
                f.write("%s:文件%s不存在, 无法进行grep ---error\n" % (test_name, txt_one))

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
