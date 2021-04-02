import socket
import argparse
import os
from threading import Thread

class ClientThread(Thread):
    def __init__(self,sk, client_addr, client):
        super(ClientThread, self).__init__()
        self.sk = sk
        self.client = client
        self.name = ''
        self.client_addr = client_addr

    def run(self):
        while True:
            mess, addr = self.sk.recvfrom(1024)
            for i in client:
                i.sk.sendto(("Send : " + mess.decode('utf-8')).encode('utf-8'), i.client_addr)
            # self.sk.sendto(("Send : " + mess.decode('utf-8')).encode('utf-8'), self.client_addr)

count = 0
if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port", type = str, default=2020)
    PORT = int(parse.parse_args().port)
    client = []

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sk:
        sk.bind((HOST,PORT))
        while True:
            print(len(client))
            mess, client_addr = sk.recvfrom(1024)
            print(client_addr, " request")
            flag = True
            for i in client:
                if i.client_addr[1] == client_addr[1]:
                    flag = False

            if flag == False:
                print("continue")
                continue

            client.append(ClientThread(sk, client_addr, client))
            client[-1].start()
