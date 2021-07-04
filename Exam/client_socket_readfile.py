import socket
import os
import argparse

HOST = 'localhost'
parse = argparse.ArgumentParser()
parse.add_argument('-port', type=str, default=2000)
args = parse.parse_args()
PORT = int(args.port)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        while True:
            data = input('Please typing name file: ')
            if not data:
                break

            s.sendall(data.encode('utf-8'))

            dataRev = s.recv(1024)

            if dataRev:
                print('Server send: ', dataRev.decode('utf-8'))

if __name__ == '__main__':
    main()