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

    while True:
        #data = 'GET / HTTP/1.0\r\n\r\n'
        #data = '3,4'
        data = 'hello word.hello word again.'

        sk.send(data.encode('utf-8'))
        #nhan dl tu server
        data = sk.recv(4096)
        if not data:
            break
        print("server gui: ")
        print(data.decode('utf-8'))
    sk.close()
