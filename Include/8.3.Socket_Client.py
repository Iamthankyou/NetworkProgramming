import socket
import sys
from time import ctime
'''
 TODO : client gui ten file 
        server gui lai file

'''
if __name__ == '__main__':
    # tao socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # ket noi voi server
    try:

        sk.connect(('127.0.0.1', 9050))
    except socket.error as e:
        print("error: {}".format(e))
        sys.exit()
    print("Da tao socket")


    while True:

        data = input('Nhap vao ten file: ')
        sk.send(data.encode('utf-8'))
        while True:
            data = sk.recv(40960)
            if data == '\nhet file':
                data = input('Nhap vao ten file: ')
                sk.send(data.encode('utf-8'))
            if not data:
                break
            else:
                print("server gui: ")
                print(data.decode('utf-8'))
    sk.close()
