import socket
import argparse
import sys
import select

if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port", type = str, default=2020)
    PORT = int(parse.parse_args().port)
    client = []

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sk:
        while True:
            socket_lists = [sys.stdin,sk]
            r,w,e = select.select(socket_lists,[],[])

            for sock in r:
                if sock == sk:
                    mess = sk.recv(1024).decode('utf-8')
                    print(mess)
                else:
                    mess = input('Type something: ')
                    sk.sendto(mess.encode('utf-8'),(HOST,PORT))
