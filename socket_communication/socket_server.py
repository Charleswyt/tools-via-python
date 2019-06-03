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
        max_connection=5, encoding_type="utf-8"):
    """
    :param connection_host: the host for communication
    :param connection_port: the port for communication
    :param max_connection: the maximum number of connections
    :param msg_type: the type of message for communication
    :param encoding_type: the type of message encoding
    :return:
        NULL
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
        receive_message_str = str(receive_message_byte, encoding=encoding_type)
        
        split_content = receive_message_str.split("+")
        if len(split_content) == 2:
            request_type = split_content[0]
        else:
            request_type = "None"
        
        print("Address %s is connected." % str(addr))
        print("Request for %s" % request_type)        

        if request_type == "None":
            msg = "Request Null." + "\r\n"
        elif request_type == "message":
            msg = split_content[1]
            print("receive message: %s" % msg)
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