import socket
import multiprocessing


class WSGIServer(object):
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定套接字端口
        self.server_socket.bind(("", 7788))
        # 设置为监听模式
        self.server_socket.listen(128)

    def dealing_client(self, new_client):
        get_request = new_client.recv(1024).decode("utf-8")
        request_header_lines = get_request.splitlines()                # 将的到的内容按行拆成一个列表
        pass

    def recv_connect(self):
        # 接收到用户
        while True:
            new_client, new_client_addr = self.server_socket.accept()
            process_1 = multiprocessing.Process(target=self.dealing_client, args=(new_client, ))

def main():
    pass


if __name__ == "__main__":
    main()