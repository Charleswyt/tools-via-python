#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on 2018.12.4
Finished on 2018.12.4
Modified on 

@author: Yuntao Wang
"""

import os
import socket
from glob import glob


buffer_size = 65536
encoding_type = "utf-8"
visible_file_path = ""


def communication_server(connection_host=socket.gethostname(), connection_port=1234, 
        max_connection=5):
    """
    :param connection_host:
    :param connection_port:
    :param max_connection:
    :param msg_type: 
    :return:
        
    """

    socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)       # create socket object
    host = connection_host                                                  # host of connection
    port = connection_port                                                  # port of connection
    
    socket_server.bind((host, port))                                        # bind host and port
    socket_server.listen(max_connection)                                    # set max connection
    
    # print basci info
    print("Host: %s" % connection_host)
    print("Port: %d" % connection_port)
    print("Max Connection: %d" % max_connection)

    while True:
        socket_client, addr = socket_server.accept()                        # build the connection
        receive_message_byte = socket_client.recv(buffer_size)
        receive_message_str = str(receive_message_byte, encoding = encoding_type)
        
        split_content = receive_message_str.split("+")
        request_type = split_content[0]
        
        print("Address %s is connected." % str(addr))
        # request_type = 
        print("Request for %s" % request_type)        

        if request_type == "None":
            msg = "Request Null." + "\r\n"
        elif request_type == "file_list":
            file_list = sorted(glob(visible_file_path + "/*"))
            msg = str(file_list)
        elif request_type == "file":
            file_path = split_content[1]
            if os.path.exists(file_path):
                with open(file_path, "rb") as file:
                    msg = file.read()
            else:
                msg = str()
        else:
            msg = str()
            print("Wrong type of file, please try again.")

        try:
            socket_client.send(msg.encode(encoding_type))
        except AttributeError:
            socket_client.send(msg)

        socket_client.close()


if __name__ == "__main__":
    communication_server()