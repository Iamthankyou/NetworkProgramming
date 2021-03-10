import socket
import time
#SERVER

if __name__ == '__main__':
    host = 'localhost'
    port = 4008
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    s.listen(1)
    print("Server listening on port", port)

    c, addr = s.accept()
    print("Connect from ", str(addr))

    s = c.recv(1024)

    s = s.decode()
    arr = s.split()

    print("Sum two number: ")
    print(int(arr[0])+int(arr[1]))

#    if s.decode() == "GET TIME":
 #       print(time.time())

    #c.send(b"Hello, how are you")
    #c.send("Bye", encode())
    c.close()