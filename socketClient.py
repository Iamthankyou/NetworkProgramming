#CLIENT
import socket

if __name__ == '__main__':
    s = socket.socket()
    s.connect(('localhost',4008))

    s.send("100 300".encode())

    msg = s.recv(1024)

    while msg:
        print('Recvied',msg.decode())
        msg = s.recv(1024)

    s.close()