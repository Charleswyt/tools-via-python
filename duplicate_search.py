#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.8.17
Finished on 2018.8.17
@author: Wang Yuntao
"""

import os
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
    md5 = None
    if os.path.exists(file_path):
        file = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(file.read())
        hash_code = md5_obj.hexdigest()
        file.close()

    return md5


def get_duplication(files_path):
    """
    get duplication list
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
    for item in Counter_list.items():
        if item[1] > 1:
            duplication_list = [index for index in range(len(hash_code_list)) if hash_code_list[index] == item[0]]

    # get duplication file list
    duplication_file_list = []
    for i in range(len(duplication_list)):
        duplication_file_list.append(files_path_list[i])

    return duplication_file_list


if __name__ == "__main__":
    files_path = "E:/Myself/2.database/1.wav"
    hash_code_list = get_duplication(files_path)
    print(hash_code_list)
    print(type(hash_code_list))
