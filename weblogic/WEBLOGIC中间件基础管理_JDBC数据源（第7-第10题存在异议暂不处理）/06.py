# -*- coding: utf-8 -*-
import commands, os, re
test_name = 'JDBC数据源题目六'
test_vlu = '是否存在参数'

save_address = "./score.txt"
name = "/examdata/result/log_jdbc6.txt"


def run():
    f = open(save_address, 'w')
    # 1
    if os.path.exists(name):
        f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))

        cmd = "cat %s" % name
        com_ret = commands.getoutput(cmd).lower().replace(" ", "")
        if "<Error> <Deployer> <BEA-149205> <Failed to initialize the application 'jdbc6'".lower().replace(" ", "") in com_ret:
            f.write("%s:%s错误 ---error\n" % (test_name, test_vlu))
        else:
            f.write("%s:%s正确 ---ok\n" % (test_name, test_vlu))
    else:
        f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))
        f.write("%s:查看文件%s不存在, 无法查询%s ---error\n" % (test_name, name, test_vlu))

    f.close()
    print("%s:成功" % test_name)


if __name__ == '__main__':
    run()