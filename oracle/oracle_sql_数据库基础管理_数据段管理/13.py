#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
    import cx_Oracle, commands, os
    save_address = "/tmp/score.txt"
    name = "/examdata/result/seq_dept.log"
    # 数据库信息
    username = "system"
    pwd = "SXadmin#1234"
    ip = "127.0.0.1"
    tns = "oradb"
    port = 1521


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            if os.path.exists(name):
                f.write("数据库数据段管理课件题目十三:文件%s,存在 ---ok\n" % name)
                # 1.1
                cmd = "cat %s" % name
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")

                if "Deptno_seq.currval".lower().replace(" ", "") in com_ret \
                        and "Deptno_seq.nextval".lower().replace(" ", "") in com_ret \
                        and "User_sequences".lower().replace(" ", "") in com_ret \
                        and "SEQUENCE_NAME".lower().replace(" ", "") in com_ret \
                        and "MAX_VALUE".lower().replace(" ", "") in com_ret \
                        and "INCREMENT_BY".lower().replace(" ", "") in com_ret:
                    f.write("数据库数据段管理课件题目十三:查看文件%s 配置信息存在 ---ok\n" % name)
                else:
                    f.write("数据库数据段管理课件题目十三:查看文件%s 配置信息不存在 ---error\n" % name)

            else:
                f.write("数据库数据段管理课件题目十三:文件%s,不存在 ---error\n" % name)
                f.write("数据库数据段管理课件题目十三:文件%s,不存在,无法查看配置信息... ---error\n" % name)
            # 2
            # 1 检查数据库是否能正常打开
            conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(username, pwd, ip, port, tns))
            cursor = conn.cursor()
            cursor.execute("select status from v$instance")
            ret = cursor.fetchone()  # 返回('OPEN',)
            if "OPEN" in ret:
                f.write('数据库参数维护课件题目一:数据库正常打开 ---ok\n')
            else:
                f.write('数据库参数维护课件题目一:数据库打开错误 ---error\n')

            # 3

            sql = "Select count(*) from dba_sequences where SEQUENCE_OWNER='SCOTT' and SEQUENCE_NAME='DEPTNO_SEQ'"
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is not None:
                ret = str(ret).lower().replace(" ", "")
                if "1".lower().replace(" ", "") in ret:
                    f.write("数据库数据段管理课件题目十三:序列deptno_seq是否已创建正确 ---ok\n")
                else:
                    f.write("数据库数据段管理课件题目十三:序列deptno_seq是否已创建错误 ---error\n")
            else:
                f.write("数据库数据段管理课件题目十三:序列deptno_seq是否已创建错误 ---error\n")
            #
            # except:
            #     f.write('数据库数据段管理课件题目十三:数据库查询表字段错误,无法序列deptno_seq是否已创建 ---error\n')

        except Exception as e:
            print str(e) + '---except'

        else:
            f.close()
            cursor.close()
            conn.close()

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
