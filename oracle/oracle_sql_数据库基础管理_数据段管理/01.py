#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
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
                f.write('数据库参数维护课件题目一:数据库正常打开 ---ok\n')
            else:
                f.write('数据库参数维护课件题目一:数据库打开错误 ---error\n')
        
            # 2
            sql = "SELECT INDEX_TYPE FROM DBA_INDEXES WHERE INDEX_NAME IN ( SELECT DISTINCT INDEX_NAME FROM DBA_IND_COLUMNS WHERE table_name='CUSTOMERS' AND table_owner='SH' AND column_name='COUNTRY_ID')"
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is not None:
                if "bitmap" in str(ret).lower():
                    f.write("数据库数据段管理课件题目一:查看创建的索引为bitmap ---ok\n")
                else:
                    f.write("数据库数据段管理课件题目一:查看创建的索引不为bitmap ---error\n")
            else:
                f.write("数据库数据段管理课件题目一:查看创建的索引不为bitmap ---error\n")
            # except:
            #     f.write('数据库数据段管理课件题目一:数据库打开错误,无法查看创建的索引 ---error\n')
    
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
