#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    test_name = '数据库参数维护课件题目三'
    test_vlu = '查看参数db_16k_cache_size'
    
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
        
            sql = "select value from v$parameter where name='db_16k_cache_size'"
            cursor.execute(sql)
            ret = cursor.fetchone()
            if ret is not None:
                ret = int(ret[0])
                if ret > 0:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
        
            # except:
            #     f.write('%s:数据库查询表字段错误,无法%s ---error\n' % (test_name, test_vlu))
    
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
