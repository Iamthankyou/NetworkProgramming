import socket
import argparse
import sys
import select

if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port",type=str,default=2020)
    PORT = int(parse.parse_args().port)

    name = input('Type nickname: ')

    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sk:
        sk.connect((HOST,PORT))
        print("Connected")
        sk.send(name.encode('utf-8'))

        while True:
            socket_lists = [sys.stdin,sk]
            r, w, e = select.select(socket_lists,[],[])

            for sock in r:
                if sock == sk:
                    mess = sk.recv(1024)

                    print("Server: " + mess.decode('utf-8'))
                    # mess = input('Type showlist, name file: ')
                    # sk.send(mess.encode('utf-8'))
                else:
                    mess = input('Type showlist, name file: ')
                    if mess:
                        sk.send(mess.encode('utf-8'))