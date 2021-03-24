import socket
import sys

#Viet chuong trinh client server
#client ket noi thi gui "Hello server" den server
#server accept, in dia chi client, gui lai "Hello client" den client
if __name__ == '__main__':

    sk=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        sk.connect(('127.0.0.1',9050))

    except socket.error as e:
        print("error : {}".format(e))
        sys.exit()
    print("Da tao socket")

    while True:
        #data="  bui   tien bac.do xuan canh"
        data = "yeuem5000"
        sk.send(data.encode('utf-8'))
        #nhan du lieu tu server
        data=sk.recv(4096)
        if not data:
            break
        print("Server gui : ")
        print(data.decode('utf-8'))
    sk.close()
