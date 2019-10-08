#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands
    test_name = '配置文件参数调整题目一'
    test_vlu = '检查是否存在setDomainEnv.sh相关备份文件'
    test_vlu2 = '检查是否存在参数'
    test_vlu3 = '检查是否存在命令'


    save_address = "/tmp/score.txt"
    name = "find /weblogic/user_projects/domains/test_domain1/bin/ -name 'setDomainEnv.sh*' | wc -l"
    name1 = "/weblogic/user_projects/domains/test_domain1/bin/setDomainEnv.sh"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            cmd = "%s" % name
            com_ret = commands.getoutput(cmd)
            com_ret = int(com_ret)
            if com_ret > 1:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

            # 2
            cmd = "cat %s" % name1
            com_ret = commands.getoutput(cmd).lower().replace(" ", "")
            if "WLS_MEM_ARGS_32BIT='-Xms1024m –Xmx1024m'".lower().replace(" ", "") in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))

            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

            # 3
            if "MEM_PERM_SIZE_32BIT='-XX:PermSize=512m'".lower().replace(" ", "") in com_ret:
                f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
            else:
                f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

        except Exception as e:
            print str(e) + '---except'

        else:
            f.close()

        finally:
            try:
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


except Exception as e:
    print str(e) + '---except'

else:
    if __name__ == '__main__':
        run()