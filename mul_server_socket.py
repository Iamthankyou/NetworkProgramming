import socket
import selectors

HOST = 'localhost'
PORT = 65432

if __name__ == '_main__':
    sel = selectors.DefaultSelector()

    lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    lsock.bind((HOST,PORT))
    lsock.listen()
    print('Listening on', (HOST,PORT))
    lsock.setblocking(False)
    sel.register(lsock,selectors.EVENT_READ,data = None)

