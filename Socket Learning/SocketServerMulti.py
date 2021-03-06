import socket
import os
from _thread import *
import argparse

HOST = 'localhost'
parse = argparse.ArgumentParser()
parse.add_argument("-port",type = str,default=2020)
args = parse.parse_args()

PORT = int(args.port)
ThreadCount = 0

sk = socket.socket()

try:
    sk.bind((HOST,PORT))
except socket.error as e:
    print(str(e))

print('Watting for a connection')
sk.listen(5)

def thread_client(conn):
    conn.sendall(str.encode('Welcome from server, plese type anything: ','utf-8'))
    while True:
        data = conn.recv(1024)
        rep = 'Server say: '+ data.decode('utf-8')
        if not data:
            break
        conn.sendall(rep.encode('utf-8'))
    conn.close()

if __name__ == '__main__':
    while True:
        conn,addr = sk.accept()

        print(f'Address local: {sk.getsockname()}')
        print('Connected to: ' + addr[0]+":"+str(addr[1]))
        start_new_thread(thread_client,(conn,))
        ThreadCount+=1
        print('Thread num: '+ str(ThreadCount))
    sk.close()
