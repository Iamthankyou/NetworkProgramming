import socket
host = '127.0.0.1'
port = 9050

def create_socket(host, port):
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sk.bind((host, port))
    sk.listen(10)
    return sk


def create_data(msg):
    msg =  msg + '\0'
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
    sk1 = create_socket(host, port)
    print('dia chi server: {}'.format(host,port))
    #sk1.getsockname()
    while True:
        client_socket, addr = sk1.accept()
        print("dia chi client: {}".format(addr))
        try :
            msg = receive_data(client_socket)
            print("{}:{}".format(client_socket,msg))
            send_data(client_socket, msg)
        except ConnectionError:
            print("Error")
        finally:
            print("Dong ket noi")
            client_socket.close()




