import socket
import argparse
from clientThread import ClientThread

if __name__ == '__main__':
    HOST = 'localhost'
    parse = argparse.ArgumentParser()
    parse.add_argument("-port", type=str, default=2020)
    PORT = int(parse.parse_args().port)
    client = []

    # with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sk:
    #     sk.bind((HOST, PORT))
    #     sk.listen(4)
    #     print("Server listening")
    #     while True:
    #         conn, addr = sk.accept()
    #         with conn:
    #             try:
    #                 print('Connected by ', addr)
    #                 client.append(ClientThread(conn, addr, client))
    #                 client[-1].start()
    #             except Exception as e:
    #                 print(e)


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen(4)
        print('Server is listening...')
        while True:
            conn, addr = s.accept()
            with conn:
                try:
                    print('Connected by', addr)
                    client.append(ClientThread(conn, addr, client))
                    client[-1].start()
                except Exception as e:
                    print(e)