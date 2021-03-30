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
            data = sk.recv(4096)
            if data == 'het file':
                data = input('Nhap vao ten file: ')
                sk.send(data.encode('utf-8'))
            if not data:
                break
            else:
                try :
                    f = open("D:/Python/Code/LapTrinhMang/Nhan/results.txt",'a')
                except FileNotFoundError:
                    print("Khong tim thay file in ")
                    sys.exit()
                f.write(data.decode('utf-8'))
                print("server gui: ")
                print(data.decode('utf-8'))
                f.close()
    sk.close()