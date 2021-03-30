import socket
from time import ctime

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',9050))
    sk.listen(10)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    begin = 0
    con = True
    while con:
        if begin == 0 :
            print('Wating for client')
            client_sk, client_addr = sk.accept()
            print('Dia chi client: {}'.format(client_addr))
        else:
            #nhan du lieu tu client
            data = client_sk.recv(4096)
            print(data.decode('utf-8'))
            s = ['hello' , 'bye']
            if(data.decode('utf-8') == 'Hello') :
                client_sk.send(s[0].encode('utf-8'))
                con = False
            elif (data.decode('utf-8') == 'bye') :
                client_sk.send(s[1].encode('utf-8'))
                con = False
                client_sk.close()

    sk.close()