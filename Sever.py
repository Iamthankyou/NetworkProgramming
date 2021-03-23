# Server
import socket
import datetime

if __name__ == "__main__":
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.bind(("127.0.0.1", 9050))
    sk.listen(100)
    sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    while True:
        print("Waiting for client...")
        client_sk, client_addr = sk.accept()
        print("Dia chi client: {}".format(client_addr))
        while True:
            data = client_sk.recv(4096) # Nhận data từ client
            # print(data.decode('utf-8'))
            # Xử lý dữ liệu
            val = data.decode('utf-8')
            value1 = ""
            try:
                f = open('Data\\' + val, 'r')
                value1 = f.read()
                print(value1)
            except:
                value1 = "Error: Không có file tên '" + val + "'"
            data = value1
            # gửi lại client
            client_sk.send(data.encode('utf-8'))
            if val == "/stop":
                print("client_sk.close()")
                client_sk.close()
                break
    sk.close()
