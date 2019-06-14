# coding=utf-8

import commands
import os
import re


# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'


linux_txt_1 = "/examdata/training/wenjian.sh"
linux_txt_2 = '/examdata/result/inode.txt'
linux_txt_4 = "/examdata/result/list_file"
linux_txt_5 = "/examdata/result/dir_right"
linux_txt_6 = "/examdata/result/user20_can_write"
linux_txt_7 = "/examdata/result/file_right"
linux_txt_8 = "/examdata/result/group_exam"
linux_txt_10 = "/examdata/result/fast_create_dir.txt"
linux_txt_11_1 = "/var/log/messages"
linux_txt_11_2 = "/examdata/result/new_messages/empt1"
linux_txt_12_1 = "/etc/passwd"
linux_txt_12_2 = "/examdata/result/new_passwd"
linux_txt_14 = "/examdata/training/technology"
linux_txt_17 = "/examdata/result/dir"
linux_txt_18 = "/examdata/result/user08.sh"
linux_txt_19 = "/tmp/exam_51.log"
linux_txt_20 = "/examdata/result/num_users"
linux_txt_21_1 = "/etc/fstab"
linux_txt_21_2 = "/examdata/result/fstab.bak"
linux_txt_22 = "/examdata/result/admins"


class Cat_score_1(object):

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_txt_1):
                with open(save_address, "w") as f:
                    f.write("Linux目录与文件管理题目一：文件%s存在, ---ok\n" % linux_txt_1)

                cmd_ll = "ls -l /examdata/training/wenjian.sh |grep -E '(-rwxrwxr--)'"
                com_ret_ll = commands.getoutput(cmd_ll)

                with open(save_address, "a+") as f:
                    if "-rwxrwxr--" in com_ret_ll:
                        f.write("Linux目录与文件管理题目一：文件%s其权限属性为-rwxrwxr--, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目一：文件%s其权限属性不为-rwxrwxr--, ---error\n")

            else:
                with open(save_address, "w") as f:
                    f.write("Linux目录与文件管理题目一：文件%s不存在, ---error\n" % linux_txt_1)

        except:
            print("Linux目录与文件管理题目一:失败")

        else:
            print("Linux目录与文件管理题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:
            cmd_txt = "df -i /|awk 'NR>1 {print $2}'"
            com_ret_txt = commands.getoutput(cmd_txt)

            if os.path.exists('/examdata/result/inode.txt'):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二：文件%s存在, ---ok\n" % linux_txt_2)

                cmd_cat_txt = "cat /examdata/result/inode.txt"
                com_ret_cat = commands.getoutput(cmd_cat_txt)

                with open(save_address, "a+") as f:
                    if com_ret_txt[:-2] in com_ret_cat:
                        f.write("Linux目录与文件管理题目二：输出相近, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目二：输出不相近, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二：文件%s不存在, ---error\n" % linux_txt_2)

        except:
            print("Linux目录与文件管理题目二:失败")

        else:
            print("Linux目录与文件管理题目二:成功")


class Cat_score_3(object):

    @staticmethod
    def run():
        try:
            cmd_txt = "ls /examdata/training/"
            com_ret_txt = commands.getoutput(cmd_txt)

            with open(save_address, "a+") as f:
                if "sam.txt" in com_ret_txt:
                    f.write("Linux目录与文件管理题目三：检查/examdata/training/存在sam.txt, ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目三：检查/examdata/training/不存在sam.txt, ---error\n")

            cmd_jack = "ls /examdata/result/"
            com_ret_jack = commands.getoutput(cmd_jack)

            with open(save_address, "a+") as f:
                if "jack.txt" in com_ret_jack:
                    f.write("Linux目录与文件管理题目三：检查/examdata/result/存在jack.txt, ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目三：检查/examdata/result/不存在jack.txt, ---error\n")

        except:
            print("Linux目录与文件管理题目三:失败")

        else:
            print("Linux目录与文件管理题目三:成功")


class Cat_score_4(object):

    @staticmethod
    def run():
        try:
            cmd_txt = "ll -a / >/a.txt"
            commands.getoutput(cmd_txt)

            if os.path.exists(linux_txt_4):

                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目四：文件%s存在, ---ok\n" % linux_txt_4)

                cmd_jack = "diff /a.txt  /examdata/result/list_file"
                com_ret = commands.getoutput(cmd_jack)

                with open(save_address, "a+") as f:
                    if com_ret == "":
                        f.write("Linux目录与文件管理题目四：两个文件内容一致, ---ok\n")
                    else:

                        f.write("Linux目录与文件管理题目四：两个文件内容不一致, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目四：文件%s不存在, ---error\n" % linux_txt_4)

        except:
            print("Linux目录与文件管理题目四:失败")

        else:
            print("Linux目录与文件管理题目四:成功")


class Cat_score_5(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_5):

                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目五：文件%s存在, ---ok\n" % linux_txt_5)

                cmd_dir = "ls -ld /examdata/result/dir_right | awk '{print $3,$4}'"
                com_ret = commands.getoutput(cmd_dir)

                with open(save_address, "a+") as f:
                    if "root" in com_ret and 'user20' in com_ret:
                        f.write("Linux目录与文件管理题目五：检查其用户和组内容一致, ---ok\n")

                    else:
                        f.write("Linux目录与文件管理题目五：检查其用户和组不一致, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目五：文件%s存在, ---error\n" % linux_txt_5)

        except:
            print("Linux目录与文件管理题目五:失败")

        else:
            print("Linux目录与文件管理题目五:成功")


class Cat_score_6(object):
    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_6):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目六：创建文件%s成功, ---ok\n" % linux_txt_6)

                cmd_cat = "cat /examdata/result/user20_can_write"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if "drwxr--rwx" in com_ret_cat and ".ssh" in com_ret_cat:
                        f.write("Linux目录与文件管理题目五：检查输出内容一致, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目五：检查输出不一致, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目六：创建文件%s失败, ---error\n" % linux_txt_6)

        except:
            print("Linux目录与文件管理题目六:失败")

        else:
            print("Linux目录与文件管理题目六:成功")


