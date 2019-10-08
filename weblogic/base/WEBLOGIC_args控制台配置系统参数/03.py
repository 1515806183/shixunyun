#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    test_name = '参数配置题目三'
    test_vlu = '检查是否存在config.xml相关备份文件'
    test_vlu2 = '检查config.xml是否存在参数'

    save_address = "/tmp/score.txt"
    name = "find /weblogic/user_projects/domains/test_domain2/config/ -name 'config.xml*' | wc -l"
    name1 = '/weblogic/user_projects/domains/test_domain2/config/config.xml'


    def run():
        try:
            f = open(save_address, 'w')

            # 判断文件是否存在
            if os.path.exists(name1):
                f.write("%s:文件%s存在 ---ok\n" % (test_name, name1))
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
                if "<console-context-path>testcon</console-context-path>".lower().replace(" ", "") in com_ret:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

            else:
                f.write("%s:文件%s不存在 ---error\n" % (test_name, name1))
                f.write("%s:文件%s不存在 %s错误 ---error\n" % (test_name, name1, test_vlu))
                f.write("%s:文件%s不存在 %s错误 ---error\n" % (test_name, name1, test_vlu2))

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