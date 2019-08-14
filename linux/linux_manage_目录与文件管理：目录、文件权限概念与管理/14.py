#!/usr/bin/python
# -*- coding: utf-8 -*-
# 保存正式score文件
import commands, os, re
save_address = "/tmp/score.txt"
name = "/examdata/training/technology"


def run():
    try:
        f = open(save_address, 'w')
        # 1
        num = True
        cmd_cat = "cat /etc/passwd|grep well|awk -F ':' '{print $3,$4}'"
        com_ret_cat = commands.getoutput(cmd_cat)
        ret_list = re.findall(r'\d+', com_ret_cat)
        for ret in ret_list:
            if ret != "502":
                num = False
                break
        if num:
            f.write("Linux目录与文件管理题目十四：用户well,uid和gid均为502, ---ok\n")
        else:
            f.write("Linux目录与文件管理题目十四：用户well,uid和gid不为502, ---error\n")

        # 2
        cmd_cat = "cat  /etc/group|grep engineer|awk -F ':' '{print $4}'"
        com_ret_cat = commands.getoutput(cmd_cat)
        if 'well' in com_ret_cat:
            f.write("Linux目录与文件管理题目十四：用户well,组engineer,过滤well成功, ---ok\n")
        else:
            f.write("Linux目录与文件管理题目十四：用户well,组engineer,过滤well失败, ---error\n")

        # 3
        if os.path.exists(name):
            f.write("Linux目录与文件管理题目十四：文件%s存在, ---ok\n" % name)
            cmd = "ls -ld /examdata/training/technology| egrep '(well\sengineer)' | awk '{print $1}'"
            ret = commands.getoutput(cmd)
            if "drwxr-xr-x" in ret:
                f.write("Linux目录与文件管理题目十四：目录technology属性为well:engineer,权限为drwxr-xr-x, ---ok\n")
            else:
                f.write("Linux目录与文件管理题目十四：目录technology属性不为well:engineer,权限不为drwxr-xr-x, ---error\n")
        else:
            f.write("Linux目录与文件管理题目十四：文件%s不存在, ---error\n" % name)
            f.write("Linux目录与文件管理题目十四：文件%s不存在,无法查看目录technology属性和权限 ---error\n" % name)

    except:
        raise

    else:
        print("Linux目录与文件管理题目十四:成功")
        f.close()



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

    print total_score

if __name__ == '__main__':
    run()
