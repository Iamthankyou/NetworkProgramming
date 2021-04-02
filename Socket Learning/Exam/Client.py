import socket
import sys
import select
import argparse

if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port", type=str, default=2020)
    PORT = int(parse.parse_args().port)

    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sk:
        sk.connect((HOST,PORT))
        # while True:
        sk.sendto("Hello server".encode('utf-8'), (HOST,PORT))
        mess,client_addr = sk.recvfrom(1024)
        print(mess.decode('utf-8'))

        while True:
            sk.sendto("Hello server".encode('utf-8'), (HOST, PORT))
            list_sockets = [sys.stdin, sk]
            r,w,e = select.select(list_sockets,[],[])

            for i in r:
                if i == sk:
                    mess, client_addr = sk.recvfrom(1024)
                    print(mess.decode('utf-8'))
                else:
                    mess = input('Type list number: ')
                    if mess:
                        sk.sendto(mess.encode('utf-8'), (HOST, PORT))
