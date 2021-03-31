import socket
import argparse

HOST = 'localhost'
parser = argparse.ArgumentParser()
parser.add_argument("-port", type = str, default=1206)
args = parser.parse_args()
PORT = int(args.port)

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        conn, addr = s.accept()

        print ('Watting for love')

        with conn:
            print('Server connected by ',addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print('Client call: ',data.decode('utf8'))

                f = open(data,"r")

                conn.sendall(f.read().encode('utf8'))

if __name__ == '__main__':
    main()
