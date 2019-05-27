# coding=utf-8
# 数据库得分保存地址

# 保存正式score文件
save_address = "./score.txt"

# 测试文件
save_address_test = './test.txt'

linux_16_find = '/examdata/result/auto_shutdown.txt'
linux_17_ip = '192.168.100.3'
linux_18_ip = '10.10.10.9'
linux_19_find_1 = './check_atime.txt'
linux_19_find_2 = '/examdata/result/find_var.txt'
linux_22_find = '/examdata/result/process_running'
linux_23_file = '/examdata/result/file1'
linux_23_server = '/examdata/training/file1'
linux_24_new_ssh = '/etc/ssh/sshd_config'
linux_24_file = '/examdata/result/xtgl_08.txt'

linux_25_file = '/examdata/result/tcp.txt'
linux_25_ftp_test = 'ESTABLISHED 	1'
linux_26_find = '/examdata/result/init_files'
linux_28_find = '/examdata/result/fetch_ip'
linux_29_find = '/etc/motd'
linux_29_find_1 = 'hello, welcome to login linux  trainning system'
linux_30_find_5 = 'timeout=5'
linux_31_find = '/examdata/result/hosts.bak'

import commands
import pexpect
import time
import re
import os


class Cat_score_16(object):
    """
    题目 16
    16.计划于今天1:30让系统自动关机，请写出操作重要部分
    将操作输出到 /examdata/result/auto_shutdown.txt
    """

    def __init__(self):
        self.at_time = 'at 1:30'
        self.at_file = '/sbin/shutdown -h now'
        self.a = 0

    def run(self):
        try:

            self.time_down()

            with open(save_address, 'w') as f:

                if self.a > 0:
                    f.write("LINUX安装与配置题目一：系统自动关机设置成功, ---ok" + '\n')

                else:
                    f.write("LINUX安装与配置题目一：系统自动关机设置失败, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目一:失败")
            raise

        else:
            print("操作LINUX系统基本组成题目一:成功")

    def time_down(self):

        process = pexpect.spawn(self.at_time)

        process.expect('at> ')

        process.sendline(self.at_file)
        process.sendline('<EOT>')

        process.sendcontrol('d')

        process.interact()

        localtime = time.asctime(time.localtime(time.time()))

        filename = linux_16_find

        with open(filename, 'w') as f:
            f.write(localtime + '' + self.at_time + '' + self.at_file + '\n')

        self.a += 1

        return self.a


class Cat_score_17(object):
    """
    题目 17
    执行ip addr，检查eth1的IP地址，正常输出为192.168.100.3
    """

    @staticmethod
    def run():
        try:

            cmd_cat = "ip addr"
            com_ret = commands.getoutput(cmd_cat)

            # 寻找ip为192.168.100.3
            ip_list = re.findall(linux_17_ip, com_ret)

            with open(save_address, 'a+') as f:
                if linux_17_ip in ip_list:

                    f.write("LINUX系统基本组成题目二：检查eth1的IP地址，正常输出为192.168.100.3, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目二：检查eth1的IP地址，正常输出不为192.168.100.3, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目二:失败")

        else:
            print("操作LINUX系统基本组成题目二:成功")


class Cat_score_18(object):
    """
    题目 18
    18.添加一条路由，目的地址为10.10.10.9
    """

    @staticmethod
    def run():
        try:

            cmd_ip = "route -n | awk '{print $1}'"
            com_ret = commands.getoutput(cmd_ip)

            # 寻找ip为192.168.100.3
            ip_list = re.findall(linux_18_ip, com_ret)

            # 保存文件
            with open(save_address, 'a+') as f:

                if linux_18_ip in ip_list:
                    f.write("LINUX系统基本组成题目三：输出包含路由, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目三：输出不包含路由, ---error" + '\n')


        except:
            print("操作LINUX系统基本组成题目三:失败")

        else:
            print("操作LINUX系统基本组成题目三:成功")


