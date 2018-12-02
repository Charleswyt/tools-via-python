#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.5.2
Finished on 2018.5.2
@author: Wang Yuntao
"""

import os
import sys
import time
import win_unicode_console

win_unicode_console.enable()


def get_file_path(file_folder, file_types):
    """
    获取待统计文件的路径
    :param file_folder: 代码所在文件路径
    :param file_types: 待统计文件的类型
    :retuen:
        file_list: 当前文件夹下的文件列表(完整路径)
    """
    file_path_list = list()
    for parent, dirnames, filenames in os.walk(file_folder):
        for filename in filenames:
            extension = filename.split('.')[-1]
            if extension in file_types:
                file_path_list.append(parent + "/" + filename)
    
    return file_path_list


def get_file_name(file_path):
    """
    根据文件路径获取文件名
    :param file_path: 文件路径
    :return:
        file_name: 文件名
    """
    file_name = file_path.split("/")[-1]

    return file_name


def count_line(file_name):
    """
    统计文件的内容行数
    :param file_name: 文件名
    :return:
        count: 当前文件的内容行数
    """
    count = 0
    for file_line in open(file_name, encoding="utf-8", errors='ignore').readlines():
        if file_line != '' and file_line != '\n':  # 过滤掉空行
            count += 1

    return count


def get_lines(file_folder, file_types):
    """
    获取当前文件夹下的代码量
    :param file_folder: 代码所在文件路径
    :param file_types: 待统计文件的类型
    """
    file_path_list = get_file_path(file_folder, file_types)
    index, total_lines = 0, 0
    
    template_title = "{:^5}\t{:36}{:^15}"
    template_content = "{:^5}\t{:36}{:^15}"
    print(template_title.format("ID", "file name", "lines"))
    print("=======================================================")
    
    for file_path in file_path_list:
        file_name = get_file_name(file_path)
        lines = count_line(file_path)
        total_lines = total_lines + lines
        index += 1
        print(template_content.format(index, file_name, lines))

    print("=======================================================")
    print("total lines: %d" % total_lines)
    

if __name__ == "__main__":
    params_num = len(sys.argv)
    if params_num == 1:
        print("Please input the command as the format of {python source_code_statistics.py \"code_files_floder\" \"code_type (default is cpp)\"} ")
    else:
        if params_num == 2:
            args_file_folder = sys.argv[1]
            args_file_types = ["cpp"]
        else:
            args_file_folder = sys.argv[1]
            i = 2
            args_file_types = []
            while i < params_num:
                args_file_types.append(sys.argv[i])
                i += 1

        startTime = time.clock()
        get_lines(args_file_folder, args_file_types)
        print('Done! Cost Time: %0.2f second' % (time.clock() - startTime))
