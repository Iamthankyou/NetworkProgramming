import socket
import netifaces

if __name__ == '__main__':
    hostname = socket.gethostname()
    print('Host name: ', hostname)
    ip_addr = socket.gethostbyname(hostname)
    print('Ip address: ', ip_addr)

    interface = netifaces.interfaces()

    for i in interface:
        ipaddr = netifaces.ifaddresses(i)
        if netifaces.AF_INET in ipaddr:
            ip_ = ipaddr[netifaces.AF_INET]
            ip_ = ip_[0]
            print("network interface: {}".format(i))
            print("IP address: {}".format(ip_['addr']))
            print("Network mask {}".format(ip_['netmask']))
        # gateway
        gw = netifaces.gateways()
        print("default gateway: {}".format(gw['default'][netifaces.AF_INET][0]))

