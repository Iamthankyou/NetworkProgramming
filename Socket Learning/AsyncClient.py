import socket
import argparse
import sys
import select


HOST = 'localhost'
parse = argparse.ArgumentParser()
parse.add_argument("-port",type = str, default=2020)
PORT = int(parse.parse_args().port)
client = []

if __name__ == '__main__':
    name = input('Enter your nickname: ')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            print('Connect successfully!!')
            s.send(bytes(name, 'utf-8'))
            while True:
                sockets_list = [sys.stdin, s]
                read_sockets, write_socket, error_socket = select.select(sockets_list, [], [])
                for socks in read_sockets:
                    if socks == s:
                        message = socks.recv(1024).decode()
                        print(message)
                    else:
                        message = input()
                        s.send(bytes(name + ': ' + message, 'utf8'))
        except Exception as e:
            print(e)