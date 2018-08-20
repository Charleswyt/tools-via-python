#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.8.17
Finished on 2018.8.20
@author: Wang Yuntao
"""

import os
import sys
import hashlib
from collections import Counter


def fullfile(file_dir, file_name):
    """
    fullfile as matlab
    :param file_dir: file dir
    :param file_name: file name
    :return: a full file path
    """
    full_file_path = os.path.join(file_dir, file_name)
    full_file_path = full_file_path.replace("\\", "/")

    return full_file_path


def get_files_list(files_path):
    """
    :param files_path: path of MP3 files for move
    :return: a list containng file path
    """
    filename = os.listdir(files_path)
    files_list = []
    for file in filename:
        file_path = fullfile(files_path, file)
        if not os.path.isfile(file_path):
            pass
        else:
            files_list.append(file_path)
    
    return files_list


def get_file_name(file_path, sep="/"):
    """
    get the name of file
    :param file_path: file path
    :param sep: separator
    :return: file name
    """
    if os.path.exists(file_path):
        file_path.replace("\\", "/")
        file_name = file_path.split(sep=sep)[-1]
    else:
        file_name = None
    return file_name


def get_file_md5(file_path):
    """
    get MD5 of file
    :param file_path: file path
    :return:
        hash_code: hash code of file
    """
    hash_code = None
    if os.path.exists(file_path):
        file = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(file.read())
        hash_code = md5_obj.hexdigest()
        file.close()

    return hash_code


def get_duplication(files_path):
    """
    get duplication list
    :param files_path: path to be retrieved of files
    :return:
        duplication_file_list: a list containing duplicated files
        left_list: a list containing all left files (e.g. 0, 1, 2 are duplicated files, file 2 will be left)
    """
    # get files path list
    files_path_list = get_files_list(files_path)
    
    # get hash code list
    hash_code_list = []
    for file_path in files_path_list:
        hash_code = get_file_md5(file_path)
        hash_code_list.append(hash_code)
    
    # get number of each hash code, return a dict variable
    Counter_list = Counter(hash_code_list)

    # get duplication list
    duplications_list, left_list = [], []
    if len(Counter_list.values()):
        for item in Counter_list.items():
            if item[1] > 1:
                duplication_list = [index for index in range(len(hash_code_list)) if hash_code_list[index] == item[0]]
                left_list.append(duplication_list[-1])
                del duplication_list[-1]
                duplications_list.extend(duplication_list)
            else:
                pass
    else:
        pass

    # get duplication file list
    duplication_file_list = []
    for order in duplications_list:
        duplication_file_list.append(files_path_list[order])

    return duplication_file_list


def file_remove(duplication_file_list):
    """
    remove duplicated files
    :param duplication_file_list: a list containing duplicated files
    :return
        NULL
    """
    for file in duplication_file_list:
        os.remove(file)


if __name__ == "__main__":
    params_num = len(sys.argv)
    if params_num == 2:
        files_path = sys.argv[1]
        duplication_file_list = get_duplication(files_path)
        if len(duplication_file_list) == 0:
            print("No duplicated files in this path.")
        else:
            file_remove(duplication_file_list)
            print("All duplicated files have been removed.")
    else:
        print("Please input the command as the format of {python duplcatate_search.py \"files_path\"}.")