# Viết chương trình client-sever
# client kết nối gửi "Hello sever" đến sever
# sever accept, in địa chỉ client, gửi lời chào "Hello client" cho client

import socket
import sys

if __name__ == "__main__":
    # while True:
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # sk.connect(('www.linux.org',80))
        sk.connect(('127.0.0.1', 9050))
    except socket.error as e:
        print('error: {}'.format(e))
        sys.exit()
    print('Da tao Socket!!!', end=" ")

    while True:
        print("Text: ")
        data = str(input())
        # data = 'GET / HTTP/1.0\r\n\r\n'
        sk.send(data.encode('utf-8'))
        while True:
            data = sk.recv(4096) # Nhận data từ sever
            if not data:
                break
            print('Sever gui: ', data.decode('utf-8'))
        if data.decode('utf-8') == "/stop":
            print("test")
            break
    sk.close()
