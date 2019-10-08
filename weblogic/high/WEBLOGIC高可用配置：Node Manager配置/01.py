#!/usr/bin/python
# -*- coding: utf-8 -*-
try:
    import commands, os, re
    test_name = 'Node_Manager配置题目一'
    save_address = "/tmp/score.txt"
    # ---------------------------- 1 ------------------------------------
    test_vlu = '检查是否存在config.xml相关备份文件'
    test_vlu2 = '检查config.xml是否存在参数<machine>Machine-test6</machine>'
    test_vlu3 = '检查name的值为Machine-test6，nm-type的值为Plain'

    xml_name = '/weblogic/user_projects/domains/test_domain6/config/config.xml'
    bak_cmd = "find /weblogic/user_projects/domains/test_domain6/config/ -name 'config.xml*' | wc -l"

    # ---------------------------- 2 ------------------------------------
    sh_path = '/weblogic/user_projects/domains/test_domain1/bin/startNodeManager.sh'
    sh_1 = '参数 NODEMGR_HOME="/weblogic/user_projects/domains/base_domain2/bin/"'
    sh_2 = '参数 JAVA_OPTIONS="${JAVA_OPTIONS} -Dweblogic.nodemanager.sslHostNameVerificationEnabled=false"'

    def run():
        try:
            f = open(save_address, 'w')
            # 判断文件是否存在
            # ---------------------------- 1 ------------------------------------
            if os.path.exists(xml_name):
                f.write("%s:文件%s存在 ---ok\n" % (test_name, xml_name))

                # 1
                cmd = "%s" % bak_cmd
                com_ret = commands.getoutput(cmd)
                com_ret = int(com_ret)

                if com_ret > 1:
                    f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))

                # 2 判断Machine-test6
                cmd = "cat %s" % xml_name
                com_ret = commands.getoutput(cmd)
                r = re.compile(r'<name>server1</name>(.*)', re.S)
                ret_data = r.search(com_ret)

                if ret_data:
                    if 'Machine-test6'.lower() in ret_data.group().lower().replace(" ", ""):
                        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu2))
                    else:
                        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu2))

                # 3 判断name的正确值为Machine-test6，nm-type的正确值为Plain
                r = re.compile(r'<machine>(.*)</machine>', re.S)
                ret_data = r.search(com_ret)
                name = '<name>Machine-test6</name>'
                type = '<nm-type>Plain</nm-type>'
                data = ret_data.group().lower().replace(" ", "")

                if ret_data:
                    if name.lower() in data and type.lower() in data:
                        f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu3))
                    else:
                        f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

                else:
                    f.write("%s:%s错误 ---error\n" % (test_name, test_vlu3))

            else:
                f.write("%s:文件%s不存在 ---error\n" % (test_name, xml_name))
                f.write("%s:文件%s不存在,%s ---error\n" % (test_name, xml_name, test_vlu2))
                f.write("%s:文件%s不存在,%s ---error\n" % (test_name, xml_name, test_vlu3))

            # ---------------------------- 2 ------------------------------------
            if os.path.exists(sh_path):
                f.write("%s:文件%s存在 ---ok\n" % (test_name, sh_path))
                # 1
                cmd = "cat %s | grep NODEMGR_HOME=" % sh_path
                sh_ret = commands.getoutput(cmd)
                if sh_ret:
                    if '/weblogic/user_projects/domains/base_domain2/bin/'.lower().replace(" ", "") in sh_ret.lower().replace(" ", ""):
                        f.write("%s:%s 存在 ---ok\n" % (test_name, sh_1))
                    else:
                        f.write("%s:%s 不存在 ---error\n" % (test_name, sh_1))

                else:
                    f.write("%s:%s 不存在 ---error\n" % (test_name, sh_1))

                # 2
                cmd = "cat %s | grep JAVA_OPTIONS=" % sh_path
                sh_ret = commands.getoutput(cmd)
                if sh_ret:
                    if '${JAVA_OPTIONS} -Dweblogic.nodemanager.sslHostNameVerificationEnabled=false'.lower().replace(" ", "") in sh_ret.lower().replace(" ", ""):
                        f.write("%s:%s 存在 ---ok\n" % (test_name, sh_2))
                    else:
                        f.write("%s:%s 不存在 ---error\n" % (test_name, sh_2))

                else:
                    f.write("%s:%s 不存在 ---error\n" % (test_name, sh_2))

            else:
                f.write("%s:文件%s不存在 ---error\n" % (test_name, sh_path))
                f.write("%s:文件%s不存在 %s 不存在 ---error\n" % (test_name, sh_path, sh_1))
                f.write("%s:文件%s不存在 %s 不存在 ---error\n" % (test_name, sh_path, sh_2))


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