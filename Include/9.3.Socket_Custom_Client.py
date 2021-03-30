import socket
import sys

host = '127.0.0.1'
port = 9050

def create_data(msg):
    msg = msg + '\0'
    return msg.encode()

def send_data(sk,msg):
    data = create_data(msg)
    sk.sendall(data)

def receive_data(sk):
    data = bytearray()
    msg  = ''
    while not msg:
        b = sk.recv(1024)
        if not b:
            raise ConnectionError()
        data = data + b
        if b'\0' in b:
            msg = data.rstrip(b'\0')

    msg = msg.decode('utf-8')
    return msg

if __name__ == '__main__':
    # sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # try:
    #     sk.connect(('127.0.0.1', 9050))
    # except socket.error as e:
    #     print("error: {}".format(e))
    #     sys.exit()
    # print("Da tao socket")
    #
    # msg = ('day la data').format(bytearray)
    # try:
    #     data = create_data(msg)
    #     send_data(sk,data)
    # except ConnectionError:
    #         print("Error")
    while True:
        try :
            sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sk.connect((host,port))
            data = input('nhap mess')
            if data == 'exit':
                break
            send_data(sk, data)
            print("client gui {}: ".format(data))
            data = receive_data(sk)
            print("server gui {}: ".format(data))
        except ConnectionError:
            print("Error")
            break
        finally:
            sk.close()
            print("dong ket noi")
'''
sua receive va create

'''
