#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os
    test_name = 'LINUX运行机制与服务状态管理题目五'
    save_address = "/tmp/score.txt"
    name = '/examdata/result/port_used'
    test_vlu = "命令netstat 输出"
    test_vlu1 = "命令rpcinfo 输出"


    def run():
        try:
            f = open(save_address, 'w')
            # 1
            if os.path.exists(name):
                f.write("%s:文件%s,存在 ---ok\n" % (test_name, name))

                # 1
                cmd = "netstat -tulnp|grep vsftpd"
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")

                cmd_1 = "cat %s" % name
                com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
                if com_ret in com_ret_1:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

                # 2
                cmd = "rpcinfo -p"
                com_ret = commands.getoutput(cmd).lower().replace(" ", "")

                cmd_1 = "cat %s" % name
                com_ret_1 = commands.getoutput(cmd_1).lower().replace(" ", "")
                if com_ret in com_ret_1:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu1))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu1))
            else:
                f.write("%s:文件%s,不存在 ---error\n" % (test_name, name))
                f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu))
                f.write("%s:文件%s不存在, 无法%s ---error\n" % (test_name, name, test_vlu1))

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
    print str(e) + ' ---except'

else:
    if __name__ == '__main__':
        run()