class Cat_score_19(object):
    """
    题目 19
    18.添加一条路由，目的地址为10.10.10.9
    """

    @staticmethod
    def run():
        try:

            cmd_check = "find /var ! -atime -90"

            com_check_ret_1 = commands.getoutput(cmd_check)
            com_check_ret_2 = commands.getoutput(cmd_check)

            # 保存在file文件下
            with open(linux_19_find_1, 'w') as f:
                f.write(com_check_ret_1)

            # 保存在服务器上
            with open(linux_19_find_2, 'w') as f:
                f.write(com_check_ret_2)

            # 比较两个文件内容
            cmd_num_file = "cat ./check_atime.txt|wc -l"
            cmd_num_server = "cat /examdata/result/find_var.txt|wc -l"

            cmd_num_ret = commands.getoutput(cmd_num_file)
            cmd_server_ret = commands.getoutput(cmd_num_server)

            num = len(cmd_server_ret) - len(cmd_num_ret)

            # 保存文件
            with open(save_address, 'a+') as f:

                if -10 < num < 10:
                        f.write("LINUX系统基本组成题目四：检查两个文件输入一致, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目四：检查两个文件输入不一致, ---error" + '\n')


        except:
            print("操作LINUX系统基本组成题目四:失败")

        else:
            print("操作LINUX系统基本组成题目四:成功")


class Cat_score_20(object):
    """
    题目 20
    20.星期的 1~5 ，下午 3 点的每分钟，执行脚本 /examdata/training/exame_server_status.sh
    """

    @staticmethod
    def run():
        try:

            cmd_cro = "crontab -l"
            num_1 = "*/1  15  *  *  1-5  root  sh /examdata/training/exame_server_status.sh"
            num_2 = "*  15  *  *  1-5  root  sh /examdata/training/exame_server_status.sh"

            com_ret = commands.getoutput(cmd_cro)

            with open(save_address_test, "w") as f:
                f.write(com_ret)

            f = open(save_address_test, "r")

            r_list = f.readlines()

            f.close()

            # 保存文件
            with open(save_address, 'a+') as f:

                if num_1 in r_list or num_2 in r_list:
                        f.write("LINUX系统基本组成题目五：执行命令crontab -l输入正确, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目五：执行命令crontab -l输入不正确, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目五:失败")

        else:
            print("操作LINUX系统基本组成题目五:成功")


class Cat_score_21(object):
    @staticmethod
    def run():
        try:

            cmd_cro = "crontab -l"
            num_1 = "15 * * * * sysmonitor  df -h >>/examdata/result/sysdf.log"

            com_ret = commands.getoutput(cmd_cro)

            with open(save_address_test, "w") as f:
                f.write(com_ret)

            f = open(save_address_test, "r")

            r_list = f.readlines()

            f.close()

            # 保存文件
            with open(save_address, 'a+') as f:

                if num_1 in r_list:
                        f.write("LINUX系统基本组成题目六：执行命令crontab -l输入正确, ---ok" + '\n')

                else:
                    f.write("LINUX系统基本组成题目六：执行命令crontab -l输入不正确, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目六:失败")

        else:
            print("操作LINUX系统基本组成题目六:成功")


class Cat_score_22(object):
    """
    题目 22
    有多少个进程，把结果存放到/examdata/result/process_running,要求把执行
    """

    @staticmethod
    def run():
        try:

            cmd_cro = "date>/examdata/result/process_running;ps -ef|wc -l>>/examdata/result/process_running"

            commands.getoutput(cmd_cro)
            line_list = []

            f = open(linux_22_find, "r")
            for line in f.readlines():
                line = line.strip('\n')
                line_list.append(line)

            f.close()

            if 'CST' in line_list[0]:

                str_1 = line_list[1]
                with open(save_address, 'a+') as f:

                    if str(str_1).isdigit():
                        f.write("LINUX系统基本组成题目七：日期信息在第一行且下一行有进程数量, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目七：第二行没有进程数量, ---error" + '\n')

            else:
                with open(save_address, 'a+') as f:
                    f.write("LINUX系统基本组成题目七：日期信息不在第一行, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目七:失败")

        else:
            print("操作LINUX系统基本组成题目七:成功")


