#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    save_address = "/tmp/score.txt"
    name = "/examdata/result/constraint_query.result"


    def run():
        try:
            f = open(save_address, 'w')
            if os.path.exists(name):
                f.write("数据库数据字典与视图课件题目一:文件%s,存在 ---ok\n" % name)
                # 1
                cmd = "cat %s" % name
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")

                if "dba_constraints".lower() in com_ret \
                        and "CONSTRAINT_NAME".lower() in com_ret\
                        and "CONSTRAINT_NAME".lower() in com_ret \
                        and "TABLE_NAME".lower() in com_ret \
                        and "OWNER".lower() in com_ret:
                    f.write("数据库数据字典与视图课件题目一:查看配置信息dba_constraints,CONSTRAINT_NAME,CONSTRAINT_NAME,TABLE_NAME,OWNER存在 ---ok\n")
                else:
                    f.write("数据库数据字典与视图课件题目一:查看配置信息dba_constraints,CONSTRAINT_NAME,CONSTRAINT_NAME,TABLE_NAME,OWNER不存在 ---error\n")

            else:
                f.write("数据库数据字典与视图课件题目一:文件%s,不存在 ---error\n" % name)
                f.write("数据库数据字典与视图课件题目一:文件%s,不存在,无法查看配置信息dba_constraints,CONSTRAINT_NAME,CONSTRAINT_NAME,TABLE_NAME,OWNER ---error\n" % name)

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
