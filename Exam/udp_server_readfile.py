import socket
import os
import argparse

HOST = 'localhost'
parse = argparse.ArgumentParser()
parse.add_argument('-port', type=str, default=2000)
args = parse.parse_args()
PORT = int(args.port)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((HOST, PORT))

        while True:
            data, addr = s.recvfrom(1024)
            print('Client connect to server is: ', addr)
            print('Client send to server: ', data.decode('utf-8'))

            if data:
                try:
                    f = open(data, "r")
                    s.sendto(f.read().encode('utf-8'), addr)
                except OSError as e:
                    s.sendto(str(e).encode('utf-8'), addr)
                    print(e)

if __name__ == '__main__':
    main()
