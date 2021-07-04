import socket
import netifaces
import dns.reversename
import dns.resolver

if __name__ == '__main__':
    #hostname = socket.gethostname()
    #hostname = 'www.baomoi.com'
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    print('host',hostname)
    print('Ip address: ',ip_addr)

    #Chuyen tu ip sang ten mien
    # dn = dns.reversename.from_address('118.102.1.125')
    # print("Ten mien: {}".format(dn))

    #Lay cac giao dien mang
    gd = netifaces.interfaces()
    for i in gd:
        ipaddr = netifaces.ifaddresses(i)
        if netifaces.AF_INET in ipaddr:
            ip_ = ipaddr[netifaces.AF_INET]
            ip_ = ip_[0]
            print("network interface: {}".format(i))
            print("IP address: {}".format(ip_['addr']))
            print("Network mask {}".format(ip_['netmask']))
    #gateway
    gw = netifaces.gateways()
    print("default gateway: {}".format(gw['default'][netifaces.AF_INET][0]))

