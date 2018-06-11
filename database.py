#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.5.2
Finished on 2018.5.2
@author: Wang Yuntao
"""

import pymysql

host = "127.0.0.1"
user = "root"
password = "123456"
port = 3306
database = "AudioSteganalysis"
connect = pymysql.connect(host=host, db=database, user=user, password=password, port=port, charset="utf8mb4")
cursor = connect.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print("Database version : %s " % data)