class Cat_score_23(object):
    """
    题目 23
     1）查询file1里面空行的所在行号 2）查询file1以abc结尾的行 3）
     打印出file1文件第1到第3行，并把结果输出到/examdata/result/file1
    """

    @staticmethod
    def run():
        try:
            if os.path.exists(linux_23_server):
                cmd_1 = "grep -n ^$ /examdata/training/file1"
                cmd_2 = "grep abc$ /examdata/training/file1"
                cmd_3 = "head -n 3 /examdata/training/file1"

                com_ret_1 = commands.getoutput(cmd_1)
                com_ret_2 = commands.getoutput(cmd_2)
                com_ret_3 = commands.getoutput(cmd_3)

                with open(linux_23_file, 'w') as f:
                    f.write(com_ret_1 + '\n')

                with open(linux_23_file, 'a+') as f:
                    f.write(com_ret_2 + '\n')

                with open(linux_23_file, 'a+') as f:
                    f.write(com_ret_3  + '\n')

                # 打开file文件
                line_list_file = []
                f = open(linux_23_file, "r")
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_file.append(line)
                f.close()

                cmd_cat = 'cat /examdata/result/file1'
                com_cat = commands.getoutput(cmd_cat)
                with open(save_address_test, 'w') as f:
                    f.write(com_cat)

                # 打开临时文件
                line_list_test = []
                f = open(save_address_test, "r")
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_test.append(line)
                f.close()

                with open(save_address, 'a+') as f:
                    if line_list_file == line_list_test:
                        f.write("LINUX系统基本组成题目八：检查与1）的输出是一致, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目八：检查与1）的输出不一致, ---error" + '\n')

            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目八：文件%s不存在, ---error" + '\n') % linux_23_server,)
                    f.write("LINUX系统基本组成题目八：检查与1）的输出不一致, ---error" + '\n')


        except:
            print("操作LINUX系统基本组成题目八:失败")

        else:
            print("操作LINUX系统基本组成题目八:成功")


class Cat_score_24(object):
    """
    题目 24
     24.将 /etc/ssh/sshd_config 内容取出后，
     (1)去除开头为 # 的行 (2)去除空白行 (3)取出开头为英文字母的那几行
     (4)最终统计总行数该如何进行？
     将输出结果到/examdata/result/xtgl_08.txt
    """

    @staticmethod
    def run():
        try:
            filename_new_ssh = linux_24_new_ssh
            filename_ssh_conf = linux_24_file

            cmd_1 = " egrep -v '^(#|$)' /etc/ssh/sshd_config | wc -l"
            cmd_2 = "cat /examdata/result/xtgl_08.txt | wc -l"

            if os.path.exists(filename_new_ssh):
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目九：文件%s存在, ---ok" + '\n') % filename_new_ssh)

                if os.path.exists(filename_ssh_conf):
                    with open(save_address, 'a+') as f:
                        f.write(("LINUX系统基本组成题目九：文件%s存在, ---ok" + '\n') % filename_ssh_conf)

                    com_ret_1 = commands.getoutput(cmd_1)
                    com_ret_2 = commands.getoutput(cmd_2)

                    with open(save_address, 'a+') as f:
                        if '18' in com_ret_1 and  '18' in com_ret_2:
                            f.write("LINUX系统基本组成题目九：检查的输出是一致, ---ok" + '\n')

                        else:
                            f.write("LINUX系统基本组成题目九：检查与的输出不一致, ---error" + '\n')

                else:
                    with open(save_address, 'a+') as f:
                        f.write(("LINUX系统基本组成题目九：文件%s不存在, ---error" + '\n') % filename_ssh_conf)

            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目九：文件%s不存在, ---error" + '\n') % filename_new_ssh)

        except:
            print("操作LINUX系统基本组成题目九:失败")

        else:
            print("操作LINUX系统基本组成题目九:成功")


