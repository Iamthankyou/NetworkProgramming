import netifaces
import socketServer
import dns.reversename

if __name__ == '__main__':
    hostname = socketServer.gethostname()
    ip_addr  = socketServer.gethostbyname(hostname)
    print('hostname: ',hostname)
    print('IP Address: ', ip_addr)
    dns = dns.reversename.from_address('125.212.247.5')
    print('Domand name: {}'.format(dns))

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