class Cat_score_7(object):
    @staticmethod
    def run():
        try:
            with open(save_address, "a+") as f:
                if os.path.exists(linux_txt_7):
                    f.write("Linux目录与文件管理题目七：创建文件%s成功, ---ok\n" % linux_txt_7)
                else:
                    f.write("Linux目录与文件管理题目七：创建文件%s失败, ---error\n" % linux_txt_7)

        except:
            print("Linux目录与文件管理题目七:失败")

        else:
            print("Linux目录与文件管理题目七:成功")


class Cat_score_8(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_8):

                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目八：文件%s存在, ---ok\n" % linux_txt_8)

                cmd_dir = "ls -ld /examdata/result/group_exam|grep 'drwxr-s'"
                com_ret = commands.getoutput(cmd_dir)

                with open(save_address, "a+") as f:
                    if 'drwxr-s' in com_ret:
                        f.write("Linux目录与文件管理题目八：文件和子目录继承文件和子目录, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目八：文件和子目录没有继承文件和子目录, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目八：文件%s不存在, ---error\n" % linux_txt_8)

        except:
            print("Linux目录与文件管理题目八:失败")

        else:
            print("Linux目录与文件管理题目八:成功")


class Cat_score_9(object):

    @staticmethod
    def run():
        try:

            cmd_dir = "getfacl /etc/passwd"
            com_ret = commands.getoutput(cmd_dir)
            with open(save_address_test, 'w') as f:
                f.write(com_ret)

            cmd_dir = "cat " + save_address_test + " | grep 'user:user20:rw'"
            com_ret = commands.getoutput(cmd_dir)

            with open(save_address, "a+") as f:
                if 'user:user20:rwx' in com_ret:
                    f.write("Linux目录与文件管理题目九：有正常结果返回, ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目九：没有正常结果返回, ---error\n")

        except:
            print("Linux目录与文件管理题目九:失败")

        else:
            print("Linux目录与文件管理题目九:成功")