class Cat_score_25(object):
    """
    题目 25
     24.将 /etc/ssh/sshd_config 内容取出后，
     (1)去除开头为 # 的行 (2)去除空白行 (3)取出开头为英文字母的那几行
     (4)最终统计总行数该如何进行？
     将输出结果到/examdata/result/xtgl_08.txt
    """

    @staticmethod
    def run():
        try:
            filename_tcp = linux_25_file

            cmd_1 = r'''netstat -n | awk '/^tcp/ {++State[$NF]} END {for (a in State) print a, "\t"State[a]}' '''

            com_ret_1 = commands.getoutput(cmd_1)

            with open(save_address, 'a+') as f:
                if com_ret_1 == linux_25_ftp_test:
                    f.write("LINUX系统基本组成题目十：TCP连接状态成功, ---ok" + '\n')
                else:
                    f.write("LINUX系统基本组成题目十：TCP连接状态失败, ---error" + '\n')

            with open(filename_tcp, 'w') as f:
                f.write(com_ret_1 + '\n')

        except:
            print("操作LINUX系统基本组成题目十:失败")

        else:
            print("操作LINUX系统基本组成题目十:成功")


class Cat_score_26(object):
    """
    题目 26
     26.找/etc目录下，文件名为 init开头的文件。把结果存放到/examdata/result/init_files
    """

    @staticmethod
    def run():
        try:
            filename = linux_26_find

            cmd_1 = "ls /etc --file-type |grep -v /$|grep ^init"

            com_ret_1 = commands.getoutput(cmd_1)

            with open(filename, 'w') as f:
                f.write(com_ret_1 + '\n')

            # 打开保存地址的文件
            line_list = []
            f = open(filename, "r")
            for line in f.readlines():
                line = line.strip('\n')
                line_list.append(line)
            f.close()

            a = 0
            for i in line_list:
                if i in com_ret_1:
                    a += 1
                else:
                    pass

            with open(save_address, 'a+') as f:
                if a > 0:
                    f.write(("LINUX系统基本组成题目十一：检查%s与1）的输出是一致, ---ok" + '\n') % filename)
                else:
                    f.write(("LINUX系统基本组成题目十一：检查%s与1）的输出不一致, ---ok" + '\n') % filename)

        except:
            print("操作LINUX系统基本组成题目十一:失败")

        else:
            print("操作LINUX系统基本组成题目十一:成功")


class Cat_score_27(object):
 

    @staticmethod
    def run():
        try:
           pass
        except:
            print("操作LINUX系统基本组成题目十二:失败")

        else:
            print("操作LINUX系统基本组成题目十二:成功")


class Cat_score_28(object):
    """
    题目 28
     28.请执行命令取出linux中eth0的IP地址(请用cut，有能力者也可分别用awk,sed命令作答)。
     将命令保存到/examdata/result/fetch_ip里
    """
    # 判断是否是ip
    def isIP(self, str):
        p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if p.match(str):
            return True
        else:
            return False

    def run(self):
        try:
            filename = linux_28_find

            cmd_1 = "ifconfig eth0 |awk -F '[ :]+' 'NR==2 {print $4}' "

            com_ret_1 = commands.getoutput(cmd_1)

            with open(filename, 'w') as f:
                f.write(com_ret_1 + '\n')

            with open(save_address, 'a+') as f:
                if self.isIP(com_ret_1):

                    f.write("LINUX系统基本组成题目十三：eth0的IP地址正确, ---ok" + '\n')
                else:
                    f.write("LINUX系统基本组成题目十三：eth0的IP地址错误, ---error" + '\n')

        except:
            print("操作LINUX系统基本组成题目十三:失败")

        else:
            print("操作LINUX系统基本组成题目十三:成功")


