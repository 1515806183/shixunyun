#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    test_name = '用户与角色管理课件题目二'
    test_vlu_1 = '查看用户exam_user7表空间'
    test_vlu_2 = '数据库帐号exam_user7最大可使用表空间'
    test_vlu_3 = '用户 test_user7 可试探空间'

    import cx_Oracle

    save_address = "/tmp/score.txt"
    # 数据库信息
    username = "system"
    pwd = "SXadmin#1234"
    ip = "127.0.0.1"
    tns = "oradb"
    port = 1521


    def run():
        try:
            f = open(save_address, 'w')
            # 1 检查数据库是否能正常打开
            conn = cx_Oracle.connect('{0}/{1}@{2}:{3}/{4}'.format(username, pwd, ip, port, tns))
            cursor = conn.cursor()
            cursor.execute("select status from v$instance")
            ret = cursor.fetchone()  # 返回('OPEN',)
            if "OPEN" in ret:
                f.write('%s:数据库正常打开 ---ok\n' % test_name)
            else:
                f.write('%s:数据库打开错误 ---error\n' % test_name)

            # 2

            sql = "select DEFAULT_TABLESPACE from dba_users where username='EXAM_USER7'"
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is not None:
                ret = str(ret).lower().replace(" ", "")
                if 'USERS'.lower() in ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu_1))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_1))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_1))

            # except:
            #     f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_1))

            # 3

            sql = "select max_bytes/1024/1024 from dba_ts_quotas where tablespace_name='USERS' AND username='EXAM_USER7'"
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is not None:
                ret = int(ret[0])
                if ret == 10:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu_2))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_2))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_2))

            # except:
            #     f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_2))

            # 4

            sql = "select TEMPORARY_TABLESPACE from dba_users where username='EXAM_USER7'"
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is not None:
                ret = str(ret).lower().replace(" ", "")
                if 'temp5' in ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu_3))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_3))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu_3))

            # except:
            #     f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu_3))

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
