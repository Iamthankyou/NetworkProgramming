import socket
import os

HOST = 'localhost'
PORT = 1200

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT))
        s.listen()
        conn,addr = s.accept()

        print(os.listdir())

        with conn:
            print('Connnected by',addr)
            while True:
                data = conn.recv(1024).decode('utf8')
                if not data:
                    break

                print(data)

                try:
                    f = open(data,"r")
                    print(f.read())
                except OSError:
                    print("Error")

if __name__ == '__main__':
    main()