import socket

HOST = 'localhost'
PORT = 1200

def main():
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        s.sendall(b'server1.py')

if __name__ == '__main__':
    main()