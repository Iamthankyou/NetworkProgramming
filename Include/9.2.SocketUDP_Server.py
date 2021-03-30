import socket

if __name__ == '__main__':
    # tao socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sk.bind(('127.0.0.1',9050))

    while True:
        #nhan du lieu
        data, client_addr = sk.recvfrom(1024)
        print("Dia chi client {}: ".format(client_addr))
        print(data)
        sk.sendto(data, client_addr)
        if(data.decode('utf-8') == 'bye'): break
    sk.close()