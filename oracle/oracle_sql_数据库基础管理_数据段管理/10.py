#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    name = "/examdata/result/query_reb_ind.log"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            if os.path.exists(name):
                f.write("数据库数据段管理课件题目十:文件%s,存在 ---ok\n" % name)
                # 1.1
                cmd = "cat %s" % name
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")

                if "STATUS".lower().replace(" ", "") in com_ret \
                        and "Dba_indexes".lower().replace(" ", "") in com_ret \
                        and "Table_name='EMPLOYEES'".lower().replace(" ", "") in com_ret:
                    f.write("数据库数据段管理课件题目十:查看文件%s 配置信息存在 ---ok\n" % name)
                else:
                    f.write("数据库数据段管理课件题目十:查看文件%s 配置信息不存在 ---error\n" % name)

            else:
                f.write("数据库数据段管理课件题目十:文件%s,不存在 ---error\n" % name)
                f.write("数据库数据段管理课件题目十:文件%s,不存在,无法查看配置信息... ---error\n" % name)

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
