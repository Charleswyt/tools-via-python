"""
Created on 2019.05.30
Finished on 2019.05.30
Modified on 
@author: Yuntao Wang
"""

import socket


def communication_client(connection_host=socket.gethostname(), connection_port=1234,
                         request_type="None", encoding_type="utf-8", buffer_size=1024,
                         request_file_path=None, send_message="hello", write_file_path="receive.txt"):
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
    if request_type == "file":
        send_message = "file+" + request_file_path
    elif request_type == "message":
        send_message = "message+" + send_message
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
    host = "192.168.2.159"
    port = 1234
    request = "None"
    send_message = "hello world"
    request_file_path = "C:/Users/CatKing/Desktop/code/audio_steganalysis_ml/plot/test.txt"
    saved_file_path = "C:/Users/CatKing/Desktop/receive.txt"

    communication_client(connection_host=host, connection_port=port, request_type=request,
                         request_file_path=request_file_path, send_message=send_message,
                         write_file_path=saved_file_path)
    