class Cat_score_29(object):
    """
    题目 29
     29.修改系统登陆提示,当用户登录系统时，提示：hello, welcome to login linux trainning system
    """
    @staticmethod
    def run():
        try:
            filename = linux_29_find

            if os.path.exists(filename):
                f = open(filename, 'r')
                read_list = f.readlines()
                f.close()

                if len(read_list) > 0:

                    a = 0
                    for read_str in read_list:
                        if linux_29_find_1 in read_str:
                            a += 1
                        else:
                            pass

                    with open(save_address, 'a+') as f:
                        f.write(("LINUX系统基本组成题目十四：文件%s存在提示信息, ---ok" + '\n') % filename)

                else:
                    with open(filename, 'w') as f:
                        f.write('hello, welcome to login linux  trainning system' + '\n')

            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目十四：文件%s不存在, ---error" + '\n') % filename)

        except:
            print("操作LINUX系统基本组成题目十四:失败")

        else:
            print("操作LINUX系统基本组成题目十四:成功")


class Cat_score_30(object):
    """
    题目 29
     29.修改系统登陆提示,当用户登录系统时，提示：hello, welcome to login linux trainning system
    """
    @staticmethod
    def run():
        try:

            cmd_ret = "cat /boot/grub/grub.conf "
            com_ret = commands.getoutput(cmd_ret)

            # re匹配
            re_ret_5 = re.search(r'timeout=\d+', com_ret)
            ret = re_ret_5.group()
            ret_num = re.search(r'\d+', str(ret))

            with open(save_address, 'a+') as f:
                if ret_num.group() == '5':
                    f.write(("LINUX系统基本组成题目十五：菜单引导的时候等待时间为:%s, ---error" + '\n') % ret)

                else:
                    f.write(("LINUX系统基本组成题目十五：菜单引导的时候等待时间为:%s, ---error" + '\n') % ret)

        except:
            print("操作LINUX系统基本组成题目十五:失败")

        else:
            print("操作LINUX系统基本组成题目十五:成功")


class Cat_score_31(object):
    """
    题目 31
     31.将date和hostname的输出添加到/examdata/result/hosts.bak文件
    """

    @staticmethod
    def run():
        try:
            filename_host = linux_31_find

            # 判断文件是否存在
            if os.path.exists(filename_host):

                # 查看服务器hosts文件
                f = open(filename_host, 'r')

                line_list_hosts = []
                for line in f.readlines():
                    line = line.strip('\n')
                    line_list_hosts.append(line)

                f.close()

                # 判断服务器文件是否为空
                if len(line_list_hosts) > 0:

                    cmd = "cat /examdata/result/hosts.bak|egrep '(2018|rhel65-training)' "
                    com_ret = commands.getoutput(cmd)

                    # 临时保存文件
                    with open(save_address_test, 'w') as f:
                        f.write(com_ret)

                    # 打开临时文件, 去换行
                    line_list_find = []
                    for line in f.readlines():
                        line = line.strip('\n')
                        line_list_find.append(line)

                    a = 0
                    # 遍历临时文件列表，判断
                    for i in line_list_find:
                        if i in line_list_hosts:
                            a += 1
                        else:
                            pass

                    if a >= 2:
                        f.write("LINUX系统基本组成题目十六：文件里包含日期和主机名, ---ok" + '\n')

                    else:
                        f.write("LINUX系统基本组成题目十六：文件里不包含日期和主机名, ---error" + '\n')

                else:
                    f.write(("LINUX系统基本组成题目十六：文件:%s为空, ---error" + '\n') % filename_host)

            else:
                with open(save_address, 'a+') as f:
                    f.write(("LINUX系统基本组成题目十六：文件:%s不存在, ---error" + '\n') % filename_host)

        except:
            print("操作LINUX系统基本组成题目十六:失败")

        else:
            print("操作LINUX系统基本组成题目十六:成功")


def run():
    Cat_score_16().run()
    Cat_score_17().run()
    Cat_score_18().run()
    Cat_score_19().run()
    Cat_score_20().run()
    Cat_score_21().run()
    Cat_score_22().run()
    Cat_score_23().run()
    Cat_score_24().run()
    Cat_score_25().run()
    Cat_score_26().run()
    # text_score_27.Cat_score_27().run()
    Cat_score_28().run()
    Cat_score_29().run()
    Cat_score_30().run()
    Cat_score_31().run()

run()

