# -*- coding: utf-8 -*-
#!/usr/bin/python

import os


# 获取文件名 返回一个文件名列表
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return files


files_list = file_name('./')[:-1]


# 遍历文件名，修改参数

for files in files_list:
    f = open(files, 'r')
    # 读取文件每一个文件里面内容
    res_read_list = f.readlines()
    f.close()
    main_index = 0
    coding_index = 0

    for index, i in enumerate(res_read_list):
        if '# -*- coding: utf-8 -*-' in i:
            coding_index = index

    res_read_list.insert(coding_index+1, """
try:
    """)

    for index, i in enumerate(res_read_list):
        if "except:" in i:
            main_index = index

    if main_index:
        new_list = res_read_list[:main_index]
        new_index = main_index - 1

        new_list.insert(new_index, """
        except Exception as e:
            print str(e) + ' ---except'
    
        else:
            f.close()
    
        finally:
            with open(save_address) as f:
                num = f.readlines()
    
            # 总题目数
            sum = len(num)
            # 一题多少分
            average = 100 // sum
    
            # 正确的题目总数
            timu_all = 0
            for i in num:
                print i.strip("\\n").split(":")[1]
    
                if '---ok' in i:
                    timu_all += 1
    
            if timu_all == sum:
                total_score = 100
            else:
                total_score = timu_all * average
    
            print str(total_score) + ' ---score'
    
    
except Exception as e:
    print str(e) + ' ---except'

else:
    if __name__ == '__main__':
        run()
""")


        f = open(files, "w")
        indexs = 0
        for index, i in enumerate(new_list):
            if index> coding_index:
                f.write("    " + i)

            else:
                f.write(i)

            if "except Exception as e:" == i:
                indexs = index

            if indexs >= index:
                f.write(i)

        f.close
    else:
        print 'except:不存在'

