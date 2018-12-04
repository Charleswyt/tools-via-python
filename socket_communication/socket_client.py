#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.12.4
Finished on 2018.12.4
Modified on 

@author: Yuntao Wang
"""

import socket

buffer_size = 65536
encoding_type= "utf-8"


def communication_client(connection_host=socket.gethostname(), connection_port=1234,
                         request_type="None", request_file_path=None, write_file_path="receive.txt"):
    """
    :param connection_host: host of connected server
    :param connection_port: port of connected server
    :param request_type: type of request, None, file, file_list
    :param write_file_path: path of received file
    :return:
        NULL
    """

    socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # create socket object
    socket_host = connection_host                                           # host of connection
    socket_port = connection_port                                           # port of connection
    socket_client.connect((socket_host, socket_port))                       # bind host and port
    
    # send request to server
    send_message = request_type
    if request_type == "file":
        send_message += ("+" + request_file_path)
    
    socket_client.send(bytes(send_message, encoding=encoding_type))
    msg = socket_client.recv(buffer_size)                                   # set buffer size
    
    if request_type == "file":
        if not len(msg) == 0:
            with open(write_file_path, "wb")as file:
                file.write(msg)
            print("The file is saved to %s" % write_file_path)
        else:
            print("Received message is of zero length.")
    else:
        print(msg.decode('utf-8'))

    socket_client.close()
    

if __name__ == "__main__":
    host = ""
    port = 1234
    request = "file"
    saved_file_path = "test.txt"
    file_path = ""
    communication_client(host, port, request, file_path, saved_file_path)
