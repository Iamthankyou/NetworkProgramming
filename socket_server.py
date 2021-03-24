import socket
from time import ctime
if __name__ == '__main__':
    # server
    sk1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk1.bind(('127.0.0.1', 9050))
    sk1.listen(10)
    sk1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    while True:
        print("Waiting for client...")
        client_sk1, client_addr = sk1.accept()
        print("Dia chi client: {}".format(client_addr))
        # nhan du lieu tu client
        data = client_sk1.recv(4096)
        print(data.decode('utf-8'))
        filename = data.decode('utf-8')
        ser_data = open(filename,'rt')
        s = ser_data.readlines()
        str = ""
        for line in s:
            client_sk1.send(line.encode('utf-8'))
        #val=" ".join(data.decode('utf-8').split())
        # val = " ".join((filter(lambda x:not x.__eq__(" "),data.decode('utf-8').split())))
        # s = []
        # for x in val:
        #     s.append(x)
        #a=s[0]
        #b=s[1]
        # s[0]=s[0].upper()
        # if s[-1]!=".":
        #     s.append('.')
        # for i,x in enumerate(s):
        #     if x.__eq__(".") and i+1<len(s):
        #         s.insert(i + 1, ' ')
        #         s[i+2]=s[i+2].upper()
        #     if x.__eq__(",") and not s[i+1].__eq__(" "):
        #         s.insert(i+1,' ')

        '''
        d=0
        for x in s:
            d=d+int(x)
        #data=int(s[0])+int(s[1])
        
        data1="{}".format(d)
        '''
        # client_sk1.send("".join(s).encode('utf-8'))
        #client_sk1.send(str.encode('utf-8'))
        '''
        if data.decode('utf-8')=='GET TIME':
            client_sk1.send(bytes(ctime(),'utf-8'))
        '''

        '''
        # gui lai client
        data = 'Hello client'
        client_sk1.send(data.encode('utf-8'))
        '''

        #client_sk1.close()
    #sk1.close()