class Cat_score_10(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_10):

                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十：文件%s存在, ---ok\n" % linux_txt_10)

                cmd_dir = "ls -F /examdata/result/ | grep ^dir_level.*/$ | wc -l"
                com_ret = commands.getoutput(cmd_dir)

                with open(save_address, "a+") as f:
                    if "5" in com_ret:
                        f.write("Linux目录与文件管理题目十：文件和子目录继承文件和子目录, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目十：文件和子目录没有继承文件和子目录, ---error\n")
            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十：文件%s不存在, ---error\n" % linux_txt_10)

        except:
            print("Linux目录与文件管理题目十:失败")

        else:
            print("Linux目录与文件管理题目十:成功")


class Cat_score_11(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_11_1):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十一：文件%s存在, ---ok\n" % linux_txt_11_1)

                if os.path.exists(linux_txt_11_2):
                    with open(save_address, "a+") as f:
                        f.write("Linux目录与文件管理题目十一：文件%s存在, ---ok\n" % linux_txt_11_2)

                    cmd_diff = "diff /var/log/messages /examdata/result/new_messages/empt1"
                    com_ret_diff = commands.getoutput(cmd_diff)

                    with open(save_address, "a+") as f:
                        if '' == com_ret_diff:
                            f.write("Linux目录与文件管理题目十一：内容一致, ---ok\n")

                        else:
                            f.write("Linux目录与文件管理题目十一：内容不一致, ---error\n")

                    cmd_grep = "ls -ld /examdata/result/new_messages/empty1"
                    com_ret_grep = commands.getoutput(cmd_grep)

                    with open(save_address, "a+") as f:
                        if 'rw-------' in com_ret_grep and 'root' in com_ret_grep:
                            f.write("Linux目录与文件管理题目十一：文件组主和属组一致, ---ok\n")
                        else:
                            f.write("Linux目录与文件管理题目十一：文件组主和属组不一致, ---error\n")
                else:
                    with open(save_address, "a+") as f:
                        f.write("Linux目录与文件管理题目十一：文件%s不存在, ---error\n" % linux_txt_11_2)

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十一：文件%s不存在, ---error\n" % linux_txt_11_1)

        except:
            print("Linux目录与文件管理题目十一:失败")

        else:
            print("Linux目录与文件管理题目十一:成功")


class Cat_score_12(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_12_1):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十二：文件%s存在, ---ok\n" % linux_txt_12_1)

                if os.path.exists(linux_txt_12_2):
                    with open(save_address, "a+") as f:
                        f.write("Linux目录与文件管理题目十二：文件%s存在, ---ok\n" % linux_txt_12_2)

                    cmd_diff = "cat /etc/passwd | tee /examdata/result/new_passwd >> aaa"
                    commands.getoutput(cmd_diff)

                    cmd_aaa = "diff /etc/passwd ./aaa"
                    com_ret_aaa = commands.getoutput(cmd_aaa)

                    cmd_new = "diff /etc/passwd /examdata/result/new_passwd"
                    com_ret_new = commands.getoutput(cmd_new)

                    with open(save_address, "a+") as f:
                        if '' == com_ret_aaa and '' == com_ret_new:
                            f.write("Linux目录与文件管理题目十二：数据正确, ---ok\n")

                        else:
                            f.write("Linux目录与文件管理题目十二：数据不正确, ---error\n")

                else:
                    with open(save_address, "a+") as f:
                        f.write("Linux目录与文件管理题目十二：文件%s不存在, ---error\n" % linux_txt_12_2)

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十二：文件%s不存在, ---error\n" % linux_txt_12_1)

        except:
            print("Linux目录与文件管理题目十二:失败")

        else:
            print("Linux目录与文件管理题目十二:成功")


class Cat_score_13(object):

    @staticmethod
    def run():
        try:

            cmd_cat = "cat /etc/passwd | wc -cl"
            com_ret_cat = commands.getoutput(cmd_cat)

            ret_list = str(com_ret_cat).split()
            ret_a = ret_list[0]
            ret_b = ret_list[1]

            cmd_aaa = "cat /examdata/result/count_pwd |grep " + str(ret_a) + " | grep " + str(ret_b)
            com_ret_aaa = commands.getoutput(cmd_aaa)

            with open(save_address, "a+") as f:
                if str(ret_a) in com_ret_aaa and str(ret_b) in com_ret_aaa:
                    f.write("Linux目录与文件管理题目十三：数据一致, ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目十三：数据不一致, ---error\n")

        except:
            print("Linux目录与文件管理题目十三:失败")

        else:
            print("Linux目录与文件管理题目十三:成功")


