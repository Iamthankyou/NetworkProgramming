# su dung ky tu dac biet de bao hieu ket thuc
'''
    @ de bat dau
    # de ket thuc
    gui lai
'''

import socket

if __name__ == '__main__':
    # tao socket
    sk = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_addr = ('127.0.0.1', 9050)

    while True:
        data = 'Test gui data'
        sk.sendto(data.encode('utf-8'),server_addr)
        data,addr = sk.recvfrom(1024)
        print('server feedback: {}'.format(data))
        if data.decode('utf-8') == 'bye':
            break
        if not data:
            break
    sk.close()