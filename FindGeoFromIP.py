from geoip2 import *
import socket

if __name__ == '__main__':
    hostname = 'www.baomoi.com'
    print('hostname: ', hostname)
    ip_addr = socket.gethostbyname(hostname)
    print('ip:{}'.format(ip_addr))

    # Lookup find infor on ip:
    kq = geolite2.lookup(ip_addr)
    if kq is not None:
        print('Country: ',kq.coutry)
        print('Time zone: ', kq.timezone)