class Cat_score_14(object):

    @staticmethod
    def run():
        try:
            cmd_cat = "cat /etc/passwd|grep well|awk -F ':' '{print $3,$4}'"
            com_ret_cat = commands.getoutput(cmd_cat)

            ret_list = str(com_ret_cat).split()

            ret_num = 0
            for i in ret_list:
                if "502" in i:
                    ret_num += 1

            with open(save_address, "a+") as f:
                if ret_num == 2:
                    f.write("Linux目录与文件管理题目十四：输出正确, ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目十四：输出错误, ---error\n")

            cmd_cat = "cat /etc/group|grep engineer|awk -F ':' '{print $4}'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if "well" in com_ret_cat:
                    f.write("Linux目录与文件管理题目十四：输出正确, ---ok\n")
                else:
                    f.write("Linux目录与文件管理题目十四：输出错误, ---error\n")

            if os.path.exists(linux_txt_14):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十四：文件%s存在, ---ok\n" % linux_txt_14)

                cmd_well = "ls -ld /examdata/training/technology|egrep '(well\sengineer)'"
                com_ret_well = commands.getoutput(cmd_well)

                cmd_drw = "ls -ld /examdata/training/technology|grep 'drwxr-xr-x'"
                com_ret_drw = commands.getoutput(cmd_drw)

                with open(save_address, "a+") as f:
                    if "well" in com_ret_well or 'engineer' in com_ret_well:
                        f.write("Linux目录与文件管理题目十四：属性为well:engineer, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目十四：属性不为well:engineer, ---error\n")

                with open(save_address, "a+") as f:
                    if "drwxr-xr-x" in com_ret_drw:
                        f.write("Linux目录与文件管理题目十四：目录权限为drwxr-xr-x, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目十四：目录权限不为drwxr-xr-x, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十四：文件%s不存在, ---error\n" % linux_txt_14)


        except:
            print("Linux目录与文件管理题目十四:失败")

        else:
            print("Linux目录与文件管理题目十四:成功")


class Cat_score_15(object):

    @staticmethod
    def run():
        try:

            cmd_cat = "cat /etc/passwd |grep hill| grep nologin"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if "" == com_ret_cat:
                    f.write("Linux目录与文件管理题目十五：查询grep nologin错误, ---error\n")

                else:
                    f.write("Linux目录与文件管理题目十五：查询grep nologin正确, ---ok\n")

        except:
            print("Linux目录与文件管理题目十五:失败")

        else:
            print("Linux目录与文件管理题目十五:成功")


class Cat_score_16(object):

    @staticmethod
    def run():
        try:

            cmd_cat = "cat /etc/shadow|grep tom|awk -F ':' '{print $3}'"
            com_ret_cat = commands.getoutput(cmd_cat)

            with open(save_address, "a+") as f:
                if '0' in com_ret_cat:
                    f.write("Linux目录与文件管理题目十六：输出数据为0, ---ok\n")

                else:
                    f.write("Linux目录与文件管理题目十六：输出数据不为0, ---error\n")

        except:
            print("Linux目录与文件管理题目十六:失败")

        else:
            print("Linux目录与文件管理题目十六:成功")


class Cat_score_17(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_17):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十七：文件%s存在, ---ok\n" % linux_txt_17)

                cmd_ll_user = "ls -ld /examdata/result/dir | egrep '(user01\sadmin)' | awk '{print $3}'"
                com_ret_ll_user = commands.getoutput(cmd_ll_user)

                cmd_ll_admin = "ls -ld /examdata/result/dir | egrep '(user01\sadmin)' | awk '{print $4}'"
                com_ret_ll_admin = commands.getoutput(cmd_ll_admin)

                with open(save_address, "a+") as f:
                    if "user01" in com_ret_ll_user and "admin" in com_ret_ll_admin:
                        f.write("Linux目录与文件管理题目十七：主属组设置正确, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目十七：主属组设置错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十七：文件%s不存在, ---error\n" % linux_txt_17)

                # TODO
                """"""

        except:
            print("Linux目录与文件管理题目十七:失败")

        else:
            print("Linux目录与文件管理题目十七:成功")


