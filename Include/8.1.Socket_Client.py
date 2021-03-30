import socket
import sys
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

    con = True
    begin = 0
    while con:
        if begin == 0:
           print('Bat dau cuoc tro chuyen:')
           begin = 1
           data = 'Hello'
           sk.send(data.encode('utf-8'))
        else:

            data = input('Nhap')
            sk.send(data.encode('utf-8'))
        data = sk.recv(4096)
        if data == 'bye':
            begin = 0
            con = False
        if not data:
            break
        print("server gui: ")
        print(data.decode('utf-8'))
    sk.close()
