# import socket
#
#
# def handle_client(client_socket):
#     recv_data = client_socket.recv(1024 * 1024).decode("utf-8")
#     # 接受信息
#     print(recv_data)  # 接收到的信息被分成了好几段
#     request_hander_lines = recv_data.splitlines()  # 将信息按行拆分成一个列表
#     print("___________________________")
#     for line in request_hander_lines:
#         print(line)
#     print("____________________________________")
#
#     # 返回信息
#     # 表头信息
#     response_head = "HTTP/1.1 200 OK\r\n"  # \r\n都是换行符，通过\r\n就可以实现换行
#     response_head += "\r\n"
#     # body信息
#     response_body = input("请输入要发送的内容:")
#     # response_body = "hello"
#     response_all = response_head + response_body
#     client_socket.send(response_all.encode("utf-8"))
#     # client_socket.close()
#
#
# def main():
#     # 创建一个套接子
#     server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     # 绑定地址
#     server_socket.bind(("", 7788))
#     # server_socket.setsockopt(socket.SOLSOCKET, socket.SO_REUSEADDR, 1)
#     server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#     print("_______________1__________________")
#     server_socket.listen(128)
#
#     #
#     while True:
#         # 设置为监听
#
#         print("________________2______________")
#
#         new_client, new_client_addr = server_socket.accept()
#         print("________________3_________________")
#         handle_client(new_client)
#         new_client.close()
#
#
# if __name__ == "__main__":
#     main()


# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 21:14:56 2020

@author: acer
"""

import socket
# import process


class WSGIServer(object):
    def __init__(self, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 绑定地址
        self.server_socket.bind(("", port))
        # 这里直接将端口号变量装进了元祖中， 不知道可不可以
        # server_socket.setsockopt(socket.SOLSOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # print("_______________1__________________")
        # self.server_socket.listen(128)


    def handle_client(self, client_socket):
        recv_data = client_socket.recv(1024 * 1024).decode("utf-8")
        # 接受信息
        print(recv_data)  # 接收到的信息被分成了好几段
        request_hander_lines = recv_data.splitlines()  # 将信息按行拆分成一个列表
        print("___________________________")
        for line in request_hander_lines:
            print(line)
        print("____________________________________")

        # 返回信息
        # 表头信息
        response_head = "HTTP/1.1 200 OK\r\n"  # \r\n都是换行符，通过\r\n就可以实现换行
        response_head += "\r\n"
        # body信息
        # response_body = input("请输入要发送的内容:")

        response_body = "hello"
        response_all = response_head + response_body
        client_socket.send(response_all.encode("utf-8"))
        # client_socket.close()

    def run_forver(self):
        print("_______________1__________________")
        self.server_socket.listen(128)
        while True:
            # 设置为监听

            print("________________2______________")

            new_client, new_client_addr = self.server_socket.accept()
            print("________________3_________________")
            self.handle_client(new_client)
            new_client.close()
            # 在我们调用子套接字通信结束的命令，三次握手四次挥手开始，此时我们并没有与new_client断开联系,
            # 从而导致在 server_socket.accept()这里并没有发生堵塞
            # 而是正式发起了三次握手四次挥手，我们回送内容的body如果是input，让服务器输入发送内容好几次
            # 而链接我们的客户端，并未显示我们的Input,因为这是三次握手和四次挥手的内容


def main():
    httpd = WSGIServer(7788)
    httpd.run_forver()


if __name__ == "__main__":
    main()