class Cat_score_18(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_18):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十八：文件%s 存在, ---ok\n" % linux_txt_18)

                cmd_cat = "cat /examdata/result/user08.sh"
                com_ret_cat = commands.getoutput(cmd_cat)

                ret_num = 0

                if "cp /bin/bash /bin/rbash" in com_ret_cat and "usermod -s /bin/rbash user08" in com_ret_cat and "mkdir /home/user08/bin" in com_ret_cat\
                        and "PATH=$HOME/bin" in com_ret_cat and "export PATH" in com_ret_cat:
                    ret_num += 1

                if "ln -s /bin/cat /home/user08/bin/cat" in com_ret_cat or "ln -s /bin/cat ~user08/bin/cat" in com_ret_cat:
                    ret_num += 1

                if "ln -s /bin/lsblk /home/user08/bin/lsblk" in com_ret_cat or "ln -s /bin/cat ~user08/bin/lsblk" in com_ret_cat:
                    ret_num += 1

                if "ln -s /bin/ping  /home/user08/bin/ping" in com_ret_cat or "ln -s /bin/cat ~user08/bin/ping" in com_ret_cat:
                    ret_num += 1

                with open(save_address, "a+") as f:
                    if ret_num >= 4:
                        f.write("Linux目录与文件管理题目十八：查询/examdata/result/user08.sh字眼正确, ---ok\n")
                    else:
                        f.write("Linux目录与文件管理题目十八：查询/examdata/result/user08.sh字眼失败, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十八：文件%s 不存在, ---error\n" % linux_txt_18)

        except:
            print("Linux目录与文件管理题目十八:失败")

        else:
            print("Linux目录与文件管理题目十八:成功")


class Cat_score_19(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_19):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十九：文件%s存在, ---ok\n" % linux_txt_19)

                cmd_cat = "cat /tmp/exam_51.log | awk '{print $1}'"
                com_ret_cat = commands.getoutput(cmd_cat)

                re_list = ['stu07', 'stu06', 'stu05', 'stu04', 'stu03', 'stu02', 'stu01', 'stu10', 'stu09', 'stu08']

                a = 0
                for i in re_list:
                    if i in com_ret_cat:
                        a += 1

                with open(save_address, "a+") as f:
                    if a >= 10:
                        f.write("Linux目录与文件管理题目十九：查询用户被创建正常, ---ok\n")

                    else:
                        f.write("Linux目录与文件管理题目十九：查询用户被创建错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目十九：文件%s不存在, ---error\n" % linux_txt_19)

        except:
            print("Linux目录与文件管理题目十九:失败")

        else:
            print("Linux目录与文件管理题目十九:成功")


class Cat_score_20(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_20):
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二十：文件%s存在, ---ok\n" % linux_txt_20)

                cmd_grep = "grep -v 'nologin' /etc/passwd|awk -F ':' '{print $1}'"
                com_ret_grep = commands.getoutput(cmd_grep)

                cmd_cat = "cat /examdata/result/num_users"
                com_ret_cat = commands.getoutput(cmd_cat)

                with open(save_address, "a+") as f:
                    if com_ret_grep in com_ret_cat:
                        f.write("Linux目录与文件管理题目二十：与1）的输出一致, ---ok\n")

                    else:
                        f.write("Linux目录与文件管理题目二十：与1）的输出不一致, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二十：文件%s不存在, ---error\n" % linux_txt_20)

        except:
            print("Linux目录与文件管理题目二十:失败")

        else:
            print("Linux目录与文件管理题目二十:成功")


