#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
save_address_test = './test.txt'
linux_txt_6 = "/examdata/result/rpmbuild_package_install.log"


def run():
    try:
        # 1
        if os.path.exists(linux_txt_6):
            with open(save_address, "w") as f:
                f.write("Linux软件安装与配置题目六：文件%s存在, ---ok\n" % linux_txt_6)
            cmd_cat = "cat %s|grep rpm-build" % linux_txt_6
            com_ret_cat = commands.getoutput(cmd_cat).lower()

            with open(save_address, "a+") as f:
                if "rpm-build" in com_ret_cat:
                    f.write("Linux软件安装与配置题目六：过滤 rpm-build正确, ---ok\n")
                else:
                    f.write("Linux软件安装与配置题目六：过滤 rpm-build错误, ---error\n")
        else:
            with open(save_address, "w") as f:
                f.write("LinuxLinux软件安装与配置题目六：文件%s不存在, ---error\n" % linux_txt_6)

            with open(save_address, "a+") as f:
                f.write("LinuxLinux软件安装与配置题目六：文件%s不存在,无法过滤 rpm-build ---error\n" % linux_txt_6)

    except:
        print("Linux软件安装与配置题目六:\033[0;34m失败\033[0m")
        raise

    else:
        print("Linux软件安装与配置题目六:成功")



    with open(save_address) as f :
        num = f.readlines()

    # 总题目数
    sum = len(num)
    # 一题多少分
    average = 100 // sum

    # 正确的题目总数
    timu_all = 0
    for i in num:
        if '---ok' in i:
                timu_all += 1
    total_score = timu_all * average

    print('\033[0;34;40m总题目: %s 道\033[0m' % sum)
    print '\033[0;34;40m正  确: %s 道\033[0m' % timu_all
    print '\033[0;34;40m详细内容: %s 路径下\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()
