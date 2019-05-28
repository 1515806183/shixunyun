# -*- coding: utf-8 -*-
test_name = '数据库参数维护课件题目六'

import os
save_address = "./score.txt"
name = "/examdata/result/pfile_tmp.ora"


def run():
    try:
        f = open(save_address, 'w')
        if os.path.exists(name):
            f.write("%s:文件%s,存在, ---ok\n" % (test_name, name))
        else:
            f.write("%s:文件%s,不存在, ---error\n" % (test_name, name))

    except:
        print("%s:\033[0;34m失败\033[0m" % test_name)
        raise

    else:
        print("%s:成功" % test_name)
        f.close()


if __name__ == '__main__':
    run()