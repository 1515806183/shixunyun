#!/usr/bin/python
# -*- coding: utf-8 -*-
import os


# 获取文件名 返回一个文件名列表
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


files_list = file_name('./')[:-1]

for files in files_list:

    f = open(files, 'r')

    res_read_list = f.readlines()

    f.close()

    for index, i in enumerate(res_read_list):
        if "print total_score" in i:
            res_read_list.pop(index - 1)
            res_read_list.pop(index - 2)
            res_read_list.pop(index - 3)

    f = open(files, "w")

    for i in res_read_list:
        f.write(i)

    f.close
