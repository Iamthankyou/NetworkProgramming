import socket
import argparse
# from clientThread import ClientThread
from threading import Thread

class ClientThread(Thread):
    def __init__(self, conn, addr, client):
        super().__init__()
        self.conn = conn
        self.addr = addr
        self.client = client
        self.mess = ''

    def run(self):
        try:
            self.mess = self.conn.recv(1024).decode('utf-8')
            self.sendMessJoin(self.mess)
            while True:
                s = self.conn.recv(1024).decode('utf-8')
                if s:
                    self.sendMess(s)

        except Exception as e:
            print(e)

    def sendMessJoin(self, name):
        self.conn.send("Welcome from server".encode('utf-8'))
        for client in self.client:
            # if client.is_alive() and client.conn != self.conn:
            client.conn.send((name + " join server").encode('utf-8'))

    def sendMess(self, message):
        for client in self.client:
            # if client.is_alive() and client.conn != self.conn:
            client.conn.send(message.encode('utf-8'))

if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port", type=str, default=2020)
    PORT = int(parse.parse_args().port)
    client = []

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
        sk.bind((HOST, PORT))
        sk.listen(4)
        print("Server listening")

        while True:
            conn, addr = sk.accept()
            # with conn:
            try:
                print('Connected by ', addr)
                client.append(ClientThread(conn, addr, client))
                client[-1].start()
            except Exception as e:
                print(e)

    # sk = socket.socket()
    #
    # try:
    #     sk.bind((HOST, PORT))
    # except socket.error as e:
    #     print(str(e))
    #
    # print('Watting for a connection')
    # sk.listen(5)
    #
    # while True:
    #     conn,addr = sk.accept()
    #
    #     print(f'Address local: {sk.getsockname()}')
    #     print('Connected to: ' + addr[0]+":"+str(addr[1]))
    #     client.append(ClientThread(conn, addr, client))
    #     client[-1].start()
    #
    # sk.close()