class Cat_score_21(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_21_1):
                if os.path.exists(linux_txt_21_2):

                    with open(save_address, "a+") as f:
                        f.write("Linux目录与文件管理题目二十一：文件存在, ---ok\n")

                    cmd_diff = "diff /etc/fstab /examdata/result/fstab.bak"
                    com_ret_grep = commands.getoutput(cmd_diff)

                    with open(save_address, "a+") as f:
                        if com_ret_grep == "":
                            f.write("Linux目录与文件管理题目二十一：两个文件内容一致, ---ok\n")

                        else:
                            f.write("Linux目录与文件管理题目二十一：两个文件内容不一致, ---error\n")

                    cmd_ll = "ls -l /examdata/result/fstab.bak|awk -F " " '{print $4}'"
                    com_ret_ll = commands.getoutput(cmd_ll)

                    with open(save_address, "a+") as f:
                        if "manager" in com_ret_ll:
                            f.write("Linux目录与文件管理题目二十一：输出内容为manager, ---ok\n")

                        else:
                            f.write("Linux目录与文件管理题目二十一：输出内容不为manager, ---error\n")

                    cmd_harry = "getfacl /examdata/result/fstab.bak|egrep '(harry|natasha|other)'"
                    com_ret_harry = commands.getoutput(cmd_harry)

                    with open(save_address, "a+") as f:
                        if "harry" in com_ret_harry and "natasha" in com_ret_harry and "other" in com_ret_harry and 'user' in com_ret_harry and 'other' in com_ret_harry:
                            f.write("Linux目录与文件管理题目二十一：检查harry natasha及其他用户的权限设置正确, ---ok\n")

                        else:
                            f.write("Linux目录与文件管理题目二十一：检查harry natasha及其他用户的权限设置错误, ---error\n")

                else:
                    with open(save_address, "a+") as f:
                        f.write("Linux目录与文件管理题目二十一：文件%s不存在, ---error\n" % linux_txt_21_2)

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二十一：文件%s不存在, ---error\n" % linux_txt_21_1)

        except:
            print("Linux目录与文件管理题目二十一:失败")

        else:
            print("Linux目录与文件管理题目二十一:成功")


class Cat_score_22(object):

    @staticmethod
    def run():
        try:

            if os.path.exists(linux_txt_22):

                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二十二：文件%s存在, ---ok\n" % linux_txt_22)

                cmd_ll = "ls -ld  /examdata/result/admins|awk -F " " '{print $4}'"
                com_ret_ll = commands.getoutput(cmd_ll)

                with open(save_address, "a+") as f:
                    if "manager" in com_ret_ll:
                        f.write("Linux目录与文件管理题目二十二：输出内容为manager, ---ok\n")

                    else:
                        f.write("Linux目录与文件管理题目二十二：输出内容不为manager, ---error\n")

                cmd_harry = "ls -ld /examdata/result/admins|grep 'drwxrws---'"
                com_ret_harry = commands.getoutput(cmd_harry)

                with open(save_address, "a+") as f:
                    if "drwxrws---" in com_ret_harry:
                        f.write("Linux目录与文件管理题目二十二：检查drwxrws---正确, ---ok\n")

                    else:
                        f.write("Linux目录与文件管理题目二十二：检查drwxrws---错误, ---error\n")

            else:
                with open(save_address, "a+") as f:
                    f.write("Linux目录与文件管理题目二十二：文件%s不存在, ---error\n" % linux_txt_22)

        except:
            print("Linux目录与文件管理题目二十二:失败")

        else:
            print("Linux目录与文件管理题目二十二:成功")



def run():
    Cat_score_1().run()
    Cat_score_2().run()
    Cat_score_3().run()
    Cat_score_4().run()
    Cat_score_5().run()
    Cat_score_6().run()
    Cat_score_7().run()
    Cat_score_8().run()
    Cat_score_9().run()
    Cat_score_10().run()
    Cat_score_11().run()
    Cat_score_12().run()
    Cat_score_13().run()
    Cat_score_14().run()
    Cat_score_15().run()
    Cat_score_16().run()
    Cat_score_17().run()
    Cat_score_18().run()
    Cat_score_19().run()
    Cat_score_20().run()
    Cat_score_21().run()
    Cat_score_22().run()


run()




