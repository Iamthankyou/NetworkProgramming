import socket
from time import ctime

def convert_string(string):
    s = string[0].upper() + string[1:]
    new = ""
    id = 0
    for c in s:
        if s[id-1] == '.' and  s[id+1] != ' ':
            new = new + ' ' + c.upper()
        elif s[id-1] == ',' and s[id+1]  != ' ':
            new = new + ' ' + c
        elif id + 1 == len(s):
            new = new + c
        else:
            new = new + c
        id = id + 1
    return new

if __name__ == '__main__':
    sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sk.bind(('127.0.0.1',9050))
    sk.listen(10)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    while True:
        print('Wating for client')
        client_sk, client_addr = sk.accept()
        print('Dia chi client: {}'.format(client_addr))
        #nhan du lieu tu client
        data = client_sk.recv(4096)
        print(data.decode('utf-8'))
        # if data.decode('utf-8') == 'Get time':
        #     #gui lai client
        #     data = 'Hello client'
        #     client_sk.send(bytes(ctime(),'utf-8'))
        #     client_sk.close()
        # else :
        #     # gui lai client
        #     data = 'Hello client'
        #     client_sk.send(data.encode('utf-8'))
        #     client_sk.close()

        # a,b = map(int,(data.decode('utf-8').split(',')))
        # c = a+b
        # data = str(c)
        # client_sk.send(data.encode('utf-8'))
        # client_sk.close()
        new = convert_string(data.decode('utf-8'))
        client_sk.send(new.encode('utf-8'))
        client_sk.close()

    sk.close()