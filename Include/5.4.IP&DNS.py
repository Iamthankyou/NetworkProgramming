from  geoip import geolite2
import socket

if __name__ == '__main__':
    #hostname = socket.gethostname()
    hostname = 'www.baomoi.com'
    ip_addr = socket.gethostbyname(hostname)
    print('ip: {}'.format(ip_addr))

    kq = geolite2.lookup(ip_addr)
    if kq is not None:
        print("Country: :",kq.Country)
        print("Time zone: ",kq.timezone)