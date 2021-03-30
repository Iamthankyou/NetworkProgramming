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
            data = client_sk.recv(4096)
            filename = data.decode('utf-8')
            if data.decode('utf-8') == 'tam biet':
                client_sk.close()

            else:
                try:
                    f = open('D:/Python/Code/LapTrinhMang/Include/Test/'+ filename +'.txt', 'r')

                    for l in f:
                        print(l)
                        data = l
                        client_sk.send(data.encode('utf-8'))
                    f.close()
                    data = '\nhetfile'
                    client_sk.send(data.encode('utf-8'))

                except FileNotFoundError as e:
                    print("Khong tim thay file{}".format(e))
                    sys.exit()

    sk.close()