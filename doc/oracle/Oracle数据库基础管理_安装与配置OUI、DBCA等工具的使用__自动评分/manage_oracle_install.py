# coding=utf-8
# 数据库得分保存地址
username = "system"
pwd = "oracle"
ip = "127.0.0.1"
tns = "oradb"

# 正式文件
save_address = "/etc/vsfox/score.txt"
# 测试文本
save_address_test = './test.txt'

oreacle_1_file = '/home/oracle/.bash_profile'
oreacle_2_file = '/examdata/result/start_db.log'

import commands
import os


class Cat_score_1(object):

    @staticmethod
    def run():
        try:
            filename = oreacle_1_file
            if os.path.exists(filename):

                cmd = "cat /home/oracle/.bash_profile"
                cmd_cat = commands.getoutput(cmd)

                with open(save_address, 'w') as f:
                    if 'PATH' in cmd_cat and '$ORACLE_HOME/bin' in cmd_cat and 'ORACLE_SI' in cmd_cat:
                        f.write(("数据库安装与配置题目一：文件: %s中存在关键信息, ---ok" + '\n') % filename)

                    else:
                        f.write(("数据库安装与配置题目一：文件: %s中不存在关键信息, ---errot" + '\n') % filename)

            else:
                with open(save_address, 'w') as f:
                    f.write(("数据库安装与配置题目一：文件: %s不存在, --- error" + '\n') % filename)

        except:
            print("操作数据库安装与配置题目一:失败")


        else:
            print("操作数据库安装与配置题目一:成功")


class Cat_score_2(object):

    @staticmethod
    def run():
        try:
            filename = oreacle_2_file
            if os.path.exists(filename):

                cmd = "cat /examdata/result/start_db.log"
                cmd_cat = commands.getoutput(cmd)

                with open(save_address, 'a+') as f:
                    if 'startup nomount' in cmd_cat and 'alter database mount' in cmd_cat and 'alter database open' in cmd_cat:
                        f.write(("数据库安装与配置题目二：文件: %s中存在关键信息, ---ok" + '\n') % filename)

                    else:
                        f.write(("数据库安装与配置题目二：文件: %s中不存在关键信息, ---errot" + '\n') % filename)

            else:
                with open(save_address, 'a+') as f:
                    f.write(("数据库安装与配置题目二：文件: %s不存在, --- error" + '\n') % filename)

        except:
            print("操作数据库安装与配置题目二:失败")


        else:
            print("操作数据库安装与配置题目二:成功")


def run():
    Cat_score_1().run()
    Cat_score_2().run()


run()
