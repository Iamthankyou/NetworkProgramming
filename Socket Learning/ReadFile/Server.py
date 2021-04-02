import socket
import argparse
import os
from threading import Thread
import threading

# threadLock = threading.Lock()

class ClientThread(Thread):
    def __init__(self, conn, addr, client):
        super().__init__()
        self.conn = conn
        self.addr = addr
        self.client = client
        self.name = ''

    def run(self):
        try:
            self.name = self.conn.recv(1024).decode('utf-8')
            self.sendAll(("Welcome "+ self.name + "-"+ str(self.addr) + " join"))
            while True:
                # threadLock.acquire()
                mess = self.conn.recv(1024).decode('utf-8')
                # threadLock.release()

                if mess:
                    if mess == "show list":
                        self.sendOne(os.listdir().__str__())
                    else:
                        try:
                            f = open(mess,"r")
                            self.sendOne(f.read())
                        except OSError as e:
                            self.sendOne(e.__str__())
        except Exception as e:
            print(e)

    def sendOne(self,mess):
        for client in self.client:
            client.conn.send(mess.encode('utf-8'))

    def sendAll(self,mess):
        self.conn.send(mess.encode('utf-8'))


if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port",type=str,default = 2020)
    PORT = int(parse.parse_args().port)
    client = []
    with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as sk:
        sk.bind((HOST,PORT))
        sk.listen(10)
        print("Watting client connect..")
        while True:
            conn, addr = sk.accept()
            try:
                print("Connected by + ",addr)
                client.append(ClientThread(conn,addr,client))
                client[-1].start()
            except Exception as e:
                print(e)

