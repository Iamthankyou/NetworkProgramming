import socket
import argparse

HOST = 'localhost'
parser = argparse.ArgumentParser()
parser.add_argument("-port", type = str, default=1206)
args = parser.parse_args()
PORT = int(args.port)

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        while True:
            data = input()
            if not data:
                break

            s.sendall(data.encode('utf8'))

            dataRev = s.recv(1024)

            if dataRev:
                print('Server call reback ',dataRev)

if __name__ == '__main__':
    main()