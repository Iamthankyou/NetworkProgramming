import socket
import argparse
ClientSocket = socket.socket()
host = 'localhost'

parse = argparse.ArgumentParser()
parse.add_argument("-port",type = str,default=2020)
args = parse.parse_args()

PORT = int(args.port)

print('Waiting for connection')
try:
    ClientSocket.connect((host, PORT))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
while True:
    Input = input('Say Something: ')
    ClientSocket.send(Input.encode('utf-8'))
    Response = ClientSocket.recv(1024)
    print(Response.decode('utf-8'))

ClientSocket.close()