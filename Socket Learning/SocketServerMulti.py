import socket
import os
from _thread import *

HOST = 'localhost'
PORT = 1200
ThreadCount = 0

sk = socket.socket()

try:
    sk.bind((HOST,PORT))
except socket.error as e:
    print(str(e))

print('Watting for a connection')
sk.listen(5)

def thread_client(conn):
    conn.sendall(str.encode('Welcome from server'))
    while True:
        data = conn.recv(1024)
        rep = 'Server say: '+ data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(rep))
    conn.close()

if __name__ == '__main__':
    while True:
        conn,addr = sk.accept()
        print('Connected to: ' + addr[0]+":"+str(addr[1]))
        start_new_thread(thread_client,(conn,))
        ThreadCount+=1
        print('Thread num: '+ str(ThreadCount))
    sk.close()




