#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

# 获取文件名 返回一个文件名列表
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


files_list = file_name('./')[:-1]

# 遍历文件名，修改参数

for files in files_list:
    f = open(files, 'r')

    res_read_list = f.readlines()

    f.close()

    # 加入#!/usr/bin/python
    res_read_list.insert(0, '#!/usr/bin/python\n')

    main_index = 0
    # 寻找save_address = "./score.txt" 并进行替换
    for index, i in enumerate(res_read_list):
        if 'save_address = "./score.txt"' in i:
            res_read_list.pop(4)
            res_read_list.insert(4, 'save_address = "/tmp/score.txt"\n')
        if "if __name__ == '__main__':" in i:
            main_index = index

    res_read_list.pop(main_index + 1)
    res_read_list.pop(main_index)

    res_read_list.insert(main_index, """
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

    print('\\033[0;34;40m总题目: %s 道\\033[0m' % sum)
    print '\\033[0;34;40m正  确: %s 道\\033[0m' % timu_all
    print '\\033[0;34;40m详细内容: %s 路径下\\033[0m' % save_address
    print total_score

if __name__ == '__main__':
    run()""")


    f = open(files, "w")

    for i in res_read_list:
        f.write(i)

    f.close
