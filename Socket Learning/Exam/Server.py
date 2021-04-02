import socket
import argparse
from threading import Thread

n = 6

class ClientThread(Thread):
    def __init__(self, sk, client_addr, client):
        super(ClientThread, self).__init__()
        self.sk = sk
        self.client_addr = client_addr
        self.client = client

    def run(self):
        while True:
            for i in client:
                sk.sendto(("Request from "+str(i.client_addr)).encode('utf-8'), i.client_addr)

            mess, client_addr = self.sk.recvfrom(1024)
            # print("Client send: ", mess.decode('utf-8'))
            arr = mess.decode('utf-8').split(" ")
            print(arr)

            sum = 0

            for i in range (0,len(arr)):
                sum+=int(arr[i])

            if sum == n:
                for i in self.client:
                    if client_addr == i.client_addr:
                        self.sk.sendto("Correct".encode('utf-8'), i.client_addr)
            else:
                for i in self.client:
                    if client_addr == i.client_addr:
                        self.sk.sendto("False".encode('utf-8'), i.client_addr)
            print(sum)

if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port", type = str, default=2020)
    PORT = int(parse.parse_args().port)
    client = []

    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as sk:
        sk.bind((HOST,PORT))

        while True:
            mess, client_addr = sk.recvfrom(1024)

            # for i in client:
            #     sk.sendto(("Request from "+str(i.client_addr)).encode('utf-8'), i.client_addr)
            # print("Client send: ", mess.decode('utf-8'))

            flag = True

            for i in client:
                if client_addr[1] == i.client_addr[1]:
                    flag = False

            if flag:
                print("Create thread")
                client.append(ClientThread(sk,client_addr,client))
                client[-1].start()
