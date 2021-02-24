import netifaces
import socket

if __name__ == '__main__':
    hostname = socket.gethostname()
    ip_addr  = socket.gethostbyname(hostname)
    print('hostname: ',hostname)
    print('IP Address: ', ip_addr)

    # Lay cac giao dien mang
    gd = netifaces.interfaces()
    for i in gd:
        ipaddr = netifaces.ifaddresses(i)
        if netifaces.AF_INET in ipaddr:
            ip_ = ipaddr[netifaces.AF_INET]
            ip_ = ip_[0]
            print('Network interface:{} '.format(i))
            print('IP Address: {}'.format(ip_['addr']))
            print('Network mask: {}'.format(ip_['netmask']))

    #Gateway
    gateway = netifaces.gateways()
    print('Default gateway: {}'.format(gateway['default'][netifaces.AF_INET][0]))

