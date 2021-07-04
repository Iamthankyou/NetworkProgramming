import socket
import os
import argparse

HOST = 'localhost'
parse = argparse.ArgumentParser()
parse.add_argument("-port", type=str, default=2000)
args = parse.parse_args()
PORT = int(args.port)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen(5)
        conn, addr = s.accept()

        with conn:
            print('Connected to ', addr)
            while True:
                data = conn.recv(1024).decode('utf-8')
                if data:
                    print(data)

                    try:
                        f = open(data,'r')
                        conn.sendall(f.read().encode('utf-8'))
                    except OSError as e:
                        print(e)
                        conn.sendall(str(e).encode('utf-8'))

if __name__ == '__main__':
    main()
