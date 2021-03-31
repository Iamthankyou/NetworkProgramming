import socket
import string
import sys
from time import ctime

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(('127.0.0.1', 9050))
    sk.listen(10)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        client_sk, client_addr = sk.accept()
        while True:
            data = client_sk.recv(40960)
            filename = data.decode('utf-8')
            if data.decode('utf-8') == 'tam biet':
                client_sk.close()

            else:
                try:
                    f = open(filename, 'r')
                    client_sk.send(f.read().encode('utf8'))
                    f.close()

                except FileNotFoundError as e:
                    print("Khong tim thay file{}".format(e))
                    sys.exit()

    sk.close()
